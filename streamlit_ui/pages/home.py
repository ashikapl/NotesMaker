# import requests
# import streamlit as st

# def show():
#     st.title("Notes")

#     title = st.text_input("title")
#     description = st.text_input("description")

#     if st.button("Notes"):
#         response = requests.post("http://localhost:5050/user/notes", json={
#             "title": title,
#             "description": description
#         })

#         if response.status_code == 200:
#             st.success("Note created!")
#         else:
#             st.error("Note creation failed.")

            
# show()
