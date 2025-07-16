import requests
import streamlit as st

# st.title("📝 Sign Up")

# username = st.text_input("Username")
# email = st.text_input("Email")
# password = st.text_input("Password", type="password")

# if st.button("Sign Up"):
#     res = requests.post("http://localhost:5050/user/SignUp", json={
#         "username": username,
#         "email": email,
#         "password": password
#     })
#     st.write(res.json())


# def signup_view():
st.title("👤 Sign Up")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
if st.button("Sign Up"):
    if not username or not email or not password:
        st.error("All fields are required!")
    elif len(password) < 8:
        st.error("Password must be at least 8 characters long.")
    else:
        response = requests.post("http://127.0.0.1:5000/user/SignUp", json={
            "username": username.strip(),
            "email": email.strip(),
            "password": password
        })
        # st.write(response.status_code, response.text)
        if response.status_code == 200:
            st.success("User creation successful!")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")