import pandas as pd
import numpy as np
import tensorflow as tf

#파일 읽어오기
csv = pd.read_csv('bmi.csv')

#정규화 하기
csv["height"] = csv["height"]/200
csv["weight"] = csv["weight"]/100
# 레이블을 배열로 변환하기

bclass = {"thin":[1,0,0], "normal":[0,1,0], "fat":[0,0,1]}
csv['label_pat'] = csv['label'].apply(lambda x :np.array(bclass[x]))

test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

x = tf.placeholder(tf.float32,[None,2])
y_ = tf.placeholder(tf.float32,[None,3])

#가중치 정의
W = tf.Variable(tf.zeros([2,3]));
#y인자 정의
b = tf.Variable(tf.zeros([3]));

#softmax 회귀 정의
y = tf.nn.softmax(tf.matmul(x,W)+b)

#오차함수 사용 y->예상레이블 y_ -> 정답레이블
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
#경사 하강법 학습률 0.01 매개변수 자동으로 구해줌 
optimizer = tf.train.GradientDescentOptimizer(0.03)
#오차함수가 최소로 되게 만들어 준다. 
train = optimizer.minimize(cross_entropy)

#예측과 같은지 판단 
predict = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
#1
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(3500):
#i = 100->200->300->400->500
    i = (step*100) %15000
    #모델 100개씩 훈련
    rows = csv[1+i:i+1+100]

    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x:x_pat, y_:y_ans}
    #최소 매개변수를 찾으려고 실행시킴
    sess.run(train, feed_dict=fd)
    if step % 500 == 0:
        #500번일때 마다 데이터를 집어넣어서 오차함수 실행
        acc = sess.run(accuracy, feed_dict={x:test_pat,y_:test_ans})
        print("step=",step,"acc=",acc)

acc = sess.run(accuracy,feed_dict={x:test_pat,y_:test_ans})

print(acc)
