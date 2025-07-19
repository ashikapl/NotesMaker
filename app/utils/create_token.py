import jwt
import datetime

SECRET_KEY = "my_secret_key"

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# print("Token:- ", generate_token(1))