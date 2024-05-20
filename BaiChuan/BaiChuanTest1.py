from typing import Optional, List, Mapping, Any

import requests
from langchain_core.language_models import LLM



#示例原文 https://blog.csdn.net/2301_78285120/article/details/135302776

class BaiChuanTest(LLM):
    api_url = "XXX/v1/chat/completions"
    api_key = "XXX"
    model: str = "baichuan2-13b-chat"

    # def __init__(self, model: str):
    #     self.model = model
    #     super().__init__()

    def _llm_type(self) -> str:
        return self.model

    def _call(self, prompt: str,
              stop: Optional[List[str]] = None) -> str:
        # 启动关键的函数
        {''}
        content = self._post(prompt)
        # content = "这是一个测试"
        return content

    def _post(self, prompt: str) -> str:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer XXXX'
        }
        data = {
            "model": self.model,  # 替换为实际模型名称
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        print("data", data)
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()

        result = response.json()
        text = result["choices"][0]["message"]["content"]
        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"endpoint": self.api_url, "model": self.model}


if __name__ == '__main__':
    llm = BaiChuanTest('spark')
    print(llm("你好"))
