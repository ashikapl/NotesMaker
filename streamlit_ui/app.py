import streamlit as st
# import requests
# from pages.SignUp import signup_view
# from pages.Login import login_view
# from pages.Home import create_note_view, fetch_notes_view, update_note_view, delete_note_view

st.set_page_config(page_title="Notes App", layout="centered")
st.title("📚 Welcome to Notes App")
st.markdown("Navigate using the sidebar to Sign Up, Login, or manage your Notes.")


# import streamlit as st

# st.set_page_config(page_title="Notes App", layout="wide")
# st.title("📚 Welcome to Notes App")
# st.write("Choose a page from the sidebar: Sign Up, Login, or Home")


# st.sidebar.title("Navigation")
# choice = st.sidebar.selectbox("Go to", ("Sign Up", "Login"))

# if choice == "Sign Up":
#     signup_view()
# elif choice == "Login":
#     login_view()

# st.sidebar.title("Navigation")
# choice = st.sidebar.selectbox("Go to", ("Create Note", "Fetch Notes", "Update Note", "Delete Note"))

# if choice == "Create Note":
#     create_note_view()
# elif choice == "Fetch Notes":
#     fetch_notes_view()
# elif choice == "Update Note":
#     update_note_view()
# elif choice == "Delete Note":
#     delete_note_view()