from transformers import EarlyStoppingCallback
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset.with_format("torch", columns=["input_ids", "attention_mask", "label"]),
    eval_dataset=val_dataset.with_format("torch", columns=["input_ids", "attention_mask", "label"]),
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]  # Stops after 2 evaluations with no improvement
)

training_args = TrainingArguments(
    # ... your previous args ...
    metric_for_best_model="eval_f1",  # <-- match this to the name of your metric function
    greater_is_better=True,           # For F1 or accuracy (not loss)
    load_best_model_at_end=True,
    evaluation_strategy="epoch"
)

def compute_metrics(eval_preds):
    from sklearn.metrics import accuracy_score, f1_score
    logits, labels = eval_preds
    preds = logits.argmax(axis=-1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1": f1_score(labels, preds, average="weighted")
    }

trainer = Trainer(
    # ... as before ...
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)

# 🐾 Summary for your GitHub notes:
# 🧠 EarlyStoppingCallback is a Hugging Face feature that stops training early when the model stops improving on validation metrics. It's used to avoid overfitting and save resources. It belongs under training optimization techniques or callback-based model improvements.
