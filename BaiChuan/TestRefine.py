import os

from langchain_community.llms.tongyi import Tongyi
from langchain_core.documents.base import Document as LangchainDocument

from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

from BaiChuanTest1 import BaiChuanTest

max_token = 50000
docs = LangchainDocument(page_content="https://www.sina.com.cn/", metadata={})



llm = BaiChuanTest()

chain = load_summarize_chain(llm, chain_type="refine")
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=max_token, chunk_overlap=0
)
split_docs = text_splitter.split_documents([docs])
summary = chain.run(split_docs)
print(summary)