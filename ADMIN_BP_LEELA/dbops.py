import datetime
import re
from.config import collection as dac
import uuid

 






class Resource:
    def __init__(self, name, description, slot_duration, total_slots, start_date, end_date, slot_open_time, slot_close_time, max_bookings_per_slot,admin_id):
        self.name = name
        self.description = description
        self.slot_duration = slot_duration
        self.total_slots = total_slots
        self.start_date = start_date
        self.end_date = end_date
        self.slot_open_time = slot_open_time
        self.slot_close_time = slot_close_time
        self.max_bookings_per_slot = max_bookings_per_slot
        if admin_id is None:
            self.admin_id = str(uuid.uuid4())  
        else:
            self.admin_id = admin_id

     
    def validate_name(self, name):
        if name is None:
            return False
        if len(name) < 3:
            return False
        return True
    def validate_unique_name_for_admin(self, name, admin_id):
        existing_resource = dac.find_one({"name": name, "admin_id": admin_id})
        if existing_resource:
            return False  
        return True  
    
    def validate_admin_id(self,admin_id):
        if admin_id is None:
            return False
        if len(admin_id) < 3:
            return False
        return True
    def validate_description(self, description):
        if description is None:
            return False
        if len(description) < 3:
            return False
        return True

    def validate_slot_duration(self, slot_duration):
        if slot_duration is None:
            return False
        if slot_duration < 1:
            return False
        return True
       
    

    def validate_total_slots(self, total_slots):
        if total_slots is None:
            return False
        if total_slots < 1:
            return False
        return True

    def validate_start_date(self, start_date):
        if start_date is None:
            return False
        if not self.validate_date(start_date):
            return False
        return True

    def validate_end_date(self, end_date):
        if end_date is None:
            return False
        if not self.validate_date(end_date):
            return False
        return True

    def validate_slot_open_time(self, slot_open_time):
        if slot_open_time is None:
            return False
        if not self.validate_time(slot_open_time):
            return False
        return True

    def validate_slot_close_time(self, slot_close_time):
        if slot_close_time is None:
            return False
        if not self.validate_time(slot_close_time):
            return False
        return True

    def validate_max_bookings_per_slot(self, max_bookings_per_slot):
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
    
    def delete_permissions():
        pass
        return True
    def update_permissions():
        return True
def permission():
   
    def validate(self):
        return (
            self.validate_name(self.name) and
            self.validate_unique_name_for_admin(self.name, self.admin_id)and
            self.validate_description(self.description) and
            self.validate_slot_duration(self.slot_duration) and
            self.validate_total_slots(self.total_slots) and
            self.validate_start_date(self.start_date) and
            self.validate_end_date(self.end_date) and
            self.validate_slot_open_time(self.slot_open_time) and
            self.validate_slot_close_time(self.slot_close_time) and
            self.validate_max_bookings_per_slot(self.max_bookings_per_slot)
        )
    
def to_dict(self):
    return {
        "name": self.name,
        "description": self.description,
        "slot_duration": self.slot_duration,
        "total_slots": self.total_slots,
        "start_date": self.start_date,
        "end_date": self.end_date,
        "slot_open_time": self.slot_open_time,
        "slot_close_time": self.slot_close_time,
        "max_bookings_per_slot": self.max_bookings_per_slot,
        "admin_id": self.admin_id  

 
   }




