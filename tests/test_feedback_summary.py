# tests/test_feedback_summary.py

from feedback_summary import summarize_feedback

def test_summarize_feedback():
    feedback = [
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 88},
        {"name": "Charlie", "score": 92},
        {"name": "David", "score": 67},
        {"name": "Eva", "score": 45}
    ]
    
    summary = summarize_feedback(feedback)

    assert summary["grade_counts"]["A"] == 2
    assert summary["grade_counts"]["B"] == 1
    assert summary["grade_counts"]["D"] == 1
    assert summary["grade_counts"]["F"] == 1
    assert summary["top_scorers"][0]["name"] == "Alice"
