import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import transforms
from torchvision.utils import save_image
from PIL import Image
import matplotlib.pyplot as plt

# Temel U-Net yapısı
class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 3, kernel_size=3, stride=1, padding=1),
            nn.Tanh()  # Tanh çıkışını kullanıyoruz, bu yüzden -1 ile 1 arasına dönüşecek
        )
    
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# Difüzyon Modeli
class DiffusionModel(nn.Module):
    def __init__(self, unet):
        super(DiffusionModel, self).__init__()
        self.unet = unet
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # Modelin cihazını belirtiyoruz
        self.timesteps = 1000
        self.betas = torch.linspace(0.0001, 0.02, self.timesteps).to(self.device)  # self.device kullanarak cihazı belirtiyoruz

    def forward(self, x, t):
        noise = torch.randn_like(x).to(self.device)
        return self.unet(x * (1 - self.betas[t]) + noise * self.betas[t])

    def backward(self, x, t):
        return self.unet(x)

# Yüksek Frekans Yönlendirme ve İçerik Tutarlılığı Yönlendirme Stratejileri
def high_frequency_guidance(image):
    # DWT (Discrete Wavelet Transform) kullanarak yüksek frekans bileşenlerini çıkarma
    # Burada DWT yerine basit bir kenar algılama kullanılıyor
    return F.conv2d(image, torch.tensor([[[[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]]]).to(image.device), padding=1)

def content_consistent_guidance(image, noisy_image):
    # İçerik tutarlılığını sağlamak için orijinal görüntü ile karşılaştırma
    return F.mse_loss(image, noisy_image)

# Resim yükleme ve dönüştürme fonksiyonu
def load_and_preprocess_image(image_path, target_size=(128, 128)):
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize(target_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    image = transform(image).unsqueeze(0)  # Modelin beklediği şekilde boyut ekle
    return image

# Resmi kaydetme fonksiyonu
def save_image(tensor, file_path):
    unloader = transforms.ToPILImage()
    image = tensor.cpu().clone()  # Veriyi CPU'ya taşı ve kopyala
    image = image.squeeze(0)  # Boyutları uygun hale getir
    
    # Tanh çıkışını -1 ile 1 arasında, 0 ile 1 arasına dönüştürüyoruz
    image = image * 0.5 + 0.5
    image = unloader(image)
    image.save(file_path)

# Resmi görselleştirme fonksiyonu
def show_image(tensor, title=None):
    image = tensor.cpu().clone()  # Veriyi CPU'ya taşı ve kopyala
    image = image.squeeze(0)  # Boyutları uygun hale getir
    
    # Tanh çıkışını -1 ile 1 arasında, 0 ile 1 arasına dönüştürüyoruz
    image = image * 0.5 + 0.5
    image = transforms.ToPILImage()(image)
    plt.imshow(image)
    if title is not None:
        plt.title(title)
    plt.show()

# Resmi iyileştirme fonksiyonu
def enhance_image(super_res_model, image_path, output_path):
    super_res_model.eval()  # Modeli değerlendirme moduna al
    image = load_and_preprocess_image(image_path).to(super_res_model.device)  # Model cihazına taşı
    
    # Modeli ileri ve geri difüzyon işlemi için kullan
    with torch.no_grad():
        for t in reversed(range(super_res_model.timesteps)):
            noisy_image = super_res_model.forward(image, t)
            image = super_res_model.backward(noisy_image, t)
    
    # İyileştirilmiş görüntüyü kaydet
    save_image(image, output_path)
    print(f"İyileştirilmiş resim {output_path} konumuna kaydedildi.")
    show_image(image, "İyileştirilmiş Resim")

# Cihaz ayarı (GPU varsa cuda yoksa cpu)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# UNet ve DiffusionModel oluşturma
unet = UNet().to(device)
super_res_model = DiffusionModel(unet).to(device)

# Kullanım örneği (Dosya yollarını raw string olarak belirtiyoruz)
image_path = r"C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Image quality enhancement\New folder\image.png"
output_path = r"C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Image quality enhancement\New folder\iyilestirilmis_resim.png"

# Resmi iyileştirme
enhance_image(super_res_model, image_path, output_path)