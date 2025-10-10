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

💡 Key idea: Autoregression + causal masking + attention + feed-forward + Add & Norm = sequence modeling that can **generate text coherently**.

---

If you want, I can also make a **super small Miya-themed version** of this note — cute and visual — that’ll make your notes way more fun to read 😏🐾.

Do you want me to do that?
