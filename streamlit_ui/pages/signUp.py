# import requests
# import streamlit as st

# def show():
#     st.title("SignUp")

#     username = st.text_input("Username")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("SignUp"):
#         response = requests.post("http://localhost:5050/user/signUp", json={
#             "username":username,
#             "email": email,
#             "password": password
#         })

#         if response.status_code == 200:
#             st.success("User creation successful!")
#         else:
#             st.error("User creation failed.")


# show()