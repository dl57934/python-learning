import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("mnist/",one_hot=True)
pixels = 28*28
nums = 10

x = tf.placeholder(tf.float32,[None,pixels],name = "x")
answery = tf.placeholder(tf.float32,[None,nums], name="y")

def weight_variable(name,shape):
    W_init = tf.truncated_normal(shape,stddev=0.1)
    W = tf.Variable(W_init)
    return W

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding="SAME")


def max_pool(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],stridges=[1,2,2,1],padding="SAME")



