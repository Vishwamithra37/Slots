import datetime
import re
from.config import resource_collection ,sub_resource_collection,admin_collection
import uuid

 







class Resource1:
    def __init__(self, resource_name=None, description=None, resource_unique_id=None,resource_tags=None,creator_email=None):
        self.resource_name = resource_name
        self.description = description
        self.resource_unique_id = resource_unique_id
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
    
    def validate_unique_admin_id(self, resource_unique_id): 
       
        if resource_unique_id is None:
            return False
        if len(resource_unique_id) == 6:
            return False
        existing_resource = resource_collection.find_one({"resource_unique_id": resource_unique_id})
        if existing_resource :
            return False
        
        if not bool(re.match("^[a-zA-Z0-9]+$", resource_unique_id)):
           return "Invalid admin ID format"
        else:
            return True  
    

   


    def validate_resource_tags(self, resource_tags):
       
        if resource_tags is None:
            return False
     
        if len(resource_tags) < 1:
            return False
        return True


    
        

class Resource2:
    def __init__(self, sub_resource_name=None, sub_description=None, sub_resource_id=None,resource_unique_id=None):
        self.sub_resource_name = sub_resource_name
        self.sub_description = sub_description
        self.sub_resource_id = sub_resource_id
        self.resource_unique_id =resource_unique_id
      
    def validate_sub_resource_name(self, sub_resource_name):
            if sub_resource_name is None:
               return False
            if len(sub_resource_name) < 3:
               return False
            return True
    
        
    def validate_sub_resource_id(self,sub_resource_id):
       if sub_resource_id is None:
           return False
       if len(sub_resource_id)!= 6:
           return False
       
       exisisting = sub_resource_collection.find_one({"sub_resource_id":sub_resource_id})
       if exisisting :
            return False
        
       if not bool(re.match("^[a-zA-Z0-9]+$", sub_resource_id)):
           return "Invalid admin ID format"
       else:
            return True  

      
    def validate_resource_id(self,resource_unique_id):
        res=resource_collection.find_one({"resource_id":resource_unique_id})
        if res is None:
          return "This resource does not exist."
        else:
          return "The resource you are looking for exists."
       

       
        
    def validate_sub_description(self, sub_description):
        if sub_description is None:
            return False
        if len(sub_description) < 5 and len(sub_description) > 100:
            return False
        return True
    


class Resource3:
    def __init__(self, Slot_name=None,
               Slot_description=None, 
               Status=None,StartTime=None,
               EndTime=None,MaxAdvanceDays=None,
               MaxBookings=None,Daysofweek=None,
               resource_unique_id=None,
               sub_resource_id=None,slot_unique_id=None):
        self.Slot_name=Slot_name
        self.Slot_description=Slot_description
        self.Status=Status
        self.StartTime=StartTime
        self.EndTime=EndTime
        self.MaxAdvanceDays=MaxAdvanceDays
        self.MaxBookings=MaxBookings
        self.Daysofweek=Daysofweek
        self.resource_unique_id=resource_unique_id
        self.sub_resource_id= sub_resource_id
        self.slot_unique_id=slot_unique_id



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
    def validate_resource_id(self,resource_unique_id):
        res=resource_collection.find_one({"resource_id":resource_unique_id})
        if res is None:
          return "This resource does not exist."
        else:
          return "The resource you are looking for exists."
       
    
    def validate_sub_resource_unique_id(self, sub_resource_id):
        res=sub_resource_collection.find_one({"sub_resource_id":sub_resource_id})
        if res is None:
            return "This sub-resource does not exist."
        else:
            return "The sub-resource you are looking for exists."

       
    
        
    def validate_unique_slot_id(self, unique_slot_id): 
       
        if unique_slot_id is None:
            return False
        if len(unique_slot_id)!= 6:
            return False
        existing_resource = resource_collection.find_one({"unique_slot_id": unique_slot_id})
        if existing_resource and len(existing_resource) == 6:
            return False
        
        if not bool(re.match("^[a-zA-Z0-9]+$", unique_slot_id)):
           return "Invalid admin ID format"
        else:
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







