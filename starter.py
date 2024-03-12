import os.path

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.embeddings import resolve_embed_model


def setup_environment():
    os.environ['OPENAI_API_KEY'] = 'sk-OPEN_API_KEY'
    os.environ['LLAMA_INDEX_CACHE_DIR'] = '/llama-index/cache'

def main():
    setup_environment()
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is the 52 week high stock price of IBM ?")
    print(response)


if __name__ == "__main__":
    main()
