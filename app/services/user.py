from app.stores.user import create_signUp_store, create_login_store
from app.utils.user_validator import user_validator_login

# create signUp
def create_signUp_service(data):
    try:
        result = create_signUp_store(data)
        if result:
            return {"user_id": result[0], "message": result[1]}
    except Exception as e:
        return {"error":str(e)}

# create login
# def create_login_service(data):
#     try:
#         if not user_validator_login(data['email'], data['password']):
#             return {"error":"Invalid User!"}
        
#         user_id = user_validator_login(data['email'], data['password'])['user_id']

#         result = create_login_store(user_id, data)
#         return {"id": result[0], "message": result[1]}
#         # return {"id": user_id, "message": "Login created successfully"}
#     except Exception as e:
#         print('e: ', str(e))
#         return {"error": str(e)}

def create_login_service(data):
    try:
        user_data = user_validator_login(data['email'], data['password'])
        if not user_data:
            return {"error": "Invalid email or password"}

        user_id = user_data['user_id']
        result = create_login_store(user_id, data)
        return {"id": result[0], "message": result[1]}
    except Exception as e:
        print('Login Error:', str(e))
        return {"error": str(e)}