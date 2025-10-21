Here are the common **retriever types** you’ll see in LangChain / RAG work:

---

### **1) Basic Vector Store Retriever**

* Most common
* Uses embeddings + similarity search to pull top-k chunks
* Example: `pinecone.as_retriever()`, `faiss.as_retriever()`

---

### **2) Multi-Query Retriever**

* Expands the question into multiple alternative queries using an LLM
* Runs each query against the vector store and merges results
* Helps when user query is vague, phrased unusually, or incomplete
  *(“multi-angles” to retrieve better)*

---

### **3) Self-Query Retriever**

* Uses LLM to rewrite the question into **a structured filter** + query
* Example: “papers after 2022 about transformers” → converts to

  * query: “transformers”
  * filter: `year > 2022`
* Needs a metadata-aware vector store

---

### **4) Contextual Compression Retriever**

* First retrieves a broad set, then compresses/filters using LLM to remove irrelevant chunks
* Useful when stored docs are large/noisy

---

### **5) Hybrid Retriever**

* Combines **vector similarity** + **keyword search (BM25)** together
* Good when content has important keywords not captured by embeddings

---

### **6) Ensemble (Reranking) Retriever**

* Grabs candidates with a fast retriever (BM25/Vector)
* Reranks with cross-encoder or LLM scoring to return best final list

---

### **7) Parent-Document Retriever**

* Splits documents into small chunks, but returns a bigger “parent” section containing those chunks for more context
* Helps reduce “hallucination due to over-chunking”

---

### **8) Time-Weighted / Memory-Based Retriever**

* Used in chat/agent memory systems
* Prefers more recent or more “important” messages instead of pure similarity

---

If you want I can:

1. Explain any one of them with an example, OR
2. Tell you when to use which, OR
3. Show sample code for one (your pick)

Tell me what you want next:
**A) deeper explanation**
**B) use-case comparison**
**C) code sample**
— and which retriever to start with.
