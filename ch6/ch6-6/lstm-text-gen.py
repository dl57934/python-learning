from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys


fp = open("./BEXX0003.txt",'r',encoding ='utf-16')
bsData = BeautifulSoup(fp.read(),'html.parser')
body = bsData.select_one('body > text')
text= body.getText()+" "
chars = sorted(list(set(text)))
print(chars)
char_indices = dict((c,i) for i,c in enumerate(chars))
indices_char = dict((i,c) for i,c in enumerate(chars))

maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0,len(text) -maxlen,step):
    sentences.append(text[i:i + mexlen])
    next_chars(text[i+mexlen])
X = np.zeros((len(sentences), maxlen,len(chars)),dtype=np.bool)
Y = np.zeros((len(sentences),len(chars)),dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t,char in enumerate(sentence):
        X[i,t,char_indices[char]] = 1
    Y[i,char_indices[next_chars[i]]] = 1

print('모델을 구축합니다....')

model = Sequential()
model.add(LSTM(128,input_shape=(maxlen,len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy',optimizer=optimizer)

def sample(preds,temperature=1.0):
    preds = np.
