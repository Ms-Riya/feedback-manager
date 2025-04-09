# feedback_summary.py

def summarize_feedback(feedback_list):
    """
    Summarizes feedback scores.

    Args:
        feedback_list (list of dict): Each dict should have 'name' and 'score'.

    Returns:
        dict: Summary with top scorers and grade-wise count.
    """
    if not feedback_list:
        return {"top_scorers": [], "grade_counts": {}}

    sorted_feedback = sorted(feedback_list, key=lambda x: x["score"], reverse=True)
    top_scorers = sorted_feedback[:3]  # Top 3

    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for fb in feedback_list:
        score = fb["score"]
        if score >= 90:
            grade_counts["A"] += 1
        elif score >= 80:
            grade_counts["B"] += 1
        elif score >= 70:
            grade_counts["C"] += 1
        elif score >= 60:
            grade_counts["D"] += 1
        else:
            grade_counts["F"] += 1

    return {"top_scorers": top_scorers, "grade_counts": grade_counts}
