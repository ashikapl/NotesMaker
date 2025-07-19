import streamlit as st
import requests

# ----- Config -----
st.set_page_config(page_title="NotesMaker", layout="centered")

# ----- Session State Initialization -----
if "view" not in st.session_state:
    st.session_state.view = "home"
if "jwt_token" not in st.session_state:
    st.session_state.jwt_token = None

# ----- Top Section -----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1 style='text-align: center;'>📚 Welcome to NotesMaker</h1>", unsafe_allow_html=True)
with col3:
    if st.session_state.jwt_token:
        if st.button("🔓 Logout"):
            st.session_state.jwt_token = None
            st.session_state.view = "home"
    else:
        if st.button("👤 Sign Up"):
            st.session_state.view = "signup"
        if st.button("🔐 Login"):
            st.session_state.view = "login"
        # if st.button("notes"):
        #     st.session_state.view = "notes"

# ----- Sign Up View -----
if st.session_state.view == "signup":
    st.subheader("👤 Create a New Account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up Now"):
        if not username or not email or not password:
            st.error("All fields are required.")
        elif len(password) < 8:
            st.error("Password must be at least 8 characters.")
        else:
            response = requests.post("http://127.0.0.1:5000/user/SignUp", json={
                "username": username,
                "email": email,
                "password": password
            })
            if response.status_code == 200:
                st.success("Account created! Please log in.")
                st.session_state.login_email = email
                st.session_state.login_password = password
                st.session_state.view = "login"
            else:
                st.error(response.json().get("error", "Signup failed."))

# ----- Login View -----
elif st.session_state.view == "login":
    st.subheader("🔐 Login to Your Account")
    email = st.text_input("Email", value=st.session_state.get("login_email", ""))
    password = st.text_input("Password", type="password", value=st.session_state.get("login_password", ""))

    if st.button("Login Now"):
        if not email or not password:
            st.error("All fields are required.")
        else:
            response = requests.post("http://127.0.0.1:5000/user/Login", json={
                "email": email,
                "password": password
            })
            if response.status_code == 200:
                st.session_state.jwt_token = response.json().get("token")
                st.success("Logged in successfully!")
                st.session_state.view = "notes"
            else:
                st.error(response.json().get("error", "Login failed."))

# ----- Notes Dashboard View -----
elif st.session_state.view == "notes":
    st.subheader("📝 Your Notes Dashboard")

    headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}

    # Create a New Note
    with st.expander("➕ Create a New Note"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        if st.button("Create Note"):
            if title and description:
                res = requests.post("http://127.0.0.1:5000/user/notes", json={
                    "title": title,
                    "description": description
                }, headers=headers)
                if res.status_code == 200:
                    st.success("Note created!")
                    st.rerun()
                else:
                    st.error("Failed to create note.")
            else:
                st.warning("Please enter title and description.")

    # Fetch and Display Notes
    st.markdown("---")
    st.subheader("📄 Your Existing Notes")
    res = requests.get("http://127.0.0.1:5000/user/notes", headers=headers)
    if res.status_code == 200:
        notes = res.json().get("notes", [])
        if not notes:
            st.info("You have no notes yet.")
        for note in notes:
            if isinstance(note, dict):
                with st.expander(f"📝 {note['title']}"):
                    st.write(note["description"])
                    st.write(f"Note ID: {note['note_id']}")
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("✏️ Edit", key=f"edit_{note['note_id']}"):
                        new_title = st.text_input("New Title", value=note["title"], key=f"new_title_{note['note_id']}")
                        new_desc = st.text_area("New Description", value=note["description"], key=f"new_desc_{note['note_id']}")
                        if st.button("✅ Save Changes", key=f"save_{note['note_id']}"):
                            update_res = requests.put(f"http://127.0.0.1:5000/user/notes/{note['note_id']}", json={
                                "title": new_title,
                                "description": new_desc
                            }, headers=headers)
                            if update_res.status_code == 200:
                                st.success("Note updated!")
                                st.rerun()
                            else:
                                st.error("Failed to update.")
                with col2:
                    if st.button("🗑️ Delete", key=f"delete_{note['note_id']}"):
                        delete_res = requests.delete(f"http://127.0.0.1:5000/user/notes/{note['note_id']}", headers=headers)
                        if delete_res.status_code == 200:
                            st.success("Note deleted.")
                            st.rerun()
                        else:
                            st.error("Failed to delete.")
    else:
        st.error("Error fetching notes. Please try again.")
