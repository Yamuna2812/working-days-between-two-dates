from datetime import datetime, timedelta

start = datetime.strptime(input("Start date (YYYY-MM-DD): "), "%Y-%m-%d")
end = datetime.strptime(input("End date (YYYY-MM-DD): "), "%Y-%m-%d")

working_days = 0

current = start
while current <= end:
    if current.weekday() < 5:  # Mon-Fri
        working_days += 1
    current += timedelta(days=1)

print("Working days:", working_days)