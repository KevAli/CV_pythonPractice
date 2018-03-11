import tensorflow as tf

with tf.variable_scope('foo') as foo_scope:
    # v = tf.get_variable("v", [1])
    assert foo_scope.name == "foo"

with tf.variable_scope("bar"):
    with tf.variable_scope("baz") as other_scope:
        assert other_scope.name == "bar/baz"
        with tf.variable_scope(foo_scope) as foo_scape2:
            assert foo_scape2.name == "foo"
