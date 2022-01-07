import torch

NETWORK = "./network-snapshot.pkl"
STEPS = 600
SKIPPED_FRAME_CAP = 10
FPS = 30
FREEZE_STEPS = 30
NUM_STEPS = 1000
SAVE_VIDEO = 0
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
STORAGE_DIR = "./aligned_images/"
PROJECTED_DIR = {"source": "./projected/source/", "target": "./projected/target/"}
MP4_DIR = "./output/"
