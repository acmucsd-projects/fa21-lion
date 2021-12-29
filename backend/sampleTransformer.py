# TODO Remove this mock transformer before merging

import random

from typing import *

def filler(str, req):
    return '0' * (req - len(str)) + str

def transform(image) -> Tuple[bool, object]:
    filename = f'{filler(str(random.randint(5000, 5050)), 5)}.png'
    return True, open(f'sampleImages/{filename}', 'rb')
