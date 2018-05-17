from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics

from keras.models import Sequential
from keras.layers import Activation, Dropout,Dense
from keras.wrappers.scikit_learn import KerasClassifier 
from keras.utils import np_utils

import json
import numpy as np
jsonFile = json.load(open('data.json'))
wordsFile = json.load(open('words.json'))
max_words = wordsFile["MAX"]

def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(6))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])
    return model

X = jsonFile["X"]
Y = jsonFile["Y"]

trainData, testData, trainLabel, testLabel = train_test_split(X,Y)
Y_train = np_utils.to_categorical(trainLabel,6)
model = KerasClassifier(
        build_fn = build_model,
        nb_epoch = 30,
        batch_size =64
        )
model.fit(np.array(trainData),np.array(trainLabel))
y = model.predict(np.array(testData))
ac_score = metrics.classification_report(np.array(y),np.array(testLabel))
report = metrics.accuracy_score(np.array(y),np.array(testLabel))

print(ac_score)
print(report)
