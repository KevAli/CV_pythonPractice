import tensorflow as tf

a = tf.constant([1.0, 2.0])
b = tf.constant([3.0, 4.0])
c = a * b

sess = tf.Session()

print sess.run(c)
sess.close()
