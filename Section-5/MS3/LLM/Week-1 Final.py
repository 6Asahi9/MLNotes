# ---------------------------------------
# 🧠 Install necessary Hugging Face tools
# ---------------------------------------
!pip install transformers datasets

# --------------------------------------
# 📦 Import required modules from libraries
# --------------------------------------
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset
from sklearn.model_selection import train_test_split
import pandas as pd

# ------------------------------------------------------------
# 🧠 Load a pre-trained BERT model and its tokenizer for classification
# ------------------------------------------------------------
model_name = "bert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# ----------------------------
# 🎞 Load the IMDb dataset
# ----------------------------
dataset = load_dataset('imdb')  # Contains movie reviews labeled as positive or negative

# --------------------------------------------------
# 📊 Convert the Hugging Face dataset to a DataFrame
# --------------------------------------------------
df = pd.DataFrame(dataset['train'])

# ---------------------------------------------
# 🔀 Split data into training and test datasets
# ---------------------------------------------
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# -----------------------------------------------------
# ✂️ Tokenize the text using the model’s tokenizer
# Adds padding and truncation to standardize input size
# -----------------------------------------------------
def preprocess_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

# --------------------------------------------------------
# 🔁 Convert Pandas DataFrames back into HF Dataset format
# --------------------------------------------------------
from datasets import Dataset
train_data = Dataset.from_pandas(train_data)
test_data = Dataset.from_pandas(test_data)

# -------------------------------------------------------
# 🧼 Apply tokenization to all examples in the dataset
# -------------------------------------------------------
train_data = train_data.map(preprocess_function, batched=True)
test_data = test_data.map(preprocess_function, batched=True)

# -----------------------------------------------------
# ⚙️ Set up environment and training configuration
# -----------------------------------------------------
import os
import torch
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification

# Suppress unnecessary warnings and disable experiment tracking
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["MLFLOW_TRACKING_URI"] = "disable"
os.environ["HF_MLFLOW_LOGGING"] = "false"

# Use GPU if available, otherwise fallback to CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ------------------------------------------------------
# 🏃‍♂️ Switch to a lighter model (DistilBERT) for speed
# ------------------------------------------------------
model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)
model.to(device)

# ------------------------------------------------------------
# 🧪 Use smaller subsets to reduce training time (quick testing)
# ------------------------------------------------------------
train_data = train_data.select(range(1000))  # Only first 1000 training samples
test_data = test_data.select(range(200))     # Only first 200 test samples

# -----------------------------------------------
# ⚙️ Define training configuration and parameters
# -----------------------------------------------
training_args = TrainingArguments(
    output_dir='./results',               # Folder to save results
    evaluation_strategy="steps",          # Evaluate every few steps
    eval_steps=500,                       # Evaluation interval
    learning_rate=2e-5,                   # Small learning rate
    per_device_train_batch_size=8,        # Batch size for training
    num_train_epochs=1,                   # One epoch (quick test)
    weight_decay=0,                       # No weight decay (L2 regularization)
    logging_steps=500,                    # Log every 500 steps
    save_steps=1000,                      # Save checkpoint every 1000 steps
    save_total_limit=1,                   # Keep only 1 model checkpoint
    gradient_accumulation_steps=1,        # No accumulation
    fp16=False,                           # Disable half-precision training
    report_to="none",                     # Don't use external loggers like WandB
)

# -----------------------------------------------
# 🏋️ Set up the Trainer class for fine-tuning
# -----------------------------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
)

# -----------------------------
# 🚀 Begin fine-tuning training
# -----------------------------
trainer.train()

# -------------------------
# 🧪 Evaluate model results
# -------------------------
results = trainer.evaluate()

# ----------------------------
# 📢 Print out final accuracy
# ----------------------------
print(f"Accuracy: {results['eval_accuracy']}")
