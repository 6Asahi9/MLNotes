Ahh yes, Asahi, now we’re getting into the **nuances**, and you’re right to be skeptical. 😼

Let’s break this carefully:

---

### **Soft Prompts / Prefix Tuning vs Additive Fine-Tuning**

1. **Soft prompts / prefix tuning:**

   * Adds **learnable vectors** to the input of **attention layers**.
   * The **original model weights stay frozen**.
   * It **doesn’t add new layers with activations**, it just **prepends something to the queries/keys** in attention.
   * ✅ Subtle: affects attention, but in a “vector prepending” way, **not a whole new layer with parameters like weights and biases**.

2. **Additive fine-tuning:**

   * Literally adds **new task-specific layers (like MLPs or small residual blocks)** into the model architecture.
   * The **original transformer layers are frozen**.
   * This matches Priya’s description: *“adds task-specific layers between attention blocks”*.

---

### **Why not Soft Prompts here?**

* Soft prompts only **prepend vectors at attention input**, they **don’t insert entire new layers**.
* Priya is **inserting new layers**, which is literally **additive fine-tuning**.

---

### **TL;DR:**

* **Prefix/soft prompt tuning** → tweaks input to attention.
* **Additive fine-tuning** → adds entirely **new layers** into the transformer.

So, despite the similarity (both are PEFT, both freeze original weights), **Priya’s scenario clearly describes additive fine-tuning**.

---

If you want, I can make a **tiny “Miya-approved diagram” showing soft prompts vs additive fine-tuning vs LoRA inside a transformer**, so it’s visually impossible to confuse. 🐾✨

Do you want me to do that?
