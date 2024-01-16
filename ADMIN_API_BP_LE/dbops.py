import datetime
import re
from . config import collection  as dac


class validation:
# Input validation function for date
 def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Input validation function for time
 def validate_time(time_str):
    if re.match(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', time_str):
        return True
    else:
        return False


 def create_slot(slot_name, resource,combined_datetime,number_of_slots):
    # Create the slot document with date, time, and number_of_slots
  slot_data = {
    "slot_name": slot_name,
    "resource": resource,
    "datetime": combined_datetime,
    "number_of_slots": number_of_slots
}




  result = dac.insert_one(slot_data)










    

