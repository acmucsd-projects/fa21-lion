# Core Packages
import streamlit as st
from PIL import Image
import numpy as np

# Page Configuration
st.set_page_config(page_title="Team Lion", layout="wide")

# Function to Read and Manipulate Images
def load_image(img):
  im = Image.open(img)
  image = np.array(im)
  return image

def main():

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
      st.markdown("Hey there! Welcome to Team Lion's Morph Ya Face Into Cat App. ADD ANY EXPLANATION HERE!      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consectetur euismod mi vulputate vehicula. Donec venenatis laoreet leo, eu viverra quam scelerisque nec. Sed ut placerat nisi. Duis gravida malesuada ultrices. Nam id metus vitae nisl mattis gravida. Nulla orci nibh, sollicitudin accumsan cursus vel, suscipit nec ante. Nulla facilisis orci massa, eget sagittis diam consequat vel. Morbi eu diam accumsan, tincidunt massa eget, pulvinar arcu. Donec dolor justo, tincidunt nec sapien eu, dapibus malesuada augue. Mauris odio ipsum, bibendum ac maximus sed, lacinia in nunc. Suspendisse potenti. Duis sit amet placerat lectus, a tristique turpis. Integer enim eros, rutrum vel ultrices in, fringilla interdum eros.")
      st.markdown(
          "**To begin, please upload a picture of a human face below.** 👇")

  # Row to contain the Image Uploader
  row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 3.2, .1))

  # Variables for the flags and the the files
  isConfirmed = False
  isPictureUploaded = False
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
    row2_spacer5, row2_3, row2_spacer8 = st.columns([1,1,1])
    img = Image.open(uploaded_file)
    row2_3.image(img)
    row2_spacer6, row2_spacer9, row2_spacer11, row2_spacer13, row2_spacer14, row2_spacer17, row2_4, row2_spacer18, row2_spacer15, row2_spacer16, row2_spacer12, row2_spacer6, row2_spacer7 = st.columns([1,1,1,1,1,1,1,1,1,1,1,1,1])
    # Display the button to morph the picture
    if row2_4.button('Morph It!'):
      # If button pressed, set flag to true to run GAN
      isConfirmed = True

  # If button pressed to morph, run GAN and display the video.
  if isConfirmed:
    row2_spacer3, row2_2, row2_spacer4 = st.columns((2, 3.2, 2))
    # '''
    # This is where the uploaded_file is sent to the GAN and the GAN runs it to return the video.

    # morphed_video = run_gan(uploaded_file)

    # !!! DELETE NEXT LINE - ONLY FOR REFERENCE !!!

    # Use Streamlit Lottie for Buffer Animation
    # '''
    morphed_video = open('4920.mp4', 'rb')
    video_bytes = morphed_video.read()

    with row2_2:
      st.video(video_bytes)


if __name__ == '__main__':
	main()
