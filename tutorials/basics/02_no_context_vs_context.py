from utils.claude_helper import call_haiku


print("=" * 80)
print("NO CONTEXT vs WITH CONTEXT")
print("=" * 80)

print("\nBAD - NO CONTEXT:")
print("-" * 80)
no_context = "Is this code good?"
print(f"Prompt: {no_context}")
print(f"\nResponse:\n{call_haiku(no_context)}")

print("\n" + "=" * 80)
print("\nGOOD - WITH CONTEXT:")
print("-" * 80)
with_context = """I'm building a REST API for a todo app. Here's my error handling:

```python
def get_todo(todo_id):
    todo = db.get(todo_id)
    return todo
```

Is this code good? What's missing?"""

print(f"Prompt: {with_context}")
print(f"\nResponse:\n{call_haiku(with_context)}")
