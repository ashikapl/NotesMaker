from app.models.user import SignUp
from config import DB_CONFIG

def user_validator(user_id):
    with DB_CONFIG.cursor() as cursor:
        query="SELECT user_id FROM SignUp WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        signUp_id = cursor.fetchone()

        if not signUp_id:
            return False
        else:
            return True
        
def user_validator_login(email, password):
    with DB_CONFIG.cursor() as cursor:
        query = "SELECT user_id, username, password FROM SignUp WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            db_password = user[2]  # password
            if db_password == password:
                return {"user_id": user[0], "username": user[1]}
        else:
            return False