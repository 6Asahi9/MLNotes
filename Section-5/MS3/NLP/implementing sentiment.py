from transformers import pipeline

# Load a ready-to-use sentiment analysis model
analyze_sentiment = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print("✅ Sentiment analysis model is ready!\n")

# Example texts to test
sample_texts = [
    "I absolutely love this product, it's fantastic!",
    "Terrible service. I’m really unhappy.",
    "It's alright, nothing special but not too bad."
]

# Analyze each sample text
for txt in sample_texts:
    output = analyze_sentiment(txt)[0]
    print(f"Text: {txt}")
    print(f"Sentiment: {output['label']} (Confidence: {output['score']:.2f})\n")

# Take custom input from the user
user_text = input("Type a sentence to check its sentiment: ")
result = analyze_sentiment(user_text)[0]
print(f"\nYour Sentiment: {result['label']} (Confidence: {result['score']:.2f})")

# Test with a longer paragraph
paragraph = """
The product overall is quite good, though the battery drains a little fast. 
I wish it lasted longer, but I do like the sleek design and smooth performance.
"""
long_result = analyze_sentiment(paragraph)[0]
print(f"\nParagraph Sentiment: {long_result['label']} (Confidence: {long_result['score']:.2f})")
