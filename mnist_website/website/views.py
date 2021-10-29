from django.shortcuts import render 
from keras.datasets import mnist


def home(request):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print('X_train: ' + str(x_train.shape))
    print('Y_train: ' + str(y_train.shape))
    print('X_test:  '  + str(x_test.shape))
    print('Y_test:  '  + str(y_test.shape))
    return render(request, 'website/index.html')