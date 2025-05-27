task = input("What task do you want to be reminded of? ").lower()
priority = input("What is the priority of this task? (high/medium/low) ").lower()
time_bound = input("Is this task time-bound? (yes/no) ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Note:'{task}' is a high priority task that requires immediate attention today!.")
    case "medium":
        if time_bound == "yes":
            print(f"Note:'{task}' is a medium priority task that should be completed today.")
    case "low":
        if time_bound == "no":
            print(f"Note:'{task}' is a low priority task. Consider completing it when you have free time..")