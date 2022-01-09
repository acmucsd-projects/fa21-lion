import torch

#all
TMP_DIR = "./tmp/"

# transform script
CAT_DIR = "./cat_images/"
HUMAN_IMG_NAME = "human_face.png"
PREDICT_PATH = "./predict.py"

#predict script
NETWORK = "./weights/network-snapshot.pkl"
STEPS = 2000
SKIPPED_FRAME_CAP = 30
FPS = 30
FREEZE_STEPS = 30
NUM_STEPS = 1000
SAVE_VIDEO = 0
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
STORAGE_DIR = TMP_DIR + "aligned_images/"
PROJECTED_DIR = {
    "projected": TMP_DIR + "projected/",
    "source": TMP_DIR + "projected/source/", 
    "target": TMP_DIR + "projected/target/"
}
MP4_DIR = "./output/"