---
layout: post
title:  "Freezing a TensorFlow graph to a protobuf file"
date:   2018-12-01 00:00:00 -0500
published: false
categories: Tensorflow
---

When it comes to serving your neural network with TensorFlow, training time is usually over and all you want is to pack everything neat and tidy in a file for future usage. While metagraphs and checkpoints files allow you to do something along these lines, it is still just a little bit too complex when you just want to input your data and get an output as painlessly as possible. While using TF, I found the exportation to a protobuf file to be one of the easiest and most portable way to save my neural networks. So here is how to do just that with a relatively easy template that works for all versions of TensorFlow.

```py
import tensorflow as tf

with tf.Session() as sess:
  #
  # Define/Train/Test your model here
  #

  with open('path/to/your/graph.pb', 'wb') as f:
    f.write(
        tf.graph_util.convert_variables_to_constants(
            sess,
            sess.graph.as_graph_def(),
            ['output_node_name']
        ).SerializeToString()
    )

```

Now you should have a `graph.pb` file in your path. Next, simply import it in your next project!

```py
import tensorflow as tf

with tf.Session() as sess:
  graph_def = tf.GraphDef()
  with open('path/to/your/graph.pb', 'rb') as f:
    graph_def.ParseFromString(f.read())
  tf.import_graph_def(graph_def)

  # Do something with your session here.
```

Simple as that!
