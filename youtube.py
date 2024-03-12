import os.path

from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.indices.postprocessor import SimilarityPostprocessor
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.embeddings import resolve_embed_model
# from llama_hub.youtube_transcript import YoutubeTranscriptReader
from llama_index.readers.youtube_transcript import YoutubeTranscriptReader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain


def setup_environment():
    os.environ['OPENAI_API_KEY'] = 'sk-OPEN_API_KEY'
    os.environ['LLAMA_INDEX_CACHE_DIR'] = '/llama-index/cache'

def main():
    setup_environment()
    loader = YoutubeTranscriptReader()

    documents = loader.load_data(
        ytlinks=["https://www.youtube.com/watch?v=FdI4OHumQh4"]
    )


    langchain_documents = [d.to_langchain_format() for d in documents]
    llm = OpenAI(temperature=0)
    qa_chain = load_qa_chain(llm)
    question="What is the IBM price ?"
    answer = qa_chain.run(input_documents=langchain_documents, question=question)

    print(answer)


if __name__ == "__main__":
    main()
