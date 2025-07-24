#!/usr/bin/env python3
"""
Script to explore Python's datetime module
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # return for reuse in future date calculation

def calculate_future_date(current_date):
    """
    Calculates and displays the date after a user-specified number of days.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for number of days.")

if __name__ == "__main__":
    # Part 1
    now = display_current_datetime()

    # Part 2
    calculate_future_date(now)
