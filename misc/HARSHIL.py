import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data=keras.datasets.fashion_mnist
#we alwaty=ys want  to split data into training and testing

(train_images,train_labels),(test_images,test_labels)=data.load_data()
"""
    generally we have to write for loops and stuff
    labels of all data are defined and here are between 0 and 9
    create a pre list explaining what each labels actually means


"""
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


#each image is an array of 28x28 pixels
#print(train_images[7])- pixel values for 28v28 array
#print(train_images.shape)60,000 for training
#print(test_images.shape)10,000 for testing

model= keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation="relu"),
        #densely or fully connected neuron layers
        keras.layers.Dense(10,activation="softmax")
        #softmax assignes values to neurons such that their sum is 1 
        #basically givers the probabiltiy
        
        ])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"]
              )
#loss function tells how far off our program is to the real output
#optimizer - modifies the model based on loss funciton and data
#metrics is used to monitor the training and testing steps
#here it uses accuracy the fraction of images predicted correctly


model.fit(train_images,train_labels,epochs=10)
#how many times model will see the information - epochs
#order of images influences the network
test_loss,test_acc=model.evaluate(test_images,test_labels)

print("Tested acc: ", test_acc)


