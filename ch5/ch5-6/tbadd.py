import tensorflow as tf

a = tf.constant(20,name="a")
b = tf.constant(30,name="b")
c = tf.constant(40,name="c")
v = tf.Variable(0,name="v")

Sum = a+b*c
assign_op = tf.assign(v,Sum)


sess = tf.Session()

tw = tf.summary.FileWriter("log_dir",graph=sess.graph)

sess.run(assign_op)

print(sess.run(v))

