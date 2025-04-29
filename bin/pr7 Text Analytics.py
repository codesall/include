import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')


# Sample document
document = "The quick brown fox jumps over the lazy dog. The dog was not amused by the fox."

# Tokenization
tokens = word_tokenize(document)

# POS Tagging
pos_tags = pos_tag(tokens)

# Stop words removal
stop_words = set(stopwords.words('english'))
tokens_no_stopwords = [word for word in tokens if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens_no_stopwords]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens_no_stopwords]

# Term Frequency and Inverse Document Frequency
corpus = [document]
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(corpus)

print("Tokenized Document:", tokens)
print("POS Tagging:", pos_tags)
print("Tokens without Stopwords:", tokens_no_stopwords)
print("Stemmed Tokens:", stemmed_tokens)
print("Lemmatized Tokens:", lemmatized_tokens)
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())
