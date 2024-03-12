import os.path

from llama_index.readers.youtube_transcript import YoutubeTranscriptReader
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain


def setup_environment():
    os.environ['OPENAI_API_KEY'] = 'sk-KYE'
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
