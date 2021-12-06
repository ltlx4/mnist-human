import base64
import numpy as np
from PIL import Image
from .models import User    
import io
import random
from mnist import MNIST




def get_sample():
    image_arr, label_arr = shuffle_samples()
    two_d = (np.reshape(image_arr, (28, 28)) * 255).astype(np.uint8)
    img = Image.fromarray(two_d, 'L')

    img = img.resize((150, 150), Image.ANTIALIAS)
    buffer = io.BytesIO()
    img.save(buffer, 'PNG')
    img_str = base64.b64encode(buffer.getvalue())
    
    img_str = img_str.decode('ascii')
    return img_str, label_arr


def shuffle_samples():
    mnist = MNIST('static/website/mnist')
    # random.shuffle(mnist)
    image, label = mnist.load_testing()
    samples_list = list(zip(image, label))
    random.shuffle(samples_list)
    image, label = zip(*samples_list)
    return image[0],label[0]
    

def username_exists(username):
    return User.objects.filter(username=username).exists()


def correct_guess(val1, val2):
    return val1 == val2
    

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

