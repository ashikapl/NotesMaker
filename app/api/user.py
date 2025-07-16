from flask import Flask, jsonify, request, Blueprint
from app.services.user import create_signUp_service, create_login_service

user_bp = Blueprint("user_bp", __name__)

# @user_bp.route("/", methods=["POST"])
# def signup():
#     try:
#         data = request.get_json()
#         print("Received data:", data)  # ✅ Add this
#         username = data.get("username")
#         email = data.get("email")
#         password = data.get("password")

#         # Your DB logic here
#         # For now just test with a success message:
#         return jsonify({"message": "User created"}), 200

#     except Exception as e:
#         print("Signup error:", e)  # ✅ Catch and show error in terminal
#         return jsonify({"error": str(e)}), 500


# SignUp User
@user_bp.route("/SignUp", methods=["POST"])
def create_signUp():
    data = request.get_json()
    res = create_signUp_service(data)

    if "error" in res:
        return jsonify(res), 404
    return jsonify({"message":"User Created Successfully!", "res":res["user_id"]}), 200

# Login User
@user_bp.route("/Login", methods=["POST"])
def create_login():
    data = request.get_json()
    # print('data :', data)
    res = create_login_service(data)

    if "error" in res:
        # print('res:', res)
        return jsonify(res), 404
    return jsonify({"message":"User Login Successfull!", "id":res["id"]}), 200

