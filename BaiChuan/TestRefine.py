import os

from langchain_community.llms.tongyi import Tongyi
from langchain_core.documents.base import Document as LangchainDocument

from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

max_token = 50000
docs = LangchainDocument(page_content="https://github.com/langchain-ai/langchain", metadata={})

openai_api_key = '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'
# Define LLM chain
# llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0, model_name="gpt-3.5-turbo-16k")
# chain = load_summarize_chain(llm, chain_type="refine")
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     chunk_size=max_token, chunk_overlap=0
# )
# split_docs = text_splitter.split_documents([docs])
# summary = chain.run(split_docs)
# print(summary)

os.environ['DASHSCOPE_API_KEY'] = "sk-205ee8abb0eb476cad4d76233a83d062"

llm = Tongyi()

chain = load_summarize_chain(llm, chain_type="refine")
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=max_token, chunk_overlap=0
)
split_docs = text_splitter.split_documents([docs])
summary = chain.run(split_docs)
print(summary)