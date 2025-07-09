
---

## ✨ Text Data Augmentation (Rewritten for Notes)

**Text augmentation** is the process of creating extra training samples by modifying existing text.
This can help models perform better — especially when you're working with limited data — by exposing them to more diverse examples.

However, not all methods are equal, and each comes with its own trade-offs.

---

### 🔁 **Paraphrasing**

**What it means:**
Rewriting a sentence using different words or structure, while keeping the original meaning.

**When it helps:**
Great when you have a small dataset and want more variation without altering the message. It also makes your model more flexible with different writing styles.

**Benefits:**

* Adds variety while keeping the core meaning
* Useful for tasks like text generation, translation, or summarization

**Downsides:**

* Some paraphrases may slightly shift the meaning
* Quality paraphrasing can be time-consuming or require tools that aren’t always accurate

---

### 🌍 **Back Translation**

**What it means:**
Translate a sentence into another language, then back into the original — creating a new version with a different structure.

**When it helps:**
Useful in multilingual settings or when you want to keep meaning while shifting phrasing.

**Benefits:**

* Produces natural-looking sentence variations
* Helps improve generalization across different language structures

**Downsides:**

* Relies heavily on translation tools — poor translations can twist meaning
* May introduce grammatical errors if the tools aren't reliable

---

### 🔄 **Synonym Replacement**

**What it means:**
Swap words in the sentence with similar words (synonyms) to create new versions.

**When it helps:**
Useful for classification tasks like sentiment analysis, where different words express the same idea.

**Benefits:**

* Simple to apply
* Increases data size while preserving meaning most of the time

**Downsides:**

* Meaning can be lost if synonyms don’t fit the context
* Too many swaps can make sentences sound unnatural or awkward

---

Want me to turn this into flashcards, collapsible Notion bullets, or something cute with Miya as the mascot of each technique? 🐾💗
