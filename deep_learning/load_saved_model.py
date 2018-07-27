import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

input_ckpt = './model.ckpt'
input_pb = './frozen_inference_graph.pb'

# load checkpoint file
graph1 = tf.Graph()
with tf.Session() as sess:
    saver = tf.train.import_meta_graph(input_ckpt+'.meta',clear_devices=True)
    saver.restore(sess,input_ckpt)
    graph1 = tf.get_default_graph()

# load pb file
graph2 = tf.Graph()
with tf.Session() as sess:
    graph_def = tf.GraphDef()
    with tf.gfile.GFile(input_pb,'rb') as f:
        graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def)
    graph2 = tf.get_default_graph()