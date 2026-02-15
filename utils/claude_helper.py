import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


def get_client():
    return anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def call_haiku(prompt, model="claude-haiku-4-5-20251001", max_tokens=1024, temperature=0.3, system_prompt=None):
    client = get_client()

    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}]
    }

    if system_prompt:
        kwargs["system"] = system_prompt

    response = client.messages.create(**kwargs)
    return response.content[0].text


def call_sonnet(messages, model="claude-sonnet-4-5-20250514", max_tokens=1024, temperature=0.3, system_prompt=None):
    client = get_client()

    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": messages
    }

    if system_prompt:
        kwargs["system"] = system_prompt

    response = client.messages.create(**kwargs)
    return response.content[0].text


if __name__ == "__main__":
    response = call_haiku("Say hello!")
    print(response)
