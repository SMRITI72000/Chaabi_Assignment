from dateutil import parser
from datetime import timedelta

def calculate_new_date(date_string, n):
    date_obj = parser.parse(date_string)
    new_date_obj = date_obj - timedelta(days=n)
    new_date_string = new_date_obj.strftime('%y-%m-%d')
    return new_date_string

date = input("Enter a date (YY-MM-DD): ")
n = int(input("Enter a number of days: "))

res = calculate_new_date(date, n)
print("res",res)
