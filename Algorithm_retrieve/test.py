from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf 
import numpy as np 
import cv2
import os
import random

path_digits2='Basedata/digits/2/21.png'
path_digits6='Basedata/digits/6/61.png'


img = image.load_img("Basedata/training/pattern1/A1.jpg")


plt.imshow(img)
cv2.imread("Basedata/training/pattern1/A1.jpg").shape


training = ImageDataGenerator(rescale=1/255)
validation= ImageDataGenerator(rescale=1/255)

train_dataset = training.flow_from_directory('Basedata/training/', target_size =(200,200),batch_size= 3, class_mode = 'binary')

validation_dataset = training.flow_from_directory('Basedata/validation/', target_size =(200,200),batch_size= 3, class_mode = 'binary')

print(train_dataset.class_indices)
print(train_dataset.classes)

model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3),activation='relu',input_shape=(200,200,3)),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    ##
                                    tf.keras.layers.Flatten(),
                                    ##
                                    tf.keras.layers.Dense(512,activation='relu'),
                                    ##
                                    tf.keras.layers.Dense(1,activation='sigmoid')
                                    ])

model.compile(loss='binary_crossentropy',
            optimizer = RMSprop(lr=0.001),
            metrics =['accuracy'])

model_fit = model.fit(train_dataset,
                    steps_per_epoch = 3,
                    epochs= 20,
                    validation_data= validation_dataset)


dir_path = 'Basedata/testing'

for i in os.listdir(dir_path):
    img = image.load_img(dir_path+'//'+ i,target_size=(200,200,3))
    plt.imshow(img)
    plt.show()

    x=image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    images=np.vstack([x])
    val = model.predict(images)
    if val == 0:
        print("Speckle pattern - digit 2")
        digit2=image.load_img(path_digits2)
        plt.imshow(digit2)
        plt.show()
    else:
        print("Speckle pattern - digit 6")
        digit6=image.load_img(path_digits6)
        plt.imshow(digit6)
        plt.show()
print("EXIT")
plt.show()
