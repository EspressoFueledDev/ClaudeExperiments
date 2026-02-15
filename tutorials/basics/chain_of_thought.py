from utils.claude_helper import call_haiku


print("=" * 80)
print("CHAIN OF THOUGHT PROMPTING")
print("=" * 80)

print("\nBAD - DIRECT ANSWER:")
print("-" * 80)
direct = "If a store has 15 apples and sells 60% of them, then gets a new shipment of 8 apples, how many do they have?"
print(f"Prompt: {direct}")
print(f"\nResponse:\n{call_haiku(direct)}")

print("\n" + "=" * 80)
print("\nGOOD - CHAIN OF THOUGHT:")
print("-" * 80)
cot = """If a store has 15 apples and sells 60% of them, then gets a new shipment of 8 apples, how many do they have?

Think through this step-by-step:
1. First, calculate how many were sold
2. Then, subtract from the original amount
3. Finally, add the new shipment"""

print(f"Prompt: {cot}")
print(f"\nResponse:\n{call_haiku(cot)}")
