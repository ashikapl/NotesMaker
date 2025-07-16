import requests
import streamlit as st

# st.title("🔐 Login")

# email = st.text_input("Email")
# password = st.text_input("Password", type="password")

# if st.button("Login"):
#     res = requests.post("http://localhost:5050/user/Login", json={
#         "email": email,
#         "password": password
#     })
#     st.write(res.json())


# def login_view():
st.title("🔐 Login")

if "login_email" not in st.session_state:
    st.session_state.login_email = ""

email = st.text_input("Email", key="login_email")
password = st.text_input("Password", type="password", key="login_password")
if st.button("Login"):
    if not email or not password:
        st.error("All fields are required!")
    else:
        response = requests.post("http://127.0.0.1:5000/user/Login", json={
            "email": email,
            "password": password
        })
        if response.status_code == 200:
            st.success("Login successful!")

            # redirect to Notes(home) page
            st.switch_page("pages/3_Notes.py")
        else:
            st.error("Login failed.")      
