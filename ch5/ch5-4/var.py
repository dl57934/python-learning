import tensorflow as tf

# 텐서플로우에서 변수를 표현하는 방법
#1. 상수 정의하기
a = tf.constant(120,name = 'a')
b = tf.constant(130,name = 'b')
c = tf.constant(140,name = 'c')

#2. 변수 정의하기
v = tf.Variable(0,name = "v")

calc_op = a+b+c
assign_op = tf.assign(v,calc_op)

sess = tf.Session()
sess.run(assign_op)

print(sess.run(v))

