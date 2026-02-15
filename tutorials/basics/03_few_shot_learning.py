from utils.claude_helper import call_haiku


print("=" * 80)
print("FEW-SHOT LEARNING")
print("=" * 80)

print("\nBAD - WITHOUT EXAMPLES:")
print("-" * 80)
no_examples = "Convert this to a professional email: 'hey can u send me the report'"
print(f"Prompt: {no_examples}")
print(f"\nResponse:\n{call_haiku(no_examples)}")

print("\n" + "=" * 80)
print("\nGOOD - WITH EXAMPLES:")
print("-" * 80)
with_examples = """Convert casual messages to professional emails following this style:

Example 1:
Casual: "hey can u review my PR?"
Professional: "Hi [Name], Could you please review my pull request when you have a moment? Thank you!"

Example 2:
Casual: "meeting at 3?"
Professional: "Hi team, Would 3 PM work for our meeting today? Please let me know. Thanks!"

Now convert this:
Casual: "hey can u send me the report"
Professional:"""

print(f"Prompt: {with_examples}")
print(f"\nResponse:\n{call_haiku(with_examples)}")
