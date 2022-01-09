"""
Do This before hand!
____________________

wget http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2
bzip2 -d shape_predictor_5_face_landmarks.dat.bz2

import sys

git clone https://github.com/NVlabs/stylegan2-ada-pytorch.git
pip install ninja

sys.path.insert(0, "/content/stylegan2-ada-pytorch")
"""

import argparse
import subprocess
import os
import glob
import sys
import cv2
import numpy as np
from PIL import Image
import torch
import imageio
import dlib
import dnnlib
import legacy
import shutil
import config
from utils import crop_stylegan, skipped_frames_by_step_num

import warnings
warnings.filterwarnings("ignore")

sys.path.insert(0, "./stylegan2-ada")

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--source", default="", type=str, required=True)
parser.add_argument("--target", default="", type=str, required=True)
args = parser.parse_args()

SOURCE_NAME = args.source
TARGET_NAME = args.target

print(SOURCE_NAME, TARGET_NAME)

NETWORK = config.NETWORK
STEPS = config.STEPS
SKIPPED_FRAME_CAP = config.SKIPPED_FRAME_CAP
FPS = config.FPS
FREEZE_STEPS = config.FREEZE_STEPS
NUM_STEPS = config.NUM_STEPS
SAVE_VIDEO = config.SAVE_VIDEO
DEVICE = config.DEVICE

# DIRs
TMP_DIR = config.TMP_DIR
STORAGE_DIR = config.STORAGE_DIR
PROJECTED_DIR = config.PROJECTED_DIR["projected"]
OUT_SOURCE = config.PROJECTED_DIR["source"]
OUT_TARGET = config.PROJECTED_DIR["target"]
MP4_DIR = config.MP4_DIR

# Make all necessary DIRs
print("Creating all DIRs")
if (not os.path.exists(TMP_DIR)): os.mkdir(TMP_DIR)
if (not os.path.exists(STORAGE_DIR)): os.mkdir(STORAGE_DIR)
if (not os.path.exists(PROJECTED_DIR)): os.mkdir(PROJECTED_DIR)
if (not os.path.exists(OUT_SOURCE)): os.mkdir(OUT_SOURCE)
if (not os.path.exists(OUT_TARGET)): os.mkdir(OUT_TARGET)
if (not os.path.exists(OUT_TARGET)): os.mkdir(OUT_TARGET)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor/shape_predictor_5_face_landmarks.dat')


image_source = cv2.imread(SOURCE_NAME)
image_target = cv2.imread(TARGET_NAME)

print("Cropping targets...")

# Preprocessing input images.
cropped_source = crop_stylegan(image_source, detector, predictor)
# cropped_target = crop_stylegan(image_target)
cropped_target = image_target  # For now we do this. We can apply a center crop function for animals if we find one.

cropped_source_path = os.path.join(STORAGE_DIR, "cropped_source.png")
cropped_target_path = os.path.join(STORAGE_DIR, "cropped_target.png")

cv2.imwrite(cropped_source_path, cropped_source)
cv2.imwrite(cropped_target_path, cropped_target)

print(f"Images {SOURCE_NAME} and {TARGET_NAME} cropped")
print(f"Cropped images stored in {STORAGE_DIR}")

# Extracting projections.
projector_path = "./stylegan2-ada/projector.py"

print("Converting Target to GAN...")
p1 = subprocess.call(["python", projector_path, "--save-video", str(SAVE_VIDEO), "--num-steps", str(NUM_STEPS), "--outdir", OUT_SOURCE, 
                     "--target", cropped_source_path, "--network", NETWORK])
print("Converting Source to GAN...")
p2 = subprocess.call(["python", projector_path, "--save-video", str(SAVE_VIDEO), "--num-steps", str(NUM_STEPS), "--outdir", OUT_TARGET, 
                     "--target", cropped_target_path, "--network", NETWORK])


# Generating video.
print("Setting up Video Generation...")
lvec1_path = os.path.join(OUT_SOURCE, "projected_w.npz")
lvec2_path = os.path.join(OUT_TARGET, "projected_w.npz")

lvec1 = np.load(lvec1_path)["w"]
lvec2 = np.load(lvec2_path)["w"]

# network_pkl = "https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/ffhq.pkl"
network_pkl = NETWORK  # Why?

with dnnlib.util.open_url(network_pkl) as fp:
    G = legacy.load_network_pkl(fp)['G_ema'].requires_grad_(False).to(DEVICE)

diff = lvec2 - lvec1
step = diff / STEPS
current = lvec1.copy()
target_uint8 = np.array([1024,1024,3], dtype=np.uint8)

video = imageio.get_writer(MP4_DIR, mode='I', fps=FPS, codec='libx264', bitrate='16M')

print("Generating Video...")
for j in range(STEPS):
  z = torch.from_numpy(current).to(DEVICE)
  synth_image = G.synthesis(z, noise_mode='const')
  synth_image = (synth_image + 1) * (255/2)
  synth_image = synth_image.permute(0, 2, 3, 1).clamp(0, 255).to(torch.uint8)[0].cpu().numpy()

  repeat = FREEZE_STEPS if j==0 or j==(STEPS-1) else 1

  kip_frames = skipped_frames_by_step_num(j, STEPS, SKIPPED_FRAME_CAP)
   
  if (repeat == 1 and skip_frames > 0):
    if (j % skip_frames == 0):
      video.append_data(synth_image)
  else:
    for i in range(repeat):
      video.append_data(synth_image)
  
  current = current + step

video.close()

# Clean-up.
print("Cleaning up...")
shutil.rmtree(TMP_DIR)

print(f"Success! Output video located at {MP4_DIR}")