import tensorflow as tf
import numpy as np
import pandas as pd


csv = pd.read_csv("bmi.csv")
csv["height"] = csv["height"].apply(lambda x : x/200)
csv["weight"] = csv["weight"].apply(lambda x : x/100)



onehotLabel = {"thin":[1,0,0],"normal":[0,1,0],"fat":[0,0,1]}

csv["label_pat"] = csv["label"].apply(lambda x : np.array(onehotLabel[x]))

testcsv = csv[15000:20000]
testX = testcsv[["height","weight"]]
testY = list(testcsv["label_pat"])

#변수 선언
x = tf.placeholder(tf.float32,[None,2],name = "x")
realY = tf.placeholder(tf.float32,[None,3],name="realY")


W = tf.Variable(tf.zeros([2,3]),name="W")
b = tf.Variable(tf.zeros([3]),name="b")


predictY = tf.nn.softmax(tf.matmul(x,W)+b)

cross_validation = - tf.reduce_sum(realY*tf.log(predictY))
optimizer = tf.train.GradientDescentOptimizer(0.03)
train = optimizer.minimize(cross_validation)

predict = tf.equal(tf.argmax(predictY,1),tf.argmax(realY,1))
accuracy = tf.reduce_mean(tf.cast(predict,tf.float32))


sess =tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(3500):
    i = (step*100)%15000
    trainCsv = csv[i+1:i+100]
    xdata = trainCsv[["height","weight"]]
    ydata = list(trainCsv["label_pat"])
    sess.run(train,feed_dict={x:xdata,realY:ydata})
    if step%700 == 0:
        acc = sess.run(accuracy,feed_dict = {x:testX,realY:testY})
        print("step=> ",step,"acc=> ",acc)

