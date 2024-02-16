

def validate_fullname(Fullname):
    
    if not Fullname:
        return {'message':"Fullname cannot be empty"}
    if len(Fullname) > 25:
        return {'message':"Fullname should not be more than 25 characters long"}
    if not all(part.isalpha() or part.isspace() for part in Fullname):
        return{'message':"Fullname can only contain alphabets and spaces"}
    return None

def validate_email_domain(email, accepted_domains):
    if not any(email.endswith(domain) for domain in accepted_domains):
        return {'message': "Invalid email domain. Allowed domains: gmail.com, yahoo.com, outlook.com, example.com"}, 400
    return None

def validate_password(password):
    if len(password) < 8 or not (any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and any(not c.isalnum() for c in password)):
        return {'message': "Password should be at least 8 characters and contain at least one digit, one letter, and one special character"}, 400
    return None

def validate_contact_number(contact_no):
    if not contact_no.isdigit() or len(contact_no) != 10:
        return {'message': "Invalid contact number format. Please enter a 10-digit number."}, 400
    return None
