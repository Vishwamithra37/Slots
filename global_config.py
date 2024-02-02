ADMIN_PERMISSIONS =["create_resource",
                    "delete_slot",
                    "update_by_admin_id"
                    ] 

PERMISSIONS = ['view_slots',
                'book_slot',
                "cancel_booking",
                "view_history", 
                "edit_user_profile",
                "profile_view",
                "create_resource",
                "get_all_resources"] +ADMIN_PERMISSIONS


ACCEPTED_DOMAINS = ["gmail.com",
                    "yahoo.com",
                    "outlook.com",
                    "slotzz.in"]
MONGOCLIENT = 'mongodb://localhost:27017/'
DB = 'Slotzz'
###collection ####names###
COLLECTION_RESOURCE_DETAILS = "resource_details"
COLLECTION_ADMIN_DETAILS= "admin_details"
###collection ####names####

