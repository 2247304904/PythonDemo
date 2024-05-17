import this

from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
import requests

api_key = ''
api_url = ''
model_name = ''

class BaiChuan(LLM):
    def __init__(self, api_url: str, api_key: str, model: str):
        api_key = api_key
        model_name = model
        api_url = api_url
        super().__init__()
        print("construct:" +model_name)

    def glm4_completion(self, message):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        payload = {
            "model": "baichuan2-13b-chat",  # 替换为实际模型名称
            "prompt": message,
            "stream": True
        }
        response = requests.post(api_url, json=payload, headers=headers, stream=True)
        return response.choices[0].message.content

    def _call(self, prompt, stop=None):
        messages = [{"role": "user", "content": prompt}]
        response = self.glm4_completion(messages)
        if stop is not None:
            response = enforce_stop_tokens(response, stop)
        return response


# 使用示例
if __name__ == "__main__":
    api_url = "https://api.auto-pai.cn/llm/gw/v1/chat/completions"
    api_key = "94aa2eac224e41d0b32f635820d9e91d"
    llm = BaiChuan(api_url, api_key, 'baichuan2-13b-chat')
    print(llm("如何学好编程？"))
