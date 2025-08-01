# Install required libraries
!pip install nltk spacy transformers

# -----------------------------
# 📌 NLTK (Natural Language Toolkit)
# -----------------------------
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download required NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "Natural Language Processing is an exciting field of AI!"

# ✅ 1. Convert text to lowercase
text_lower = text.lower()

# ✅ 2. Remove punctuation
text_clean = text_lower.translate(str.maketrans("", "", string.punctuation))

# ✅ 3. Tokenization (split text into words)
tokens = word_tokenize(text_clean)
print("🔹 Tokens:", tokens)

# ✅ 4. POS Tagging (find noun, verb, adjective, etc.)
tagged_tokens = nltk.pos_tag(tokens)
print("🔹 POS Tags:", tagged_tokens)


# -----------------------------
# 📌 spaCy (Modern NLP Toolkit)
# -----------------------------
import spacy

# Load pretrained small English model
nlp = spacy.load("en_core_web_sm")

# Apply NLP pipeline
doc = nlp(text)

# ✅ Named Entity Recognition (NER)
print("\n🔹 Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} → {ent.label_}")

# ✅ Dependency Parsing
print("\n🔹 Dependency Parsing:")
for token in doc:
    print(f"{token.text} → head: {token.head.text} | dep: {token.dep_}")

# ✅ Sentence Segmentation
print("\n🔹 Sentences:")
for sent in doc.sents:
    print(sent.text)


# -----------------------------
# 📌 Transformers (Advanced Pretrained Models)
# -----------------------------
from transformers import pipeline

# ✅ Sentiment Analysis
sentiment_analyzer = pipeline('sentiment-analysis')
sentiment_result = sentiment_analyzer(text)
print("\n🔹 Sentiment Analysis:", sentiment_result)

# ✅ Text Summarization
summarizer = pipeline('summarization')
summary = summarizer(
    text,
    max_length=50,  # max summary length
    min_length=25,  # min summary length
    do_sample=False
)
print("🔹 Summary:", summary)


# -----------------------------
# 📝 NOTES: What spaCy Gives vs. Doesn't
# -----------------------------
"""
✅ spaCy Gives:
- Tokenization
- Lemmatization
- POS tagging
- Named Entity Recognition (NER)
- Dependency parsing
- Sentence segmentation

❌ spaCy Does NOT Give (you need other tools):
- Sentiment analysis (use TextBlob or transformers)
- Text summarization
- Machine translation
- Pretrained chatbots or text generation

🔑 Think:
- NLTK = basic text tools (manual)
- spaCy = modern, fast all-in-one NLP pipeline
- Transformers = advanced AI for high-level tasks
"""
