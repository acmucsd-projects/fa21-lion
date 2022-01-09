import streamlit as st
from PIL import Image
import numpy as np

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
    # TODO: (Aman) Do your login magic underneath
    # result, accessKey = check(username, password)
    # DELETE LINE WITH RESULT AND ACCESSKEY ASSIGNED
    else:
      result, accessKey = [True, '234483u3u3']
      # If result is true, we have successfully logged in.
      if result:
        # TODO: (Aman) Retrieve videos from database using accessKey
        # allVideos = getVideos(accessKey) #return True/False
        # DELETE NEXT LINE
        
        allVideos = ['4920.mp4', '4920.mp4', '4920.mp4', '4920.mp4', '4920.mp4'] 
        # If allVideos is empty, there are no videos in that account
        if len(allVideos) <= 0:
          st.info("There are no videos in your account.")
        else:
          # Displays all videos
          st.subheader("Your saved videos:")
          row2_spacer3, row2_2, row2_spacer4 = st.columns((2, 3.2, 2))
          for currVideo in allVideos:
            morphed_video = open(currVideo, 'rb')
            video_bytes = morphed_video.read()
            row2_2.video(video_bytes)

      # If result is false, we return that username/password is incorrect
      else:
        st.error("Username/Password is incorrect. Please register if you haven't yet.")
