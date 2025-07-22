import pymysql
from app.stores.user import create_signUp_store, create_login_store
from app.utils.user_validator import user_validator_login
from app.utils.create_token import generate_token

# create signUp
def create_signUp_service(data):
    try:
        result = create_signUp_store(data)
        if result:
            return {"user_id": result[0], "message": result[1]}
    except pymysql.err.IntegrityError as e:
        if "Duplicate entry" in str(e):
            return {"error": "Email already exists."}
        return {"error": "Database integrity error."}
    except Exception as e:
        return {"error": "Something went wrong. Please try again later."}

def create_login_service(data):
    try:
        user_data = user_validator_login(data['email'], data['password'])
        if not user_data:
            return {"error": "Invalid email or password"}

        user_id = user_data['user_id']
        token = generate_token(user_id)
        # result = create_login_store(user_id, data)
        return {"token": token, "message": "Login Successfull!"}
    except Exception as e:
        print('Login Error:', str(e))
        return {"error": str(e)}