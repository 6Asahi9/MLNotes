Ahhh, darling 😏💖 this is a **classic RAG (retrieval-augmented generation) setup for PDFs**, let’s go step by step so it all clicks.

---

### **1️⃣ Function purpose**

```python
def process_document(document_path):
```

* Takes the path of a PDF and prepares it so the LLM (Miya) can **answer questions about it efficiently**.
* Sets up a **conversation retrieval chain** (QA system) using:

  * PDF → text chunks → embeddings → Chroma → retriever → LLM

---

### **2️⃣ Loading the PDF**

```python
loader = PyPDFLoader(document_path)
documents = loader.load()
```

* **PyPDFLoader** reads the PDF file
* `documents` is now a **list of text objects**, each representing a page or portion of the PDF
* Logging shows how many documents were loaded

---

### **3️⃣ Splitting the document into chunks**

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
texts = text_splitter.split_documents(documents)
```

* PDFs can be **huge**, so we split them into smaller chunks:

  * `chunk_size=1024` → \~1024 characters per chunk
  * `chunk_overlap=64` → small overlap so context isn’t lost between chunks

* `texts` is now a **list of manageable text pieces**, ready for embedding

💡 Analogy with Miya:

* Imagine giving her a huge tuna manual.
* You **cut it into small pages**, so she can quickly read only the relevant pages when asked 😸

---

### **4️⃣ Creating the embeddings vector store**

```python
db = Chroma.from_documents(texts, embedding=embeddings)
```

* Converts each text chunk → **embedding vector** (via HuggingFace embeddings from earlier)

* Stores vectors in **Chroma** so we can later **search for relevant chunks quickly**

* Optional: log available collections

---

### **5️⃣ Setting up the Retrieval QA chain**

```python
conversation_retrieval_chain = RetrievalQA.from_chain_type(
    llm=llm_hub,
    chain_type="stuff",
    retriever=db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25}),
    return_source_documents=False,
    input_key="question"
)
```

* **`llm_hub`** = Miya (your LLM)
* **`db.as_retriever()`** = fetches top relevant chunks from Chroma based on query embedding
* `search_type="mmr"` → uses **Maximal Marginal Relevance**, which balances **relevance** vs **diversity** in retrieved chunks
* `k=6` → retrieve top 6 chunks per query
* **QA chain**: the LLM reads only the retrieved chunks and generates an answer

💡 Analogy with Miya:

* User: “Where’s the tuna info?”
* Chroma: “Here are the 6 most relevant pages from the manual”
* Miya: reads the 6 chunks → gives **concise answer** without reading the whole PDF

---

### **6️⃣ TL;DR flow**

```
PDF file → PyPDFLoader → documents
      → RecursiveCharacterTextSplitter → text chunks
      → embeddings → Chroma vector DB
      → retriever → top N relevant chunks
      → LLM (Miya) → generates answer
```

---

### **Why the LLM needs embeddings here**

* LLM **cannot efficiently search** large PDFs or documents itself
* Embeddings + Chroma → **fast retrieval of only relevant chunks**
* LLM only sees **text**; it doesn’t need to match embedding architecture
* Without embeddings, Miya would have to tokenize and read the **entire PDF every time**, which is **slow and memory-heavy**

---

```python 
def process_prompt(prompt):
    global conversation_retrieval_chain
    global chat_history
    logger.info("Processing prompt: %s", prompt)
    # Query the model using the new .invoke() method
    output = conversation_retrieval_chain.invoke({"question": prompt, "chat_history": chat_history})
    answer = output["result"]
    logger.debug("Model response: %s", answer)
    # Update the chat history
    # TODO: Append the prompt and the bot's response to the chat history using chat_history.append and pass `prompt` `answer` as arguments
    # --> write your code here <--	
    
    logger.debug("Chat history updated. Total exchanges: %d", len(chat_history))
    # Return the model's response
    return answer
    
```
