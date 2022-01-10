# TODO Remove this mock transformer before merging
import shutil
import time

from typing import *

def filler(str, req):
    return '0' * (req - len(str)) + str

def transform(image) -> Tuple[bool, object]:
    temp_filepath = 'temp/finalVideo.mp4'
    shutil.copyfile('sample/sample1.mp4', temp_filepath)
    # time.sleep(5) # Added to imitate the real behaviour
    return True, temp_filepath
