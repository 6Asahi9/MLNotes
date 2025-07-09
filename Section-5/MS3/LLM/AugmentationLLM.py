
---

## 🧠 **Text Cleaning, Augmentation, and Data Preparation for Sentiment Analysis using BERT**

```python
# 📦 Module Installation (for notebooks like Colab)
# The '!' lets us run shell commands (e.g., installing packages) inside a notebook environment
# !pip install transformers nltk

# 📚 Library Imports
import pandas as pd
import random
import re
import torch
from nltk.corpus import wordnet
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer
```

---

### 📥 **Load & Inspect the Dataset**

```python
# Load the dataset (make sure the CSV file is placed correctly)
# Dataset link: https://huggingface.co/datasets/stepp1/tweet_emotion_intensity/tree/main
data = pd.read_csv('data/tweet_emotion_intensity.csv')

# Take a quick peek at the data
print(data.head())
```

---

### 🧼 **Text Cleaning**

```python
# Function to clean each tweet: lowercase, remove URLs, HTML tags, and punctuation
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)          # Remove URLs
    text = re.sub(r'<.*?>', '', text)            # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text)          # Remove punctuation
    return text

# Apply cleaning function to the 'tweet' column
data['cleaned_text'] = data['tweet'].apply(clean_text)

# Preview cleaned text
print(data['cleaned_text'].head())
```

---

### 🧹 **Handle Missing Values**

```python
# Check for missing data
print(data.isnull().sum())

# Drop rows with missing cleaned text (if any)
data = data.dropna(subset=['cleaned_text'])

# Or alternatively, fill missing cleaned text with a placeholder
data['cleaned_text'].fillna('unknown', inplace=True)
```

---

### 🧠 **Tokenization with BERT**

```python
# Load pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenize the cleaned text into input IDs and attention masks
tokens = tokenizer(
    data['cleaned_text'].tolist(),
    padding=True,
    truncation=True,
    max_length=128,
    return_tensors='pt'
)

# Preview tokenized input
print(tokens['input_ids'][:5])
```

---

### 🧬 **Data Augmentation: Synonym Replacement**

```python
# Replace a word with a random synonym (if available)
def synonym_replacement(word):
    synonyms = wordnet.synsets(word)
    if synonyms:
        return random.choice(synonyms).lemmas()[0].name()
    return word

# Augment a sentence by randomly replacing words with synonyms (20% chance per word)
def augment_text(text):
    words = text.split()
    augmented_words = [
        synonym_replacement(word) if random.random() > 0.8 else word
        for word in words
    ]
    return ' '.join(augmented_words)

# Generate a new column with augmented text
data['augmented_text'] = data['cleaned_text'].apply(augment_text)
```

---

### 🎯 **Label Processing for Sentiment Intensity**

```python
# Map text intensity labels to numerical values
def map_sentiment(value):
    if value == "high":
        return 1
    elif value == "medium":
        return 0.5
    elif value == "low":
        return 0
    return None  # Handle unexpected values

# Apply mapping function to the intensity column
data['sentiment_intensity'] = data['sentiment_intensity'].apply(map_sentiment)

# Drop any rows with undefined sentiment scores
data = data.dropna(subset=['sentiment_intensity']).reset_index(drop=True)

# Convert labels to PyTorch tensor
labels = torch.tensor(data['sentiment_intensity'].tolist())
```

---

### 📦 **Prepare Dataset for Training**

```python
# Extract tokenized input tensors
input_ids = tokens['input_ids']
attention_masks = tokens['attention_mask']

# Split into training/validation/test sets
train_val_inputs, test_inputs, train_val_masks, test_masks, train_val_labels, test_labels = train_test_split(
    input_ids, attention_masks, labels, test_size=0.15, random_state=42
)

train_inputs, val_inputs, train_masks, val_masks, train_labels, val_labels = train_test_split(
    train_val_inputs, train_val_masks, train_val_labels, test_size=0.2, random_state=42
)

# Wrap data in TensorDataset
train_dataset = TensorDataset(train_inputs, train_masks, train_labels)
val_dataset = TensorDataset(val_inputs, val_masks, val_labels)
test_dataset = TensorDataset(test_inputs, test_masks, test_labels)

# Create DataLoaders for batch processing
train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=16)
test_dataloader = DataLoader(test_dataset, batch_size=16)

print("✅ Data ready: Training, validation, and test sets are prepared.")
```

---

