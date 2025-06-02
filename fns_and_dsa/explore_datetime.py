
from datetime import datetime, timedelta
def display_current_datetime():
    """Display the current date and time."""
    current_date= datetime.now()
    
    
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    
def calculate_future_date():
    """Calculate the date a certain number of days in the future."""
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    if number_of_days < 0:
        print("Please enter a non-negative number of days.")
        return
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    
display_current_datetime()

calculate_future_date()