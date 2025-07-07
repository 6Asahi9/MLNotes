# 🌱 Import libraries
import os
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding
)
from sklearn.metrics import accuracy_score, f1_score

# 🗂️ Sample dataset with raw user feedback (can be swapped with your own)
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

# ⏳ Load into DataFrame
data = pd.DataFrame(data_dict)

# 🧹 Clean the input text: lowercase, strip spaces, remove URLs and symbols
def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text

data["cleaned_text"] = data["text"].apply(clean_text)

# 🧾 Encode categorical labels into numeric form
data["label"] = data["label"].astype("category").cat.codes  # e.g., positive → 2

# 🔠 Load BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# 📦 Tokenize text into input IDs and attention masks (with truncation & padding)
def tokenize_function(text):
    return tokenizer(text, truncation=True, padding="max_length", max_length=128)

data["tokenized"] = data["cleaned_text"].apply(tokenize_function)
data["input_ids"] = data["tokenized"].apply(lambda x: x["input_ids"])
data["attention_mask"] = data["tokenized"].apply(lambda x: x["attention_mask"])
data = data.drop(columns=["tokenized"])  # remove redundant column

# 🎲 Split data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# 🔁 Convert to Hugging Face Datasets format
train_dataset = Dataset.from_pandas(train_data)
test_dataset = Dataset.from_pandas(test_data)

# 🧽 Remove unused columns (we only need tokenized values and labels)
train_dataset = train_dataset.remove_columns(["text", "cleaned_text"])
test_dataset = test_dataset.remove_columns(["text", "cleaned_text"])

# 📏 Handles dynamic padding per batch during training
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# ⚙️ Set training configuration
training_args = TrainingArguments(
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    output_dir="./results",
    logging_dir="./logs",
    report_to="none",  # disables external logging (like wandb)
    save_strategy="epoch",
    evaluation_strategy="epoch"
)

# 🧠 Load a pretrained BERT model for 3-class classification
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

# 🧪 Initialize Trainer with model, data, and training setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    data_collator=data_collator
)

# 🚀 Start training
trainer.train()

# 📊 Evaluate performance on test set
predictions = trainer.predict(test_dataset)
preds = predictions.predictions.argmax(-1)
labels = test_dataset["label"]

accuracy = accuracy_score(labels, preds)
f1 = f1_score(labels, preds, average='weighted')

print(f"Accuracy: {accuracy}, F1 Score: {f1}")
