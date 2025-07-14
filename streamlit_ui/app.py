import streamlit as st
import requests

def signup_view():
    st.title("👤 Sign Up")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        response = requests.post("http://localhost:5000/user/SignUp", json={
            "username": username,
            "email": email,
            "password": password
        })
        st.write(response.status_code, response.text) 
        if response.status_code == 200:
            st.success("User creation successful!")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

def login_view():
    st.title("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post("http://localhost:5000/user/Login/{user_id}", json={
            "email": email,
            "password": password
        })
        if response.status_code == 200:
            st.success("Login successful!")
        else:
            st.error("Login failed.")

def create_notes_view():
    st.title("📝 Create Note")
    title = st.text_input("Title")
    description = st.text_input("Description")
    if st.button("Create Note"):
        response = requests.post("http://localhost:5000/user/notes", json={
            "title": title,
            "description": description
        })
        if response.status_code == 200:
            st.success("Note created!")
        else:
            st.error("Note creation failed.")

def fetch_notes_view():
    st.title("📒 Fetch Notes")
    user_id = st.text_input("Enter User ID")
    if st.button("Fetch Notes"):
        response = requests.get(f"http://localhost:5000/user/notes/{user_id}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error fetching notes.")

# Main app logic
st.sidebar.title("Navigation")
choice = st.sidebar.selectbox("Go to", ("Sign Up", "Login", "Create Note", "Fetch Notes"))

if choice == "Sign Up":
    signup_view()
elif choice == "Login":
    login_view()
elif choice == "Create Note":
    create_notes_view()
elif choice == "Fetch Notes":
    fetch_notes_view()
