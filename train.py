import matplotlib.pyplot as plt
import numpy as np
import glob
import cv2
from darkflow.net.build import TFNet
import sys


#'model' path to yolo config (all NN architecture defined there)
#'load' path to yolo weights (deserialised pretrained NN)
#'batch' , 'lr' NN's hyperparams
#'annotation' ,'dataset' path to  your images and anotations
options = {"model": "cfg/yolo_custom.cfg",
           "load": "bin/yolo.weights",
           "batch": 8,
           "epoch": 100,
           "lr" : 0.00001,
           "gpu": 1,
           "train": True,
           "annotation": "annotations/",
           "dataset": "images/"}

tfnet = TFNet(options)
tfnet.train()

#save pb format may be used for tensorflow by default unnesseccary
tfnet.savepb()
