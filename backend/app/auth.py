from fastapi import Header, HTTPException
from app.security import get_admin_password

def verify_admin(x_admin_password: str = Header(None)):
    expected_password = get_admin_password()
    print("HEADER VALUE     :", repr(x_admin_password))
    print("SECRET VALUE     :", repr(expected_password))
    print("DEBUG HEADER:", x_admin_password)
    
    if not x_admin_password:
        raise HTTPException(status_code=401, detail="Admin password required")

    expected_password = get_admin_password()

    if x_admin_password != expected_password:
        raise HTTPException(status_code=401, detail="Invalid admin password")

    return True
