# Solution is available in the "solution.ipynb"
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = tf.constant(10) #10
y = tf.constant(2) #2
z = tf.subtract(tf.divide(x,y), tf.constant(1, tf.float64))  #x/y - 1

# TODO: Print z from a session as the variable output
#output = None
with tf.Session() as sess:
    output = sess.run(z)


### DON'T MODIFY ANYTHING BELOW ###
### Be sure to run all cells above before running this cell ###
import grader1

try:
    grader1.run_grader(output)
except Exception as err:
    print(str(err))