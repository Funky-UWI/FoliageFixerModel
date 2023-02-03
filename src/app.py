import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

import pathlib

import os

data_dir = pathlib.Path('plantvillage')

folders = os.listdir(data_dir)

# for folder in folders:
#     dir = pathlib.Path('plantvillage/'+folder)
#     print(   len(list(dir.glob('*.JPG')))  )

bacterial_spot = list(data_dir.glob('Tomato___Bacterial_spot/*'))

img = np.array(PIL.Image.open(bacterial_spot[0]))
print(img.shape)
