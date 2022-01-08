import os
import sys
import glob
import cv2
import random
import subprocess
import config
import shutil

TMP_DIR = config.TMP_DIR
CAT_DIR = config.CAT_DIR
HUMAN_IMG_NAME = config.HUMAN_IMG_NAME
PREDICT_PATH = config.PREDICT_PATH

def transform(human_face):

    os.mkdir(TMP_DIR)

    human_face_path = TMP_DIR + HUMAN_IMG_NAME
    cv2.imwrite(human_face_path, human_face)

    cat_num = random.rand(0, len([name for name in os.listdir(CAT_DIR) if os.path.isfile(os.path.join(DIR, name))]) - 1)
    cat_file = os.listdir(CAT_DIR)[cat_num]

    cat_face = cv2.cvtColor(CAT_DIR + cat_file, cv2.COLOR_BGR2RGB)
    cat_face_path = TMP_DIR + cat_file
    cv2.imwrite(cat_face_path, cat_face)

    morph = subprocess.run(["python", PREDICT_PATH, f"--source {human_face_path}", f"--target {cat_face_path}"])

    shutil.rmtree(TMP_DIR)

    return True