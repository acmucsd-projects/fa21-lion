import torch

NETWORK = "../../models/network-snapshot.pkl"
STEPS = 600
FPS = 30
FREEZE_STEPS = 30
NUM_STEPS = 1000
SAVE_VIDEO = 0
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"