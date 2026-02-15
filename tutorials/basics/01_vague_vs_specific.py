import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.claude_helper import call_haiku


print("=" * 80)
print("EXAMPLE 1: VAGUE vs SPECIFIC PROMPTS")
print("=" * 80)

print("\nBAD - VAGUE PROMPT:")
print("-" * 80)
vague = "Tell me about Python"
print(f"Prompt: {vague}")
print(f"\nResponse:\n{call_haiku(vague)}")

print("\n" + "=" * 80)
print("\nGOOD - SPECIFIC PROMPT:")
print("-" * 80)
specific = """Explain Python list comprehensions to a beginner programmer.
Include:
- What they are and why they're useful
- Basic syntax with 2 examples
- One common mistake to avoid
Keep it under 150 words."""

print(f"Prompt: {specific}")
print(f"\nResponse:\n{call_haiku(specific)}")
