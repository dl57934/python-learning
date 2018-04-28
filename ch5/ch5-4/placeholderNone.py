import tensorflow as tf

a = tf.placeholder(tf.int32, None)
b = tf.constant(3)
add_op = a*b

sess = tf.Session()

r1 = sess.run(add_op, feed_dict={a:[10,20,30,40,50]})
print(r1)
r2 = sess.run(add_op, feed_dict={a:[10,30,50]})
print(r2)
