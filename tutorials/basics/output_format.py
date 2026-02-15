from utils.claude_helper import call_haiku


print("=" * 80)
print("SPECIFY OUTPUT FORMAT")
print("=" * 80)

print("\nBAD - NO FORMAT SPECIFIED:")
print("-" * 80)
no_format = "Give me 3 ideas for a todo app feature"
print(f"Prompt: {no_format}")
print(f"\nResponse:\n{call_haiku(no_format)}")

print("\n" + "=" * 80)
print("\nGOOD - FORMAT SPECIFIED:")
print("-" * 80)
with_format = """Give me 3 ideas for a todo app feature.

Format your response as JSON:
{
  "features": [
    {"name": "feature name", "description": "one sentence", "difficulty": "easy/medium/hard"},
    ...
  ]
}"""

print(f"Prompt: {with_format}")
print(f"\nResponse:\n{call_haiku(with_format)}")
