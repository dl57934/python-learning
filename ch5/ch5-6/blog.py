import tensorflow as tf

v = tf.Variable(0,tf.int32,name="v")

a = tf.constant(30,name="a")
b = tf.constant(60,name="b")
k = tf.constant(70,name="k")

add_mul_op = a*b+k

sess = tf.Session()
tw = tf.summary.FileWriter('log-dir', graph = sess.graph)
assign_op=tf.assign(v,add_mul_op)
sess.run(assign_op)
print(sess.run(v))

