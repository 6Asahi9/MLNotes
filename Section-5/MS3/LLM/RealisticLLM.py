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

# 🧠 Load a pretrained BERT model for 3-way classification
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

# ⚙️ Set training parameters: batch size, learning rate, logging, etc.
training_args = TrainingArguments(
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    output_dir='./results',
    evaluation_strategy="epoch",      # Validate after each epoch
    logging_strategy="epoch",         # Log training progress every epoch
    logging_dir='./logs',
    save_strategy="epoch",            # Save model checkpoint per epoch
    load_best_model_at_end=True       # Restore best checkpoint after training
)
# ----------------------------------------------------------------------- Added by GPT
# The data DataFrame looks like this:

# text	label	cleaned_text	tokenized	padded_tokenized

# But Trainer doesn’t train on raw pandas DataFrames.
# You’re supposed to convert data into a HuggingFace Dataset object, like this:
from datasets import Dataset
train_dataset = Dataset.from_pandas(data)
# But even that isn’t enough.
# To actually work with BERT, you’re supposed to add two specific keys:
# "input_ids" → the list of padded token IDs

# "attention_mask" → a 1/0 mask telling which tokens are real (1) or padding (0)

# So before .with_format("torch"), you usually do something like

def process(row):
    ids = row["padded_tokenized"]
    mask = [1 if token != tokenizer.pad_token_id else 0 for token in ids]
    return {"input_ids": ids, "attention_mask": mask}

processed = data.apply(process, axis=1, result_type="expand")
data["input_ids"] = processed["input_ids"]
data["attention_mask"] = processed["attention_mask"]

# Then and only then, does this make sense:
train_dataset = Dataset.from_pandas(data)
train_dataset = train_dataset.with_format("torch", columns=["input_ids", "attention_mask", "label"])
# Because now train_dataset does have those columns.
# -----------------------------------------------------------------------

# 🎯 Initialize Trainer with training loop setup and dataset
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset.with_format("torch", columns=["input_ids", "attention_mask", "label"]),
    eval_dataset=val_dataset.with_format("torch", columns=["input_ids", "attention_mask", "label"])
)

# 🚀 Start training the model
trainer.train()

# 📊 Evaluate performance on test set
from sklearn.metrics import accuracy_score, f1_score

test_dataset = test_dataset.with_format("torch", columns=["input_ids", "attention_mask", "label"])
predictions = trainer.predict(test_dataset)
preds = predictions.predictions.argmax(-1)
labels = test_dataset["label"]

# 📈 Calculate evaluation metrics
accuracy = accuracy_score(labels, preds)
f1 = f1_score(labels, preds, average="weighted")

print(f"Accuracy: {accuracy}, F1 Score: {f1}")

# 💾 Save the trained model and tokenizer for future use
model.save_pretrained("./fine_tuned_bert")
tokenizer.save_pretrained("./fine_tuned_bert")
print("Model saved successfully!")

