import global_config
from decorators import login_required
def create_admin_details(email,resource_unique_id):
    admin_details = {
        "email": email,
        "admin_id": resource_unique_id,
        "Permissions": global_config.ADMIN_PERMISSIONS
    }
    
    return admin_details