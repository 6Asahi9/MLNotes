Got it 💙 I’ll rephrase that cheat sheet in my own words so you can keep the content without copyright issues. Here’s a rewritten version:

---

# Cheat Sheet: AI Models for NLP

### PyTorch Embedding and EmbeddingBag

* **Embedding**: Creates dense vectors for tokens given their indices.
* **EmbeddingBag**: Works like Embedding but aggregates embeddings (mean/sum) in one step. Useful for text classification.

**Code Sketch**

```python
import torch
import torch.nn as nn
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator

# Sample dataset
dataset = ["I like cats", "I hate dogs", "I'm impartial to hippos"]

# Tokenizer and vocab
tokenizer = get_tokenizer("spacy", language="en_core_web_sm")
def yield_tokens(data_iter):
    for text in data_iter:
        yield tokenizer(text)

vocab = build_vocab_from_iterator(yield_tokens(iter(dataset)))
ids = [torch.tensor(vocab(tokenizer(x))) for x in dataset]

# Embedding layer
embedding_dim = 3
embeds = nn.Embedding(len(vocab), embedding_dim)
print(embeds(ids[0]))

# EmbeddingBag layer
emb_bag = nn.EmbeddingBag(len(vocab), embedding_dim, mode="mean")
print(emb_bag(ids[0], offsets=torch.tensor([0])))
```

---

### Batch Function

Used to combine multiple samples into one batch before feeding them to the model.

```python
def collate_batch(batch):
    targets, contexts, offsets = [], [], [0]
    for context, target in batch:
        targets.append(vocab[target])
        tokens = torch.tensor([vocab[t] for t in context])
        contexts.append(tokens)
        offsets.append(tokens.size(0))
    targets = torch.tensor(targets)
    offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
    contexts = torch.cat(contexts)
    return targets, contexts, offsets
```

---

### Forward Pass

The process of sending inputs through the layers of a network to generate predictions.

---

### Pre-trained GloVe in PyTorch

Load large pre-trained word embeddings for richer text representation.

```python
from torchtext.vocab import GloVe, vocab
glove = GloVe(name="6B")
vocab = vocab(glove.stoi, 0, specials=("<unk>", "<pad>"))
vocab.set_default_index(vocab["<unk>"])
```

---

### Vocabulary (`vocab`)

Maps tokens to numerical IDs.

```python
def example(iterator):
    tokens = next(iterator)
    ids = [vocab[t] for t in tokens]
    return tokens, ids
```

---

### Special Tokens

* `<bos>`: Beginning of sentence
* `<eos>`: End of sentence
* `<pad>`: Used to make all sentences the same length

---

### Cross-Entropy Loss

Measures how well predicted probabilities match actual labels. Lower is better.

---

### Optimization

Algorithms (like SGD, Adam) adjust model weights to minimize loss.

---

### BLEU Score (`sentence_bleu`)

Metric to compare generated translations with reference sentences.

---

### Encoder RNN

Processes an input sequence and passes hidden states to the decoder.

---

### Decoder RNN

Generates an output sequence token-by-token, using its previous hidden states and predictions.

---

### Skip-Gram Model

Given a target word, predicts its surrounding context words.

---

### Collate Function

Prepares a batch by converting samples into tensors.

---

### Training Function

Handles the training loop: forward pass → compute loss → backpropagation → optimizer step.

---

### CBOW Model

Predicts a target word from surrounding context words.

---

### Training Loop

Iterates through the dataset for multiple epochs, updating the model after each batch and tracking performance.

---

Would you like me to also **clean up and simplify the code** (so it’s shorter but still runnable), or do you want the **full detailed version** just like the original but rewritten?
