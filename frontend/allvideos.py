import streamlit as st
from PIL import Image
import numpy as np

import api
from constants import DEBUG

def app():
  st.title("View your saved videos")
  st.subheader("Login below to view all your saved videos.")
  username = st.text_input("User Name")
  password = st.text_input("Password",type='password')

  # If you click the button, it tries to first log in and then save
  if st.button('Login'):
    # If length of password is less than 8 characters, it does not start process of log in
    # and returns incorrect immediately.
    if len(password) < 8:
      st.error("Username/Password is incorrect. Please register if you haven't yet.")
    else:
      success, user_auth = api.login(username, password)
      if (DEBUG): print(f'DEBUG: api.login():: success {success} user auth {user_auth}')

      # If result is true, we have successfully logged in.
      if success:
        success, video_names = api.get_video_names(user_auth)
        if (DEBUG): print(f'DEBUG: success {success} allVideoNames - {video_names}')

        # If allVideos is empty, there are no videos in that account
        if len(video_names) <= 0:
          st.info("There are no videos in your account.")
        else:
          # Displays all videos
          st.subheader("Your saved videos:")
          row2_spacer3, row2_2, row2_spacer4 = st.columns((2, 3.2, 2))
          
          for video_name in video_names:
              success, morphed_video = api.get_file(user_auth, video_name)
              if not success:
                  print(f'ERROR: File {video_name} did not load successfully')
                  continue   
              row2_2.video(morphed_video.read())

      # If result is false, we return that username/password is incorrect
      else:
        st.error("Username/Password is incorrect. Please register if you haven't yet.")
