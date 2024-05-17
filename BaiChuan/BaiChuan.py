import requests
from typing import Generator, Optional, Dict, Any

from langchain_core.language_models import LLM


class BaiChuan(LLM):
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key

    def _post_request(self, payload: Dict[str, Any]) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        response.raise_for_status()  # Ensure we notice bad responses
        return response

    def generate(self, prompt: str, stream: bool = False) -> Generator[str, None, None]:
        payload = {
            "model": "baichuan2-13b-chat",  # Replace with the appropriate model name
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 150,
            "stream": stream
        }

        if stream:
            response = self._post_request(payload)
            for line in response.iter_lines():
                if line:
                    yield line.decode('utf-8')
        else:
            response = self._post_request(payload)
            yield response.json()


# Usage example
def main():
    api_url = "https://api.auto-pai.cn/llm/gw/v1/chat/completions"
    api_key = "94aa2eac224e41d0b32f635820d9e91d"

    llm = BaiChuan(api_url, api_key)

    # Non-streaming example
    prompt = "Translate the following English text to French: 'Hello, how are you?'"
    for response in llm.generate(prompt, stream=False):
        print(response)

    # Streaming example
    for response in llm.generate(prompt, stream=True):
        print(response)


if __name__ == "__main__":
    main()