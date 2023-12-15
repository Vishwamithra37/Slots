from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client['Slotzz']  
dac = db['Account_holders'] 
class User_Finder:
    def emailfinder(emailid):
         """this fn needs to find the email from database  and return true if present else false """
         result={"email":emailid}
         finder = dac.find_one(result)
         return finder
    def get_user_data(f_name,l_name,emailid,phno,paswrd):
        """this fn inserts  new data  into our database,return if true else false"""
        usersdata={"firstname":f_name,"lastname":l_name,"email":emailid,"contact":phno,"password":paswrd}
        users=dac.insert_one(usersdata)
        if users.acknowledged:
            return True
        return False
 