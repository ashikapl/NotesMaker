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