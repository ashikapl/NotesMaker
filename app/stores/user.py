from app.models.user import SignUp, Login
from app.utils.user_validator import user_validator
from config import DB_CONFIG

# SignUp Implementation
# Create User
def create_signUp_store(data):
    with DB_CONFIG.cursor() as cursor:
        query="INSERT INTO SignUp(username, email, password) VALUES (%s, %s, %s)"
        values=(data["username"], data["email"], data["password"])
        cursor.execute(query, values)
        DB_CONFIG.commit()
        return cursor.lastrowid, "SignUp created successfully"

# Login Implementation
# Create Login
def create_login_store(user_id, data):
    with DB_CONFIG.cursor() as cursor:
        query="INSERT INTO Login(user_id, email, password) VALUES (%s, %s, %s)"
        values=(user_id, data["email"], data["password"])
        cursor.execute(query, values)
        DB_CONFIG.commit()
        return cursor.lastrowid, "Login created successfully"
  