ADMIN_PERMISSIONS =["create_slot",
                    "create_sub_resource",
                    "booking_resource",
                    "delete_slot",
                    "update_by_admin_id"
                    ] 

PERMISSIONS = ['view_slots',
                'book_slot',
                "cancel_booking",
                "view_history", 
                "user_login",
                "user_logout",
                "password_reset_request",
                "password_reset",
                "edit_user_profile",
                "view_profile",
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
COLLECTION_SLOT_DETAILS= "slot_details"
COLLECTION_SUBRESOURCE_DETAILS = "subresource_details"
ACCOUNT_HOLDERS_COLLECTION = "Account_holders"
BOOKING_RESOURCE_COLLECTION = "booking_resource_details"
###collection ####names####
