from utils.claude_helper import call_haiku


print("=" * 80)
print("SYSTEM PROMPTS")
print("=" * 80)

user_prompt = "Explain recursion"

print("\nBAD - WITHOUT SYSTEM PROMPT:")
print("-" * 80)
print(f"Prompt: {user_prompt}")
print(f"\nResponse:\n{call_haiku(user_prompt)}")

print("\n" + "=" * 80)
print("\nGOOD - WITH SYSTEM PROMPT:")
print("-" * 80)
system_prompt = """You are a patient coding tutor for 10-year-olds.
Use simple language and fun analogies. Keep explanations short and playful."""

print(f"System: {system_prompt}")
print(f"User: {user_prompt}")
print(f"\nResponse:\n{call_haiku(user_prompt, system_prompt=system_prompt)}")
