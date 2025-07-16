import requests
import streamlit as st

st.title("📓 Notes")

operation = st.selectbox("Select Operation", ["Create", "Fetch", "Update", "Delete"])
user_id = st.text_input("User ID")

if operation == "Create":
    title = st.text_input("Title")
    description = st.text_area("Description")
    if st.button("Create Note"):
        if not user_id:
            st.error("Invalid User!")
        elif not title or not description:
            st.error("Incompelete Data!")
        else:
            res = requests.post(f"http://127.0.0.1:5000/user/notes/{user_id}", json={
                "user_id": user_id,
                "title": title,
                "description": description
            })
            print(res)
            if res.status_code == 200:
                st.success("Note Created.")
            else:
                st.error("Note Creation Failed!")

elif operation == "Fetch":
    if st.button("Fetch Notes"):
        if not user_id:
            st.error("Invalid User!")
        else:
            res = requests.get(f"http://127.0.0.1:5000/user/notes/{user_id}")
            print(res)
            if res.status_code == 200:
               st.json(res.json())
            else:
               st.error("There is no note!")

elif operation == "Update":
    note_id = st.text_input("Note_Id")
    title = st.text_input("Title")
    description = st.text_input("Description")

    if st.button("Update Note"):
        if not user_id:
            st.error("Invalid User!")
        elif not note_id:
            st.error("Invalid Note!")
        else:
            res = requests.put(f"http://127.0.0.1:5000/user/notes/{user_id}/{note_id}", json={
                "note_id":note_id,
                "title":title,
                "description":description
            })
            print(res)
            if res.status_code == 200:
                st.success("Note Updated!")
            else:
                st.error("Updation failed!")
    
elif operation == "Delete":
    note_id = st.text_input("Note ID")
    if st.button("Delete Note"):
        if not user_id:
            st.error("Invalid User!")
        elif not note_id:
            st.error("Invalid Note!")
        else:
            res = requests.delete(f"http://127.0.0.1:5000/user/notes/{user_id}/{note_id}")
            print(res)
            if res.status_code == 200:
                st.success("Note Deleted.")
            else:
                st.error("Note Deletion Failed!")



# def create_note_view():
#     st.title("📝 Create Note")
#     user_id = st.text_input("User_Id")
#     title = st.text_input("Title")
#     description = st.text_input("Description")
#     if st.button("Create Note"):
#         if not user_id:
#             st.error("Invalid User!")
#         else:
#             response = requests.post(f"http://127.0.0.1:5000/user/notes/{user_id}", json={
#                 "user_id":user_id,
#                 "title": title,
#                 "description": description
#             })
#             # print(response)
#             if response.status_code == 200:
#                 st.success("Note created!")
#             else:
#                 st.error("Note creation failed!")

# def fetch_notes_view():
#     st.title("📒 Fetch Notes")
#     user_id = st.text_input("Enter User ID")
#     if st.button("Fetch Notes"):
#         if not user_id:
#             st.error("Invalid User!")
#         else:
#             response = requests.get(f"http://127.0.0.1:5000/user/notes/{user_id}")
#             # print(response)
#             if response.status_code == 200:
#                 st.json(response.json())
#             else:
#                 st.error("Error fetching notes.")

# def update_note_view():
#     st.title("Update Note")
#     user_id = st.text_input("User_Id")
#     note_id = st.text_input("Note_Id")
#     title = st.text_input("Title")
#     description = st.text_input("Description")

#     if st.button("Update Note"):
#         if not user_id or not note_id:
#             st.error("Invalid User or Note!")
#         else:
#             response = requests.put(f"http://127.0.0.1:5000/user/notes/{user_id}/{note_id}", json={
#                 "user_id":user_id,
#                 "note_id":note_id,
#                 "title":title,
#                 "description":description
#             })
#             print(response)
#             if response.status_code == 200:
#                 st.success("Note Updated!")
#             else:
#                 st.error("Updation failed!")

# def delete_note_view():
#     st.title("Delete Note")
#     user_id = st.text_input("User_Id")
#     note_id = st.text_input("Note_Id")

#     if st.button("Delete Note"):
#         if not user_id or not note_id:
#             st.error("Invalid User or Note!")
#         else:
#             response = requests.delete(f"http://127.0.0.1:5000/user/notes/{user_id}/{note_id}")
#             print(response)
#             if response.status_code == 200:
#                 st.success("Note Deleted!")
#             else:
#                 st.error("Deletion Failed!")
