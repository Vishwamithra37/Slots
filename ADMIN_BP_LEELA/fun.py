import global_config
from decorators import login_required
def create_admin_details(email,admin_id):
    admin_details = {
        "email": email,
        "admin_id": admin_id,
        "Permissions": global_config.ADMIN_PERMISSIONS
    }
    
    return admin_details