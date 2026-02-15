import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    temperature=0.3,  # more focused/deterministic
    messages=[
        {"role": "user", "content": "Hi, what are summers like in San Francisco?"}
    ]
)

print(response.content[0].text)

