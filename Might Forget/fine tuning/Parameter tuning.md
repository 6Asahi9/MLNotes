absolutely, Asahi 😌 here’s a neat summary for your notes — I’ll keep it clear and concise for easy studying:

---

### **1. Greedy Decoding**

* Picks the **single most probable token** at each step.
* ✅ Deterministic, simple
* ❌ Can be repetitive or boring

---

### **2. Top‑k Sampling**

* Picks the **next token randomly from the top k most probable tokens**.
* k = fixed number
* Higher k → more diverse output
* Weighted by each token’s probability

---

### **3. Top‑p (Nucleus) Sampling**

* Picks from the **smallest set of tokens whose cumulative probability ≥ p**.
* p = probability threshold (e.g., 0.9, 0.95)
* Dynamic number of tokens considered
* More flexible than top‑k

---

### **4. Temperature Scaling**

* Adjusts **randomness of token selection**.
* T < 1 → sharper distribution → more deterministic
* T > 1 → flatter distribution → more random/creative
* Works with top‑k or top‑p sampling

---

### **5. Beam Search**

* Keeps **b multiple candidate sequences** at each step (beams)
* Expands each beam and selects the top scoring sequences
* ✅ Produces higher-quality, coherent output
* ❌ Can be slower and less diverse

---

### **6. Min/Max Tokens**

* **Min tokens** → ensures a minimum length for output
* **Max tokens** → caps the maximum length of output

---

### **7. Repetition Penalty**

* Penalizes tokens that **repeat too often** in the generated text
* Reduces loops or repeated phrases
* Helps output stay diverse and natural

---

if you want, I can also make a **tiny table with pros/cons and quick intuition** for each, so your notes look super clean. 📝✨

do you want me to do that?
