def calculate_average(scores: list[float]) -> float:
    """Calculate average score from list of ratings."""
    return sum(scores)/len(scores) if scores else 0.0

if __name__ == "__main__":
    test_scores = [4.5, 3.8, 4.0]
    print(f"Average score: {calculate_average(test_scores):.1f}")
