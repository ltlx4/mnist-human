import numpy as np
from PIL import Image
import io
import random
from mnist import MNIST


def get_sample(image_arr, label_arr):
    two_d = (np.reshape(image_arr, (28, 28)) * 255).astype(np.uint8)
    img = Image.fromarray(two_d, 'L')
      
    return (img, label_arr)


def shuffle_samples():
    mnist = MNIST('static/website/mnist')
    random.shuffle(mnist)
    image, label = mnist.load_testing()
    
    return image[:20],label[:20]

