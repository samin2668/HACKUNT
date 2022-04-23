import os
import tensorflow as tf
from tensorflow.python.keras import layers
from tensorflow.python.keras import Model
from flask import Flask, request
import cv2
import json
import numpy as np
from flask_cors import CORS
from tensorflow.python.keras.backend import set_session
import base64
from datetime import datetime

graph = tf.compat.v1.get_default_graph()

app = Flask(__name__)
CORS(app)
sess = tf.compat.v1.Session()
set_session(sess)

model = tf.keras.models.load_model('facenet_keras.h5')


def encode_img(path, model):
    

