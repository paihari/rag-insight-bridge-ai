# Llama Index RAG
Llama Index Rag Use cases, for various data source sets

LlamaIndex is a data framework for LLM-based applications which benefit from context augmentation. Such LLM systems have been termed as RAG systems, standing for “Retrieval-Augmented Generation”. LlamaIndex provides the essential abstractions to more easily ingest, structure, and access private or domain-specific data in order to inject these safely and reliably into LLMs for more accurate text generation. 



## Why RAG
LLMs are pre-trained on a great deal of data, they are not trained on data which it did not have access, which may be private or specific to the problem you’re trying to solve. It’s behind APIs, in SQL databases, or trapped in PDFs and slide decks.

We can choose to train the LLMs with the contextual data, but Training a LLM is expensive, also it’s hard to update a LLM with latest information.

Instead of fine-tuning, one can use a context augmentation pattern called Retrieval-Augmented Generation (RAG) to obtain more accurate text generation relevant to your specific data. RAG involves the following high level steps:

Retrieve information from your data sources first,

Add it to your question as context, and

Ask the LLM to answer based on the enriched prompt.

## What is here

This repository is continous and contains application of Llama Index on some obvious use cases

## What do you need
1. **OPEN API KEY**: LlamaIndex uses OpenAI’s gpt-3.5-turbo by default. Make sure your API key is available
https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key

1. **Python Installation**: Stable Python installation

## Data Source: Local Folder
```
python3 starter.py

```

starter.py

## Data Source: Youtube Transcript
```
python3 youtube.py

```



