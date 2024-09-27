from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# İngilizce stopwords'leri yükleyin
stop_words = set(stopwords.words('english'))

# Örnek cümle
sentence = "The cats are running in the garden and playing with each other."

# Tokenization
words = word_tokenize(sentence)

# Küçük harfe dönüştürme ve noktalama işaretlerini kaldırma
words = [word.lower() for word in words if word.isalnum()]

# Stopwords'leri kaldırma
words = [word for word in words if word not in stop_words]

# Stemming (Kök çıkarma)
porter_stemmer = PorterStemmer()
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Lemmatization (Lemmatizasyon)
wordnet_lemmatizer = WordNetLemmatizer()
lemmatized_words = [wordnet_lemmatizer.lemmatize(word) for word in words]

# Sonuçları yazdırma
print(f"Orijinal Cümle: {sentence}")
print(f"Tokenlar: {words}")
print(f"Stemmed Kelimeler: {stemmed_words}")
print(f"Lemmatized Kelimeler: {lemmatized_words}")
