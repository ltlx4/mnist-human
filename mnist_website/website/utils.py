import numpy as np
from PIL import Image
import random
from keras.datasets import mnist


def generate_sample(arr, arr2):
    two_d = (np.reshape(arr, (28, 28)) * 255).astype(np.uint8)
    img = Image.fromarray(two_d, 'L')
    return img, arr2


def shuffle_samples():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    images = x_train
    labels = y_train
    images_with_labels = list(zip(images,labels))
    random.shuffle(images_with_labels)
    return images_with_labels[:10]