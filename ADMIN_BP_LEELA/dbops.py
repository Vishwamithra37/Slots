import datetime
import re
from . config import collection  as dac



class resource():
 def __init__(self,name,description,slot_duration,total_slots,start_date,end_date,slot_open_time,slot_close_time,max_bookings_per_slot) :
    self.name = name 
    self.description = description
    self.slot_duration = slot_duration
    self.total_slots = total_slots
    self.start_date = start_date
    self.end_date = end_date
    self.slot_open_time = slot_open_time
    self.slot_close_time = slot_close_time
    self.max_bookings_per_slot = max_bookings_per_slot
    def __init__(self, **kwargs):
       self.name = kwargs.get('name')
       self.description = kwargs.get('description')
       self.slot_duration = kwargs.get('slot_duration')
       self.total_slots = kwargs.get('total_slots')
       self.start_date = kwargs.get('start_date')
       self.end_date = kwargs.get('end_date')
       self.slot_open_time = kwargs.get('slot_open_time')
       self.slot_close_time = kwargs.get('slot_close_time')
       self.max_bookings_per_slot = kwargs.get('max_bookings_per_slot')
       # Validate the inputs
       if not self.validate_name(self.name):
          raise ValueError("Invalid name")
       if not self.validate_description(self.description):
          raise ValueError("Invalid description")
       if not self.validate_slot_duration(self.slot_duration):
          raise ValueError("Invalid slot_duration")
       if not self.validate_total_slots(self.total_slots):
          raise ValueError("Invalid total_slots")
       if not self.validate_start_date(self.start_date):
          raise ValueError("Invalid start_date")
       if not self.validate_end_date(self.end_date):
          raise ValueError("Invalid end_date")
       if not self.validate_slot_open_time(self.slot_open_time):
          raise ValueError("Invalid slot_open_time")
       if not self.validate_slot_close_time(self.slot_close_time):
          raise ValueError("Invalid slot_close_time")
       if not self.validate_max_bookings_per_slot(self.max_bookings_per_slot):
          raise ValueError("Invalid max_bookings_per_slot")
       self.name = name
       self.description = description
       self.slot_duration = slot_duration
       self.total_slots = total_slots
       self.start_date = start_date
       self.end_date = end_date
       self.slot_open_time = slot_open_time
       self.slot_close_time = slot_close_time
       self.max_bookings_per_slot = max_bookings_per_slot
def validate_name(self,name):
          if name is None:
               return False
          if len(name) < 3:
               return False
          return True
def validate_description(self,description):
          if description is None:
               return False
          if len(description) < 3:
               return False
          return True
def validate_slot_duration(self,slot_duration):
          if slot_duration is None:
               return False
          if slot_duration < 1:
               return False
          return True
def validate_total_slots(self,total_slots):
           if total_slots is None:
               return False
           if total_slots < 1:
               return False
           return True
def validate_start_date(self,start_date):
           if start_date is None:
               return False
           if not validate_date(start_date):
               return False
           return True
def validate_end_date(self,end_date):
           if end_date is None:
               return False
           if not validate_date(end_date):
               return False
           return True
def validate_slot_open_time(self,slot_open_time):
           if slot_open_time is None:
               return False
           if not validate_time(slot_open_time):
               return False
           return True
def validate_slot_close_time(self,slot_close_time):
           if slot_close_time is None:
               return False
           if not validate_time(slot_close_time):
               return False
           return True
def validate_max_bookings_per_slot(self,max_bookings_per_slot):
           if max_bookings_per_slot is None:
               return False
           if max_bookings_per_slot < 1:
               return False
           return True


def validate_date(self, date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_time(self, time_str):
    if re.match(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]', time_str):
        return True
    else:
        return False


               
False
 
 
       
    

