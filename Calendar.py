# Print calender in python
import calendar as cd

year = int(input("Enter the year :"))
month = int(input("Enter the month (1-12) :"))

cal = cd.month(year, month)

# Display the calender
print(cal)
