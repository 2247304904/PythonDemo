from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader

from BaiChuanTest1 import BaiChuan

# 加载网络文档
loader = WebBaseLoader("https://github.com/langchain-ai/langchain")
docs = loader.load()


# 配置LLM，例如使用OpenAI的模型
llm = BaiChuan()
chain = load_summarize_chain(llm, chain_type="stuff")
# 执行文档总结
summary = chain.run(docs)
print(summary)
