import base64

import httpx
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI


class OpenAIService:
    def __init__(self):
        self.client: OpenAI = OpenAI()

    def generate_completion(
        self,
        prompt: str,
        model_name: str = "gpt-4o-mini",
        max_tokens: int = 1000,
        image_urls: list[str] = [],
        timeout: int = 60,
    ) -> str:
        __message = [{"role": "user", "content": []}]
        __message[0]["content"].append({"type": "text", "text": prompt})

        if image_urls:
            __message[0]["content"].extend(
                [{"type": "image_url", "image_url": {"url": image_url}} for image_url in image_urls]
            )

        try:
            response = self.client.chat.completions.create(
                model=model_name, messages=__message, max_tokens=max_tokens, timeout=timeout
            )

            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"error: {e}")
            return e


class GemeniService:
    def __init__(self):
        pass

    @staticmethod
    def convert_image_url_to_b64(image_url: str):
        return base64.b64encode(httpx.get(image_url).content).decode("utf-8")

    def generate_completion(
        self,
        prompt: str,
        model_name: str = "gemini-2.0-flash",
        max_tokens: int = 1000,
        image_urls: list[str] = [],
        timeout: int = 60,
    ):
        __message = [{"type": "text", "text": prompt}]

        if image_urls:
            __message.extend(
                [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{self.convert_image_url_to_b64(image_url)}"},
                    }
                    for image_url in image_urls
                ]
            )

        __message = [HumanMessage(__message)]

        llm = ChatGoogleGenerativeAI(model=model_name, max_tokens=max_tokens, timeout=timeout)

        return llm.invoke(__message).content.strip()
