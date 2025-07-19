from app.stores.notes import create_store, get_store, update_store, delete_store
from app.utils.user_validator import user_validator

# create notes
def create_service(user_id, data):
    try:
        if not user_validator(user_id):
            return {"error":"Invalid User!"}

        result = create_store(user_id, data)
        if result:
            # print(result)
            return {"notes_id":result}
        
    except Exception as e:
        return {"error":str(e)}
    
# # get notes
# def get_service(user_id):
#     try:
#         if not user_validator(user_id):
#             return {"error":"Invalid User!"}
    
#         result = get_store(user_id)
#         if result:
#             return {"notes": result}
#         else:
#             return {"message": "No notes are there!"}
        
#     except Exception as e:
#         return {"error": str(e)}
    
def get_service(user_id):
    try:
        if not user_validator(user_id):
            return {"error":"Invalid User!"}
    
        result = get_store(user_id)
        return {"notes": result or []}  # ✅ Always return a list under 'notes'
        
    except Exception as e:
        return {"error": str(e)}
    
# update notes
def update_service(user_id, notes_id, data):
    try:
        if not user_validator(user_id):
            return {"error":"Invalid User!"}
        
        rowCount = update_store(user_id, notes_id, data)

        if rowCount ==  0:
            return {"error":"Note Not Found!"}
        return {"rowCount":rowCount}
    
    except Exception as e:
        return {"error":str(e)}
    
# delete notes
def delete_service(user_id, notes_id):
    try:
        if not user_validator(user_id):
            return {"error":"Invalid User!"}
        
        rowCount = delete_store(user_id, notes_id)

        if rowCount ==  0:
            return {"error":"Note Not Found!"}
        return {"rowCount":rowCount}
    
    except Exception as e:
        return {"error":str(e)}