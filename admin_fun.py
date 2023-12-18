from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client["slotzz"]
dac = db["admin"]

class Admin_Finder:
 #admin related fucntions
 def admin_finder(phno):
        """this fn finds the userdetails from the data base by taking in phno as parameter"""
        filter = {"contact":phno}
        print(filter)
        admin_details = dac.find_one(filter = filter)
        return admin_details
 
 def emailfinder(emailid):
         """this fn needs to find the email from database usersdata and return true if present else false """
         result={"email":emailid}
         finder = dac.find_one(result)
         return finder
 def get_admin_data(f_name,l_name,emailid,phno):
        """this fn inserts  new data  into our database,return if true else false"""
        admindata={"firstname":f_name,"lastname":l_name,"email":emailid,"contact":phno}
        admins=dac.insert_one(admindata)
        if admins.acknowledged:
            return True
        else:
            return False