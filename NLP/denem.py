import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

# Örnek metin
text = "Bu ürün tamamen doğaldır ve katkı maddesi içermez."

# Temizleme ve ön işleme işlemleri
def preprocess_text(text):
    # Küçük harfe çevir
    text = text.lower()
    # Özel karakterleri kaldır
    text = re.sub(r'[^a-zçğıöşü\s]', '', text)
    # Durdurma kelimelerini kaldır
    stop_words = set(stopwords.words('turkish'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    # Lemmatizasyon
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

processed_text = preprocess_text(text)
print(processed_text)

