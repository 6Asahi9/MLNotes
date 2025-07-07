# 📦 Core libraries for data handling and cleaning
import pandas as pd
import re
from transformers import AutoTokenizer

# 🧠 Load a pretrained tokenizer (BERT lowercase version)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# 🧾 Sample feedback data with mixed tone and formatting
data_dict = {
    "text": [
        "  The staff was very kind and attentive to my needs!!!  ",
        "The waiting time was too long, and the staff was rude. Visit us at http://hospitalreviews.com",
        "The doctor answered all my questions...but the facility was outdated.   ",
        "The nurse was compassionate & made me feel comfortable!! :) ",
        "I had to wait over an hour before being seen.  Unacceptable service! #frustrated",
        "The check-in process was smooth, but the doctor seemed rushed. Visit https://feedback.com",
        "Everyone I interacted with was professional and helpful.  "
    ],
    "label": ["positive", "negative", "neutral", "positive", "negative", "neutral", "positive"]
}

# 🧱 Convert data into a structured table
data = pd.DataFrame(data_dict)

# 🧹 Clean text: normalize case, strip URLs, punctuation, and extra spaces
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Apply cleaning to all rows
data["cleaned_text"] = data["text"].apply(clean_text)

# 🏷️ Convert text labels to numerical codes
label_map = {"positive": 0, "neutral": 1, "negative": 2}
data["label"] = data["label"].map(label_map)

# 🧠 Convert cleaned text into token IDs using BERT tokenizer
data['tokenized'] = data['cleaned_text'].apply(lambda x: tokenizer.encode(x, add_special_tokens=True))

# 🔁 Ensure all token sequences are the same length (128 tokens max)
data['padded_tokenized'] = data['tokenized'].apply(
    lambda x: x + [tokenizer.pad_token_id] * (128 - len(x)) if len(x) < 128 else x[:128]
)

# 👀 Quick peek to confirm transformation
print(data[['cleaned_text', 'label', 'padded_tokenized']].head())
