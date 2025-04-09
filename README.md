# Student Feedback Manager

## Version 1.0.0

### Features
- Collect student feedback via CLI
- Calculate average ratings

### Usage
```bash
# Collect feedback
python feedback_entry.py

# Run calculations
python score_calculator.py

### Feedback Summary

The `summarize_feedback` function analyzes feedback and provides:
- Top 3 scorers
- Grade-wise distribution (A, B, C, D, F)

Usage:

```python
from feedback_summary import summarize_feedback

feedback = [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 88}]
summary = summarize_feedback(feedback)
---
