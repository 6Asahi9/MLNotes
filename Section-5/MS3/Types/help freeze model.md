| PERT Method        | What it does                                                        |
| ------------------ | ------------------------------------------------------------------- |
| **LoRA**           | Adds low-rank trainable matrices to frozen weights                  |
| **Prefix-tuning**  | Prepends learned tokens to the input sequence                       |
| **Adapter layers** | Adds small MLPs inside each transformer block                       |
| **BitFit**         | Only updates bias terms (very lightweight)                          |
| **IA³ / QLoRA**    | Modify key/value/query in attention; QLoRA uses quantization + LoRA |


🥊 Why use LoRA over others?
| Feature    | LoRA                   | Prefix-tuning | BitFit     | Full fine-tune   |
| ---------- | ---------------------- | ------------- | ---------- | ---------------- |
| Speed      | ✅ Fast                 | ✅ Fast        | ✅ Fastest  | ❌ Slow           |
| Memory     | ✅ Low                  | ✅ Low         | ✅ Lowest   | ❌ Huge           |
| Quality    | ✅ Good                 | Good          | Mid        | ✅ Best (usually) |
| Modularity | ✅ Easy to merge/remove | Somewhat      | Not really | ❌ Hard           |

after freezing, change what?
| Module                                     | Why it's important                                                                                 |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `query`, `key`, `value` (inside attention) | This is where the model learns *what to focus on*. Massive impact. Tiny modules. Perfect for LoRA. |
| `attention_output`                         | Projects that focus outward — also useful, but depends on the model.                               |
| `ffn` (feed-forward nets)                  | Sometimes targeted, especially in newer LoRA variants.                                             |
| `layer_norm`, `softmax` etc                | Rarely (if ever) LoRA'd — they don’t *learn*, they *normalize or finalize*.                        |

| Word     | What I’m looking for (Query) | What each word represents (Key) | Actual meaning to bring (Value)      |
| -------- | ---------------------------- | ------------------------------- | ------------------------------------ |
| "cat"    | Looking for cute animal info | "cat": small fuzzy hunter       | "cat": soft, sits in lap, purrs      |
| "barked" | Looking for sound info       | "dog": loud, rough              | "barked": sharp sound                |
| "Miya"   | Looking for royalty info     | "Miya": majestic goddess        | "Miya": fluff queen, lives rent free |
