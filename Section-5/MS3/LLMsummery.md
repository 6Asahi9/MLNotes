# 🧠 LLMs vs ML Models + Fine-Tuning Techniques

## 🔍 What Makes LLMs Different from Traditional ML

| Aspect               | Traditional ML                        | LLMs (Large Language Models)                         |
|----------------------|----------------------------------------|------------------------------------------------------|
| **Goal**             | Solve specific tasks (e.g., spam detection, image recognition) | General-purpose language understanding & generation |
| **Data**             | Small, task-specific                  | Huge corpora (e.g., web pages, books, code)         |
| **Model Type**       | Linear models, decision trees, CNNs, etc. | Transformer-based architectures                     |
| **Training Scope**   | From scratch per task                 | Pretrained once, reused many times                  |
| **Learning**         | Task-specific                         | Generalized → then specialized (via fine-tuning)    |

---

## 🧠 What is an LLM?

A **Large Language Model** is:
- A Transformer-based neural network
- Trained on trillions of tokens (text data)
- Learns language structure, grammar, and context
- Then **fine-tuned** for specific tasks (chatbot, legal summarizer, MiyaGPT 😼)

---

## 🏗️ Pretraining vs Fine-Tuning

| Stage        | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Pretraining** | Train on broad data to learn how language works (unsupervised)             |
| **Fine-tuning** | Retrain on small, domain-specific data to focus the model on one task      |

Example:  
Train on all of Wikipedia → Fine-tune on cat medical reports 🐾

---

## ⚙️ Common Fine-Tuning Techniques for LLMs

### 1. **Full Fine-Tuning**
- Update **all** weights of the model
- Accurate but resource-heavy
- ❌ Not practical on consumer hardware

### 2. **LoRA / QLoRA (Low-Rank Adaptation)**
- Freeze most of the model
- Train **small inserted matrices**
- **QLoRA** adds quantization (memory-efficient)
- ✅ Ideal for laptops and low-end machines

### 3. **Adapter Tuning**
- Insert **tiny neural modules** (adapters) between layers
- Original model stays frozen
- Adapters are small and task-specific
- ✅ Swappable and efficient

### 4. **Prompt Tuning**
- Learn **input tokens** (prompts) that steer the model’s behavior
- Model stays frozen
- Lightweight and quick to train
- ✅ Best for small tasks or fast experiments

---

## 🧊 What Does "Frozen Model" Mean?

When a model is **frozen**, its original weights are **not updated** during training.
Only new components (like adapters, prompts, or LoRA layers) are trained.

Why freeze?
- Save compute
- Avoid overwriting knowledge
- Enable modularity

---

## 🧁 TL;DR

> LLMs = Pretrained generalist brains  
> Fine-tuning = Teaching them a specialty  
> You don’t always need massive compute — just smart tricks like LoRA and adapters 💡

---

## 🐱 Miya Edition

| Task                          | Can do on Laptop? |
|-------------------------------|-------------------|
| Pretrain GPT-3 from scratch   | ❌ Nope           |
| Fine-tune small LLM (e.g. GPT-2, Mistral) | ✅ Yes!       |
| Train tiny model (1M params)  | ✅ Yes (slow)     |
| Create MiyaGPT personality shell | ✅ Yes 🐾         |

---

### 📦 Tools You Can Try:
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [LoRA via PEFT](https://github.com/huggingface/peft)
- [QLoRA paper](https://arxiv.org/abs/2305.14314)
- [nanoGPT](https://github.com/karpathy/nanoGPT)
- [Ollama (Run LLMs locally)](https://ollama.com/)

