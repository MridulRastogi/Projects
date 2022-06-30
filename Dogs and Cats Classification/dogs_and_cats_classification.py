import tensorflow as tf
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

cnn = Sequential()                  ### Creating Object

cnn.add(Convolution2D(32,3,3, input_shape = (64,64,3), activation = 'relu'))        ### Adding First Layer for Convolution

cnn.add(MaxPooling2D(pool_size = (2,2)))                                            ### Max Pooling (Reducing the size of feature map)

cnn.add(Convolution2D(32,3,3, activation = 'relu'))                                 ### Adding Second Convolutional Layer
cnn.add(MaxPooling2D(pool_size = (2,2)))                        

cnn.add(Flatten())                                                                  ### Flattening

cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))                        ### Establishing Full Connection
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

opt = tf.keras.optimizers.Adam(learning_rate=0.0001)

cnn.compile(optimizer = opt, loss = 'binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator                            ### Image Data Generator
                                                                                    ### To Prevent from Overfitting

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_datagen.flow_from_directory('training_set/',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('test_set/',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

cnn.fit(x = training_set, validation_data = test_set, epochs = 5)

import numpy as np
from keras.preprocessing import image

test_image = tf.keras.utils.load_img('single_prediction/cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
  prediction = 'dog'
else:
  prediction = 'cat'
  
print(prediction)