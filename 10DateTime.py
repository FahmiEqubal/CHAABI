# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29

from datetime import datetime, timedelta

def calculate_previous_date(date, n):
    # Convert the input date string to a datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the previous date by subtracting timedelta of n days
    previous_date = date_obj - timedelta(days=n)

    # Convert the previous date back to a string in the desired format
    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str

date = '16-12-10'
n = 11

result = calculate_previous_date(date, n)
print(result)  # Output: 16-11-29
