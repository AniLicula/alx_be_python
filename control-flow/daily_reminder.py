# daily_reminder.py

# Prompt the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate inputs (basic loop example)
while priority not in ("high", "medium", "low"):
    print("Please enter a valid priority: high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ("yes", "no"):
    print("Please answer 'yes' or 'no'.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match-case (Python 3.10+)
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Append message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Output the customized reminder
print("\nReminder:", message)
