import tensorflow as tf
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

add_op = a+b+c
session = tf.Session()
res = session.run(add_op)
print(res)

