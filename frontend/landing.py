# Core Packages
from os import access
import streamlit as st
from PIL import Image
import numpy as np

import api
from constants import DEBUG

def app():

  # Function to Read and Manipulate Images
  def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

  # Title and Centering It
  st.title("Team Lion")
  title_alignment="""
  <style>
  #team-lion {
    text-align: center
  }
  </style>
  """
  st.markdown(title_alignment, unsafe_allow_html=True)

  # Setting Two Columns for Description of the App
  row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2, .2, 1, .1))

  row0_1.title('Morph a human face to a cat')

  with row0_2:
      st.write('')

  row0_2.subheader(
      'An ML web app by Aman, Arth, Gaurav and Vincent.')

  row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))

  with row1_1:
      st.markdown("Hey there! Welcome to Team Lion's Morph Ya Face Into Cat App. You can upload an image into this app and we will perform geometric facial transfirguration to generate a video of your face getting transformed into a cat! ")
      st.markdown(
          "**To begin, please upload a picture of a human face below.** 👇")

  # Row to contain the Image Uploader
  row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 3.2, .1))

  # Variables for the flags and the the files
  isConfirmed = False
  isPictureUploaded = False
  isSaved = False
  isSuccessfulLogin = False
  morphed_video = None
  uploaded_file = None

  # Component for uploading the image
  # TODO: Currently put JPG, PNG and JPEG as supported files. Modify as required.
  with row2_1:
      uploaded_file = st.file_uploader("",type=['jpg', 'png', 'jpeg'])

      # Checking the Format of the Image
      if uploaded_file is not None:
          # Set Flag to True to Display Image and Option to Morph the Picture
          isPictureUploaded = True
            
      else:
          st.write("Make sure your image is in JPG/PNG/JPEG Format.")

      # TODO: If there is no JPG uploaded, what to do?
  
  # If Picture Uploaded, display picture and button to morph the picture.
  if isPictureUploaded:
    row2_spacer5, row2_3, row2_spacer8 = st.columns([0.78,1,1])
    img = Image.open(uploaded_file)
    row2_3.image(img)

    row2_spacer6, row2_spacer9, row2_4, row2_spacer6, row2_spacer7 = st.columns([1,1,1,1,1])
    # Display the button to morph the picture
    optionSelected = row2_4.multiselect('Do you want to morph this picture?', ('Morph it!', 'Let me rethink.'))
    if optionSelected == ['Morph it!']:
      # If button pressed, set flag to true to run GAN
      isConfirmed = True
  
  # If button pressed to morph, run GAN and display the video.
  row2_spacer3, row2_2, row2_spacer4 = st.columns((2, 3.2, 2))
  if isConfirmed:
    # This is where the uploaded_file is sent to the GAN and the GAN runs it to return the video.
    success, morphed_video = api.transformImage(uploaded_file)
    if success:
      row2_2.video(morphed_video.read())
      saveSelected = row2_2.multiselect('Do you want to save this picture and video?', ('Sure!', 'Let me rethink.'))
      if saveSelected == ['Sure!']:
        # If button pressed, set flag to true to run GAN
        isSaved = True

# If User wants to save the video
  if isSaved:
    row2_2.markdown("**You can save your image and morphed video by logging in.** You can register by going to the Register Page in the Left Menu.")

    # Following variables take in the username and the password.
    username = row2_2.text_input("User Name")
    password = row2_2.text_input("Password",type='password')

    # If you click the button, it tries to first log in and then save
    if row2_2.button('Login and Save'):
      # If length of password is less than 8 characters, it does not start process of log in
      # and returns incorrect immediately.
      if len(password) < 8:
        row2_2.error("Username/Password is incorrect. Please register if you haven't yet.")
      else:
        success, user_auth = api.login(username, password)
        # If result is true, we have successfully logged in.
        if success:
          saveVideo, errorMessage = api.save_transformation(user_auth, morphed_video)
          if (DEBUG): print(f'saveVideo {saveVideo} error message {errorMessage}')
          # If saveVideo returns true, then video has been saved successfully.
          if saveVideo:
            row2_2.success("Video Saved Successfully")
          else:
            row2_2.error("Video cannot be saved. Please try again later.")

        # If result is false, we return that username/password is incorrect
        else:
          row2_2.error("Username/Password is incorrect. Please register if you haven't yet.")
