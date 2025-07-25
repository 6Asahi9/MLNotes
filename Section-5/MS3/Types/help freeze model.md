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
