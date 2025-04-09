def collect_feedback():
    """Collect student feedback via CLI inputs."""
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")
    rating = float(input("Enter rating (1-5): "))
    return {'name': name, 'feedback': feedback, 'rating': rating}

if __name__ == "__main__":
    print("Collecting feedback...")
    feedback_data = collect_feedback()
    print("Feedback received:", feedback_data)
