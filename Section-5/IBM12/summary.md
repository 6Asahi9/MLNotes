Ahhh got it, Asahi 😏💖 — here’s a **compact note version** you can drop straight into your notebook: (Main Summary in drive)

---

**Transformer / Autoregressive Model Notes:**

* **Autoregressive:** Generates sequences **one token at a time**, predicting the next token from previous tokens.
* **Causal Mask:** Prevents the model from seeing future tokens while generating, ensuring **no “cheating”**.
* **Self-Supervised Learning:** Trains the model by predicting masked or next tokens **without explicit labels**, learning patterns from raw data.
* **Transformer Block Flow:**

  1. **Input Embedding + Positional Encoding** →
  2. **Masked Multi-Head Attention** → **Add & Norm**
  3. **Feed-Forward Layer** → **Add & Norm**
  4. Output goes to **next block** (repeat “so on” for multiple layers)
* **Add & Norm:** Keeps original info via **residual connections** + stabilizes values via **layer normalization**.
* **Feed-Forward Layer:** Applies a **small neural network** to each token independently, introducing **non-linearity**.

Language Modeling & Transformers: Glossary

Add and Norm – A technique that increases model depth while helping stabilize gradients during training.

Argmax Process – A method used to select the token index of the predicted word, often following self-attention.

Attention Mechanism – A component in neural networks that assigns weights to inputs, focusing on the most relevant parts when generating outputs.

Autoregressive Model – A model that generates sequences by predicting each new token based on all previous tokens.

BERT – An open-source, deeply bidirectional language model trained unsupervised on plain text corpora for rich contextual understanding.

Contextual Embeddings – Word representations that capture meaning depending on surrounding words within a sequence.

Data Loader – A utility that fetches and organizes data from sources in batches for training models.

Decoder Models – Network architectures primarily used for sequence-to-sequence tasks, generating output sequences from encoded representations.

Fine-Tuning – A supervised training step where a pretrained model is adapted for a specific downstream task, such as question answering or classification.

Generative Pre-Training (GPT) – A self-supervised approach where a decoder predicts the next token in a sequence to learn language patterns.

Language Models – Models that predict text by analyzing previous tokens, often with context length as a key parameter.

Masked Language Modeling (MLM) – A training method where certain words in a sentence are hidden, and the model learns to reconstruct them.

Masking – The process of selectively hiding or ignoring certain tokens during model computation.

Multi-Head Attention – A mechanism performing several scaled dot-product attentions in parallel to capture different relational aspects of the input.

Next Sentence Prediction (NSP) – A pretraining task where the model predicts whether one sentence logically follows another.

One-Hot Encoding Approach – A way to represent categorical features as binary vectors in a matrix or vector space.

Orthogonality – A property in systems or databases where components operate independently and without interference.

Positional Encoding – A technique for embedding sequence position information into input data for transformers.

PyTorch – An open-source deep learning framework combining Torch’s computational library with Python for building neural networks.

Python Dictionary – A built-in data structure storing key-value pairs for fast access and modification.

Reinforcement Learning from Human Feedback (RLHF) – A fine-tuning approach that improves model behavior using feedback from humans, often used in chatbots.

Scaled Dot-Product Attention – An attention mechanism computing the dot product of queries and keys, scaled to avoid overly large values, followed by weighted combination with values.

Self-Attention Mechanism – Computes attention weights for each token in a sequence to capture dependencies between all words.

Semantic – Refers to the meaning or interpretation of language in NLP.

Simple Language Modeling – A neural architecture that predicts the next word in a sequence, forming the basis of natural language understanding.

Softmax Function – Converts raw scores into probabilities, making them interpretable for classification tasks.

Tokenization – The process of splitting text into discrete units (tokens) for model input.

Transformer Model – A neural network model capable of processing and translating text or speech efficiently in near real-time.

Vector – A mathematical representation of numbers used in machine learning to encode data points or embeddings.

💡 Key idea: Autoregression + causal masking + attention + feed-forward + Add & Norm = sequence modeling that can **generate text coherently**.

---

If you want, I can also make a **super small Miya-themed version** of this note — cute and visual — that’ll make your notes way more fun to read 😏🐾.

Do you want me to do that?
