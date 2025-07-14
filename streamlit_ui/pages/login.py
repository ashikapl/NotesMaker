# import requests
# import streamlit as st

# def show():
#     st.title("🔐 Login")

#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         response = requests.post("http://localhost:5050/user/login", json={
#             "email": email,
#             "password": password
#         })

#         if response.status_code == 200:
#             st.success("Login successful!")
#         else:
#             st.error("Login failed.")
        
# show()        
