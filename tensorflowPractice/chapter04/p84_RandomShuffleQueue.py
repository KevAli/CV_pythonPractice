import tensorflow as tf

q = tf.RandomShuffleQueue(capacity=10, min_after_dequeue=2, dtypes="float")
sess = tf.Session()
for i in range(0, 10):
    sess.run(q.enqueue(i))

# for i in range(0, 8):
#     print(sess.run(q.dequeue()))

run_options = tf.RunOptions(timeout_in_ms=3000)

try:
    # max dequeue elements is 10-2=8
    for i in range(0, 12):
        print(sess.run(q.dequeue(), options=run_options))


except tf.errors.DeadlineExceededError:
    print("out of range")
