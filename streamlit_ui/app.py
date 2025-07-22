# import streamlit as st
# import requests
# import re

# # ----- Config -----
# st.set_page_config(page_title="NotesMaker", layout="centered")

# # Initialize session state keys
# # if "note_title" not in st.session_state:
# #     st.session_state.note_title = ""
# # if "note_desc" not in st.session_state:
# #     st.session_state.note_desc = ""
# # if "note_created" not in st.session_state:
# #     st.session_state.note_created = False
# if "show_create_note" not in st.session_state:
#     st.session_state.show_create_note = True

# # ----- Session State Initialization -----
# if "view" not in st.session_state:
#     st.session_state.view = "home"
# if "jwt_token" not in st.session_state:
#     st.session_state.jwt_token = None

# # ----- Top Section -----
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.markdown("<h1 style='text-align: center;'>📚 Welcome to NotesMaker</h1>", unsafe_allow_html=True)
# with col3:
#     if st.session_state.jwt_token:
#         if st.button("🔓 Logout"):
#             st.session_state.jwt_token = None
#             st.session_state.view = "home"
#             st.rerun()
#     else:
#         if st.button("👤 Sign Up"):
#             st.session_state.view = "signup"
#             st.rerun()
#         if st.button("🔐 Login"):
#             st.session_state.view = "login"
#             st.rerun()

# def is_valid_email(email):
#     # You can modify this pattern to be more general or stricter as needed
#     return re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email)

# # ----- Sign Up View -----
# if st.session_state.view == "signup":
#     st.subheader("👤 Create a New Account")
#     username = st.text_input("Username")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Sign Up Now"):
#         if not username or not email or not password:
#             st.error("All fields are required.")
#         elif not is_valid_email(email):
#             st.error("Please enter a valid Gmail address (e.g. user@gmail.com).")
#         elif len(password) < 8:
#             st.error("Password must be at least 8 characters.")
#         else:
#             response = requests.post("http://127.0.0.1:5000/user/SignUp", json={
#                 "username": username,
#                 "email": email,
#                 "password": password
#             })
#             if response.status_code == 200:
#                 st.success("Account created! Please log in.")
#                 st.session_state.login_email = email
#                 st.session_state.login_password = password
#                 st.session_state.view = "login"
#                 st.rerun()
#             else:
#                 st.error(response.json().get("error", "Signup failed."))

# # ----- Login View -----
# elif st.session_state.view == "login":
#     st.subheader("🔐 Login to Your Account")
#     email = st.text_input("Email", value=st.session_state.get("login_email", ""))
#     password = st.text_input("Password", type="password", value=st.session_state.get("login_password", ""))

#     if st.button("Login Now"):
#         if not email or not password:
#             st.error("All fields are required.")
#         else:
#             response = requests.post("http://127.0.0.1:5000/user/Login", json={
#                 "email": email,
#                 "password": password
#             })
#             if response.status_code == 200:
#                 st.session_state.jwt_token = response.json().get("token")
#                 st.success("Logged in successfully!")
#                 st.session_state.view = "notes"
#                 st.rerun()
#             else:
#                 st.error(response.json().get("error", "Login failed."))

# # ----- Notes Dashboard View -----
# elif st.session_state.view == "notes":
#     st.subheader("📝 Your Notes Dashboard")

#     headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}

#     # if "show_create_note" not in st.session_state:
#     #     st.session_state.show_create_note = True

#     # Create a New Note
#     if st.session_state.show_create_note:
#         with st.expander("➕ Create a New Note", expanded=True):
#             title = st.text_input("Title", key="title")
#             description = st.text_area("Description", key="description")
#             if st.button("Create Note"):
#                 if title and description:
#                     res = requests.post("http://127.0.0.1:5000/user/notes", json={
#                         "title": title,
#                         "description": description
#                     }, headers=headers)
#                     if res.status_code == 200:
#                         st.success("Note created!")
#                         # st.session_state.title = ""
#                         # st.session_state.description = ""
#                         # st.session_state.show_create_note = False
#                         # st.rerun()

#     # Fetch and Display Notes
#     st.markdown("---")
#     st.subheader("📄 Your Existing Notes")
#     res = requests.get("http://127.0.0.1:5000/user/notes", headers=headers)
#     if res.status_code == 200:
#         notes = res.json().get("notes", [])
#         if not notes:
#             st.info("You have no notes yet.")
#         # print(notes)
#         for note in notes:
#             with st.expander(f"📝 {note[2]}"):
#                 st.write(note[3])
#                 st.write(f"Note ID: {note[0]}")
                
#                 col1, col2 = st.columns([1, 1])

#                 with col1:
#                     if st.button("✏️ Edit", key=f"edit_{note[0]}"):
#                         st.session_state[f"editing_{note[0]}"] = True

#                     if st.session_state.get(f"editing_{note[0]}", False):
#                         new_title = st.text_input("New Title", value=note[2], key=f"new_title_{note[0]}")
#                         new_desc = st.text_area("New Description", value=note[3], key=f"new_desc_{note[0]}")
#                         if st.button("✅ Save Changes", key=f"save_{note[0]}"):
#                             update_res = requests.put(f"http://127.0.0.1:5000/user/notes/{note[0]}", json={
#                                 "title": new_title,
#                                 "description": new_desc
#                             }, headers=headers)
#                             if update_res.status_code == 200:
#                                 st.success("Note updated!")
#                                 # st.rerun()
#                             else:
#                                 st.error("Failed to update.")

#                 with col2:
#                     if st.button("🗑️ Delete", key=f"delete_{note[0]}"):
#                         delete_res = requests.delete(f"http://127.0.0.1:5000/user/notes/{note[0]}", headers=headers)
#                         if delete_res.status_code == 200:
#                             st.success("Note deleted.")
#                             st.rerun()
#                         else:
#                             st.error("Failed to delete.")
#     else:
#         st.error("Error fetching notes. Please try again.")

import streamlit as st
import requests
import re

# ----- Config -----
st.set_page_config(page_title="NotesMaker", layout="centered")

# ----- Session State Initialization -----
for key, default in {
    "view": "home",
    "jwt_token": None,
    "login_email": "",
    "login_password": "",
    "show_create_note": True,
    "note_created": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email)

# ----- Top Navbar -----
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<h1 style='text-align:center;'>📚 NotesMaker</h1>", unsafe_allow_html=True)
with col3:
    if st.session_state.jwt_token:
        if st.button("🔓 Logout"):
            st.session_state.view = "home"
            st.session_state.jwt_token = None
            st.rerun()
    else:
        if st.button("👤 Sign Up"):
            st.session_state.view = "signup"
            st.rerun()
        if st.button("🔐 Login"):
            st.session_state.view = "login"
            st.rerun()

# ----- Sign Up View -----
if st.session_state.view == "signup":
    st.subheader("👤 Create a New Account")
    username = st.text_input("Username")
    email    = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up Now"):
        if not (username and email and password):
            st.error("All fields are required.")
        elif not is_valid_email(email):
            st.error("Please enter a valid Gmail address.")
        elif len(password) < 8:
            st.error("Password must be at least 8 characters.")
        else:
            resp = requests.post(
                "http://127.0.0.1:5000/user/SignUp",
                json={"username":username, "email":email, "password":password}
            )
            if resp.status_code == 200:
                st.success("Account created! Please log in.")
                st.session_state.login_email    = email
                st.session_state.login_password = password
                st.session_state.view = "login"
                st.rerun()
            else:
                st.error(resp.json().get("error","Signup failed."))

# ----- Login View -----
elif st.session_state.view == "login":
    st.subheader("🔐 Login to Your Account")
    email    = st.text_input("Email",    value=st.session_state.login_email)
    password = st.text_input("Password", type="password", value=st.session_state.login_password)

    if st.button("Login Now"):
        if not (email and password):
            st.error("All fields are required.")
        else:
            resp = requests.post(
                "http://127.0.0.1:5000/user/Login",
                json={"email":email, "password":password}
            )
            if resp.status_code == 200:
                st.session_state.jwt_token = resp.json().get("token")
                st.success("Logged in successfully!")
                st.session_state.view = "notes"
                st.rerun()
            else:
                st.error(resp.json().get("error","Login failed."))

# ----- Notes Dashboard View -----
elif st.session_state.view == "notes":
    st.subheader("📝 Your Notes Dashboard")
    headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}

    # 1) Define your on-click callback up top:
    def handle_create_note():
        # read state
        title = st.session_state.note_title
        desc  = st.session_state.note_desc

        # call your API
        res = requests.post(
            "http://127.0.0.1:5000/user/notes",
            json={"title": title, "description": desc},
            headers=headers,
        )
        if res.status_code == 200:
            # st.session_state.note_created    = True
            # st.session_state.show_create_note = False
            # **reset before next render**
            st.session_state.note_title = ""
            st.session_state.note_desc  = ""
        else:
            st.session_state.note_error = res.json().get("error", "Failed to create note.")

    # 2) Ensure these keys exist:
    for key, default in {
        "show_create_note": True,
        "note_title":       "",
        "note_desc":        "",
        "note_created":     False,
        "note_error":       ""
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    # 3) Render the expander & widgets, wiring the button to the callback:
    if st.session_state.show_create_note:
        with st.expander("➕ Create a New Note", expanded=True):
            st.text_input("Title",       key="note_title")
            st.text_area("Description",  key="note_desc")
            # no inline logic here — just wire the click to your function:
            st.button("Create Note", on_click=handle_create_note)

    # 4) Show feedback
    if st.session_state.note_created:
        st.success("Note created!")
        st.session_state.note_created = False

    if st.session_state.note_error:
        st.error(st.session_state.note_error)
        st.session_state.note_error = ""

    # … then fetch & render existing notes as before 

    st.markdown("---")
    st.subheader("📄 Your Existing Notes")

    # — Fetch & display notes —
    res = requests.get("http://127.0.0.1:5000/user/notes", headers=headers)
    if res.status_code != 200:
        st.error("Error fetching notes.")
        st.stop()

    notes = res.json().get("notes",[])
    if not notes:
        st.info("You have no notes yet.")
    for note_id, _, title, desc in notes:
        with st.expander(f"📝 {title}"):
            st.write(desc)
            st.write(f"Note ID: {note_id}")

            col1, col2 = st.columns(2)

            # — Edit Button —
            with col1:
                if st.button("✏️ Edit", key=f"edit_{note_id}"):
                    st.session_state[f"editing_{note_id}"] = True

            # — Edit Form —
            if st.session_state.get(f"editing_{note_id}", False):
                new_title = st.text_input("New Title",
                                           value=title,
                                           key=f"new_title_{note_id}")
                new_desc  = st.text_area("New Description",
                                         value=desc,
                                         key=f"new_desc_{note_id}")
                if st.button("✅ Save Changes", key=f"save_{note_id}"):
                    upd = requests.put(
                        f"http://127.0.0.1:5000/user/notes/{note_id}",
                        json={"title":new_title,"description":new_desc},
                        headers=headers
                    )
                    if upd.status_code == 200:
                        st.success("Note updated!")
                        # turn off edit + clear fields
                        st.session_state[f"editing_{note_id}"] = False
                        for fld in (f"new_title_{note_id}", f"new_desc_{note_id}"):
                            st.session_state.pop(fld, None)
                        st.rerun()
                    else:
                        st.error("Failed to update.")

            # — Delete Button —
            with col2:
                if st.button("🗑️ Delete", key=f"delete_{note_id}"):
                    dl = requests.delete(
                        f"http://127.0.0.1:5000/user/notes/{note_id}",
                        headers=headers
                    )
                    if dl.status_code == 200:
                        st.success("Note deleted.")
                        st.rerun()
                    else:
                        st.error("Failed to delete.")
