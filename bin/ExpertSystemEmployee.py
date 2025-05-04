def evaluate_performance(punctuality, task_completion, teamwork):
    if punctuality >= 8 and task_completion >= 80 and teamwork >= 8:
        return "Excellent"
    elif punctuality >= 6 and task_completion >= 60 and teamwork >= 6:
        return "Good"
    elif punctuality >= 4 and task_completion >= 40 and teamwork >= 4:
        return "Average"
    else:
        return "Needs Improvement"

def main():
    print("=== Employee Performance Evaluation Expert System ===")
    
    try:
        punctuality = int(input("Rate punctuality (1 to 10): "))
        task_completion = int(input("Enter task completion percentage (0 to 100): "))
        teamwork = int(input("Rate teamwork (1 to 10): "))

        # Validate inputs
        if not (1 <= punctuality <= 10) or not (0 <= task_completion <= 100) or not (1 <= teamwork <= 10):
            print("Invalid input! Please enter values in the correct range.")
            return

        result = evaluate_performance(punctuality, task_completion, teamwork)
        print(f"\nPerformance Evaluation: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the expert system
main()
