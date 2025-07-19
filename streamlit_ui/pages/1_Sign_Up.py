# import requests
# import streamlit as st
# st.set_page_config(page_title="NotesMaker", layout="centered", initial_sidebar_state="collapsed")


# col1, col2, col3 = st.columns([1,4,2])

# with col2:
#     st.title("📝 NotesMaker")

# with col3:
#     st.markdown("###")
#     if "jwt_token" in st.session_state:
#         st.markdown("👤 **Account**")
#     else:
#         login_clicked = st.button("🔐 Login")
#         signup_clicked = st.button("📝 Sign Up")

#         if login_clicked:
#             st.switch_page("pages/2_Login.py")
#         if signup_clicked:
#             st.switch_page("pages/1_Sign_Up.py")

# # st.title("📝 Sign Up")

# # username = st.text_input("Username")
# # email = st.text_input("Email")
# # password = st.text_input("Password", type="password")

# # if st.button("Sign Up"):
# #     res = requests.post("http://localhost:5050/user/SignUp", json={
# #         "username": username,
# #         "email": email,
# #         "password": password
# #     })
# #     st.write(res.json())


# # def signup_view():
# st.title("👤 Sign Up")

# username = st.text_input("Username")
# email = st.text_input("Email")
# password = st.text_input("Password", type="password")
# if st.button("Sign Up"):
#     if not username or not email or not password:
#         st.error("All fields are required!")
#     elif len(password) < 8:
#         st.error("Password must be at least 8 characters long.")
#     else:
#         response = requests.post("http://127.0.0.1:5000/user/SignUp", json={
#             "username": username.strip(),
#             "email": email.strip(),
#             "password": password
#         })
#         # st.write(response.status_code, response.text)
#         if response.status_code == 200:
#             st.success("User creation successful!")

#             # automatically fill email, password in login page 
#             # Store to session_state for login page
#             st.session_state.login_email= email
#             st.session_state.login_password = password

#             # redirect to login page
#             st.switch_page("pages/2_Login.py")
#         else:
#             st.error(f"Error: {response.status_code} - {response.text}")