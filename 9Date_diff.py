# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.

from datetime import datetime

def check_date_difference(from_date, to_date, difference):
    from_date = datetime.strptime(from_date, '%Y-%m-%d')
    to_date = datetime.strptime(to_date, '%Y-%m-%d')

    date_difference = abs((to_date - from_date).days)

    if date_difference < difference:
        return True
    else:
        return False

# Example usage
from_date = '2021-01-01'
to_date = '2021-01-10'
difference = 7

result = check_date_difference(from_date, to_date, difference)
print(result)  # Output: True
