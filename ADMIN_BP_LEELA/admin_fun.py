import datetime
import re
# Input validation function for date
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        False

# Input validation function for time
def validate_time(time_str):
    if re.match(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', time_str):
        return True
    else:
        False


    

