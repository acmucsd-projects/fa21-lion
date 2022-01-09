import streamlit as st
import api
def app():
  st.title("Create New Account")

  new_user = st.text_input("Username",key='1')
  new_password = st.text_input("Password",type='password',key='2')

  if st.button("Register"):
    if len(new_user) < 5:
      st.error("Enter a username that is at least 5 characters.")
    if len(new_password) < 8:
      st.error("Enter a password that is at least 8 characters.")
    else:
      # TODO (Aman): Add your logic for registering under here
      # result = add_userdata(new_user,new_password)
      # I have assumed result returns false if username already exists
      # and true if registered successfully. Feel free to add more cases
      # if needed (eg. username is unique but failed to save in DB)
      # REMOVE NEXT LINE

      result = api.register(new_user, new_password)

      if result:
        st.success("You have successfully created an Account")
        st.info("Use the Left Sidebar to Create a New Cat Video or View Your Existing Videos")
      else:
        st.error("Username already exists.")
