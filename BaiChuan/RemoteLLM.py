from langchain_core.language_models import LLM
import requests
from typing import Optional, List, Generator, Dict, Any
from langchain_core.outputs import Generation, LLMResult, GenerationChunk
from langchain_core.callbacks import CallbackManagerForLLMRun, AsyncCallbackManagerForLLMRun

api_url = ''
api_key = ''


class RemoteLLM(LLM):
    def __init__(self, api_url: str, api_key: str):
        api_url = api_url
        api_key = api_key
        super().__init__()

    def _post_request(self, payload: Dict[str, Any], stream: bool) -> requests.Response:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.post(api_url, json=payload, headers=headers, stream=stream)
        response.raise_for_status()
        return response

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        payload = {
            "model": "baichuan2-13b-chat",  # 替换为实际模型名称
            "prompt": prompt,
            "temperature": kwargs.get('temperature', 0.7),
            "max_tokens": kwargs.get('max_tokens', 150),
            "stop": stop,
            "stream": False
        }
        response = self._post_request(payload, stream=False)
        return response.json()['choices'][0]['text']

    def _stream(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> Generator[GenerationChunk, None, None]:
        payload = {
            "model": "baichuan2-13b-chat",  # 替换为实际模型名称
            "prompt": prompt,
            "temperature": kwargs.get('temperature', 0.7),
            "max_tokens": kwargs.get('max_tokens', 150),
            "stop": stop,
            "stream": True
        }
        response = self._post_request(payload, stream=True)
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                    chunk = GenerationChunk(text=decoded_line[len("data: "):])
                    yield chunk

    async def _acall(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        return await super()._acall(prompt, stop, run_manager, **kwargs)

    async def _astream(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> Generator[GenerationChunk, None, None]:
        async for chunk in super()._astream(prompt, stop, run_manager, **kwargs):
            yield chunk

    @property
    def _llm_type(self) -> str:
        return "remote_llm"

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {
            "api_url": api_url,
            "model_name": "baichuan2-13b-chat"  # 替换为实际模型名称
        }


# 示例用法
def main():
    api_url = "https://api.auto-pai.cn/llm/gw/v1/chat/completions"
    api_key = "94aa2eac224e41d0b32f635820d9e91d"

    llm = RemoteLLM(api_url, api_key)

    # 非流式请求示例
    prompt = "Translate the following English text to French: 'Hello, how are you?'"
    response = llm._call(prompt, stream=False)
    print(response)

    # 流式请求示例
    for response in llm._stream(prompt, stream=True):
        print(response.text)


if __name__ == "__main__":
    main()
