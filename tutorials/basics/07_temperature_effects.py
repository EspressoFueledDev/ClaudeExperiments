from utils.claude_helper import call_haiku


print("=" * 80)
print("TEMPERATURE EFFECTS")
print("=" * 80)

creative_prompt = "Write a creative tagline for a coffee shop"

print("\nLOW TEMPERATURE (0.0) - Focused/Deterministic:")
print("-" * 80)
print(f"Response:\n{call_haiku(creative_prompt, temperature=0.0)}")

print("\n" + "=" * 80)
print("\nMEDIUM TEMPERATURE (0.7) - Balanced:")
print("-" * 80)
print(f"Response:\n{call_haiku(creative_prompt, temperature=0.7)}")

print("\n" + "=" * 80)
print("\nHIGH TEMPERATURE (1.0) - Creative/Random:")
print("-" * 80)
print(f"Response:\n{call_haiku(creative_prompt, temperature=1.0)}")
