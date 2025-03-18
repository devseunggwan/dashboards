from typing import Optional

from openai import OpenAI


class OpenAIService:
    def __init__(self, api_key: Optional[str] = None):
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
