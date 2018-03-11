import tensorflow as tf

q = tf.FIFOQueue(1000, "float")
counter = tf.Variable(0.0)
increment_op = tf.assign_add(counter, tf.constant(1.0))
enqueue_op = q.enqueue(counter)

qr = tf.train.QueueRunner(q, enqueue_ops=[increment_op, enqueue_op] * 1)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

coord = tf.train.Coordinator()

enqueue_thread = qr.create_threads(sess, coord=coord, start=True)

for i in range(0, 10):
    try:
        print(sess.run(q.dequeue()))
    except tf.errors.OutOfRangeError:
        break
coord.request_stop()
coord.join(enqueue_thread)
