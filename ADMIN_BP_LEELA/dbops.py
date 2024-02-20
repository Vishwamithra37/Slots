import datetime
import re
from.config import resource_collection ,sub_resource_collection,admin_collection
import uuid

 







class Resource1:
    def __init__(self, resource_name=None, description=None, admin_id=None,resource_tags=None,creator_email=None):
        self.resource_name = resource_name
        self.description = description
        self.admin_id = admin_id
        self.resource_tags = resource_tags
        self.creator_email = creator_email

    def validate_resource_name(self, resource_name):
            if resource_name is None:
               return False
            if len(resource_name) < 3:
               return False
            return True
    
    def validate_description(self, description):
        if description is None:
            return False
        if len(description) < 5 and len(description) > 100:
            return False
        return True
    
    def validate_unique_admin_id(self, admin_id):
        existing_admin_id= resource_collection.find_one({"admin_id": admin_id})
        if existing_admin_id:
            return False
        if len(admin_id) < 5:
            return False
        else:
            return True
       


    def validate_unique_name_for_admin(self, resource_name, admin_id):
        existing_resource = resource_collection.find_one({"resource_name": resource_name, "admin_id": admin_id})
        if existing_resource:
            return False  
        return True  
    def add_tag(self, resource_tags):
        self.resource_tags.append(resource_tags)

    def remove_tag(self, resource_tags):
        if resource_tags in self.resource_tags:
            self.resource_tags.remove(resource_tags)


    def validate_resource_tags(self, resource_tags):
        # Checking for empty tags field
        if resource_tags is None:
            return False
        # Checking for invalid tags
        if len(resource_tags) < 3:
            return False
        return True


    def validate_creators_mail(self,creator_email):
        if creator_email is None:
            return False
        if len(creator_email) < 3:
            return False
        return True
        
        

class Resource2:
    def __init__(self, sub_resource_name=None, sub_description=None, sub_resource_id=None):
        self.sub_resource_name = sub_resource_name
        self.sub_description = sub_description
        self.sub_resource_id = sub_resource_id
      
    def validate_sub_resource_name(self, sub_resource_name):
            if sub_resource_name is None:
               return False
            if len(sub_resource_name) < 3:
               return False
            return True
    
        
    def validate_sub_resource_id(self,sub_resource_id):
        if sub_resource_id is None:
            return False
        if len(sub_resource_id) < 3:
            return False
        return True
    def validate_sub_description(self, sub_description):
        if sub_description is None:
            return False
        if len(sub_description) < 5 and len(sub_description) > 100:
            return False
        return True
    


class Resource3:
    def _init_(self, Slot_name=None,
               Slot_description=None, 
               Status=None,StartTime=None,
               EndTime=None,MaxAdvanceDays=None,
               MaxBookings=None,Daysofweek=None,
               Resource_UniqueID=None,
               SubResource_UniqueID=None,UniqueID=None):
        self.Slot_name=Slot_name
        self.Slot_description=Slot_description
        self.Status=Status
        self.StartTime=StartTime
        self.EndTime=EndTime
        self.MaxAdvanceDays=MaxAdvanceDays
        self.MaxBookings=MaxBookings
        self.Daysofweek=Daysofweek
        self.Resource_UniqueID=Resource_UniqueID
        self.SubResource_UniqueID=SubResource_UniqueID
        self.UniqueID=UniqueID



    def validate_slot_name(self, slot_name):
        if slot_name is None:
            return False
        if len(slot_name) < 3:
            return False
        return True
    def validate_slot_description(self, slot_description):
        if slot_description is None:
            return False
        if len(slot_description) < 5 and len(slot_description) > 100:
            return False
        return True
    def validate_status(self, Status):
        if Status is None:
            return False
        if len(Status) < 3:
            return False
        return True
    def validate_start_time(self, Start_time):
        if Start_time is None:
            return False
        if not self.validate_time(Start_time):
            return False
        return True
    def validate_end_time(self, End_time):
        if End_time is None:
            return False
        if not self.validate_time(End_time):
            return False
        return True
    def validate_max_advance_days(self, Max_advance_days):
        if Max_advance_days is None:
            return False
        if Max_advance_days < 1:
            return False
        return True
    def validate_max_bookings(self, Max_bookings):
        if Max_bookings is None:
            return False
        if Max_bookings < 1:
            return False
        return True
    def validate_days_of_week(self, Days_of_week):
        if Days_of_week is None:
            return False
        if len(Days_of_week) < 1:
            return False
        return True
    def validate_resource_unique_id(self, Resource_UniqueID):
        if Resource_UniqueID is None:
            return False
        if len(Resource_UniqueID) < 3:
            return False
        return True
    def validate_sub_resource_unique_id(self, Sub_Resource_UniqueID):
        if Sub_Resource_UniqueID is None:
            return False
        if len(Sub_Resource_UniqueID) < 3:
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
    
    
   
def permissions_data():
    email = "test@example.com"
    return {
        "email": email,
        "permissions": [
            "create_resource",
            "update_resource",
            "delete_resource"]
    }







