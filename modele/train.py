import numpy as np
import json
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.ops.numpy_ops import np_config

if __name__ == '__main__':
    np_config.enable_numpy_behavior()

    with open('cleanDataset/DataFEATURES0.json', 'r') as datasets:
        string = json.load(datasets)
        featureSet = json.loads(string)
        string = ''

    with open('cleanDataset/DataCLASSES0.json', 'r') as datasets:
        string = json.load(datasets)
        classesSet = json.loads(string)
        string = ''

    featureSet = np.array(featureSet)
    print(len(featureSet))
    featureSet = tf.reshape(featureSet, [len(featureSet), 15000, 3, 1])
    classesSet = np.array(classesSet)
    print(featureSet.shape)

    model = keras.models.Sequential()

    model.add(keras.layers.MaxPooling2D((2, 2), input_shape=(15000, 3, 1)))

    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu', padding='same', input_shape=(15000, 3, 1)))
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu', padding='same', input_shape=(15000, 3, 1)))
    model.add(keras.layers.Conv2D(64, (2, 2), activation='relu', padding='same', input_shape=(15000, 3, 1)))
    model.add(keras.layers.Conv2D(64, (2, 2), activation='relu', padding='same', input_shape=(15000, 3, 1)))
    model.add(keras.layers.Conv2D(64, (2, 2), activation='relu', padding='same', input_shape=(15000, 3, 1)))

    model.add(keras.layers.Flatten())

    model.build()

    model.summary()

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(featureSet, classesSet,
                        epochs=100,
                        verbose=1)
