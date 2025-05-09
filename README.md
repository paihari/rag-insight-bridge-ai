# 📚 InsightBridge AI

> *Context-aware answers from your internal knowledge base* 

**InsightBridge AI** uses Retrieval-Augmented Generation (RAG) techniques with LlamaIndex and OpenAI to turn local documents and YouTube transcripts into intelligent, conversational answers—without the need to retrain your model.

---

## 🔍 What is Retrieval-Augmented Generation (RAG)?

LLMs are powerful but lack real-time or domain-specific knowledge. RAG bridges this gap by:
1. **Retrieving** relevant context from your documents or media
2. **Augmenting** the user's question with this context
3. **Generating** a high-quality, accurate answer with an LLM

---

## 🚀 Use Cases

### 🗂️ Use Case 1: Local Knowledge Retrieval

Turn your `.txt` documents into a smart, searchable knowledge base.

#### ✅ What It Does

- Scans `.txt` files in `./data`
- Indexes them using LlamaIndex
- Enables natural language Q&A with OpenAI GPT
- Returns answers grounded in your content

#### ▶️ Example Run

```bash
python3 starter.py
```

#### 👤 User Input:
```
What is the key message in Paul Graham's essay?
```

#### 💬 System Output:
```
Paul Graham believes great startups solve real problems founders care about. He suggests starting with something small but useful and growing it organically.
```

---

### 📺 Use Case 2: YouTube Transcript Retrieval

Ask questions based on the transcript of any public YouTube video.

#### ✅ What It Does

- Accepts a YouTube video ID
- Downloads the transcript using `youtube-transcript-api`
- Indexes and queries the content using LLMs

#### ▶️ Example Run

```bash
python3 youtube.py
```

#### 👤 User Input:
```
YouTube ID: abc123xyz
What are IBM's AI priorities discussed in the video?
```

#### 💬 System Output:
```
IBM focuses on responsible AI, hybrid cloud integration, and domain-specific automation using trustworthy models.
```

---

## 📁 Folder Structure

```
llama-index-rag/
├── data/                      # Local source documents
├── starter.py                 # Local file RAG demo
├── youtube.py                 # YouTube RAG demo
├── README.md                  # This file
└── requirements.txt           # Python dependencies
```

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-org/insightbridge-ai.git
cd insightbridge-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key

```bash
export OPENAI_API_KEY=your-key-here
```

---

## 📌 Requirements

- Python 3.7+
- OpenAI API key
- Internet access (for YouTube use case)

---
