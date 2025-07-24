# daily_reminder.py

def main():
    # Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate priority
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("❌ Invalid priority. Please enter high, medium, or low.")
            return

    # Add time sensitivity message
    if time_bound == "yes":
        full_message = f"⏰ Reminder: {base_message} that requires immediate attention today!"
    else:
        full_message = f"📌 Note: {base_message}. Consider completing it when you have free time."

    # Display the final customized reminder
    print("\n" + full_message)


# Run the main function
if __name__ == "__main__":
    main()
