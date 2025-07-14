from app.stores.user import create_signUp_store, create_login_store
from app.utils.user_validator import user_validator

# create signUp
def create_signUp_service(data):
    try:
        result = create_signUp_store(data)
        if result:
            return {"user_id": result[0], "message": result[1]}
    except Exception as e:
        return {"error":str(e)}
    
# create login
def create_login_service(user_id, data):
    try:
        if not user_validator(user_id):
            return {"error":"Invalid User!"}
        
        result = create_login_store(user_id, data)
        return {"id": result[0], "message": result[1]}
    except Exception as e:
        return {"error": str(e)}
