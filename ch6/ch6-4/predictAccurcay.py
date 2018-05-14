from keras.models import Sequential 
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import model_selection,metrics 
import json
import numpy as np
filepath = "./newsData/shData.json"
word_dict = json.load(open(filepath,'r'))

max_words = 6800
nb_classes = 6

batch_size = 64
nb_epoch = 20

def build_model():
    model = Sequential()
    model.add(Dense(512,input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])
    return model

X = word_dict["X"]
Y = word_dict["Y"]
X_train, X_test,Y_train,Y_test = train_test_split(X,Y)
Y_train = np_utils.to_categorical(Y_train, nb_classes)
model = KerasClassifier(
        build_fn = build_model,
        nb_epoch=nb_epoch,
        batch_size=batch_size)
model.fit(np.array(X_train),np.array(Y_train))

y = model.predict(np.array(X_test))
ac_score = metrics.accuracy_score(np.array(Y_test),np.array(y))
cl_report = metrics.classification_report(np.array(Y_test),np.array(y))
print(ac_score)
print(cl_report)
