import tensorflow as tf 
#32bit 정수형태로 3개 저장 
#placeholder는 선언만 해주는 그릇일 뿐 이다.
a = tf.placeholder(tf.int32, [3])

b = tf.constant(2)
x2_op = a*b

sess = tf.Session()

r1 = sess.run(x2_op, feed_dict={a:[1,2,3]})
print(r1)
r2 = sess.run(x2_op, feed_dict={a:[10,20,10]})
print(r2)
