# How to Run Python Scripts in This Project

## The Right Way: Use -m flag

Always run from the project root using the `-m` flag:

```bash
# From project root (/Users/vaibhav/Documents/DevProjects/Experiments/ClaudeExperiments/)
python -m tutorials.01_basics.01_vague_vs_specific
python -m tutorials.01_basics.03_few_shot_learning
python -m utils.claude_helper
```

## Why?

### The `-m` flag:
- Treats the script as a module
- Adds the current directory (project root) to `sys.path`
- Makes all imports work properly

### Without `-m`:
```bash
python tutorials/01_basics/01_vague_vs_specific.py  # WRONG
```
This adds `tutorials/01_basics/` to `sys.path`, so Python can't find `utils/`

## What __init__.py Does

`__init__.py` makes a directory a **package**, but doesn't add it to Python's search path.

```
utils/
  __init__.py          # Makes 'utils' a package
  claude_helper.py     # Can be imported as: from utils.claude_helper import ...
```

But Python still needs to know WHERE to find the `utils` package. That's what `-m` solves.

## Quick Reference

```bash
# Always be in project root first
cd /Users/vaibhav/Documents/DevProjects/Experiments/ClaudeExperiments

# Run any script
python -m tutorials.01_basics.01_vague_vs_specific
python -m tutorials.01_basics.04_system_prompts
python -m experiments.my_test_script

# The pattern: replace / with . and remove .py
# tutorials/01_basics/01_vague_vs_specific.py
# becomes: tutorials.01_basics.01_vague_vs_specific
```
