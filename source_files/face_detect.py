import os
import json

import openface

import numpy as np

class face_detector:

    def __init__(self):
        self.align = openface.AlignDlib("/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat")
        #self.net = openface.TorchNeuralNet("/root/openface/models/openface/nn4.small2.def.lua", 1200)


    def convert_to_array(self, vals, dim):
        return np.array(vals, np.dtype('uint8')).reshape(dim)


    def score_img(self, vals, dim):
        rgbImg = self.convert_to_array(vals, dim)
        bb = self.align.getAllFaceBoundingBoxes(rgbImg)
        rects = [[x.top(), x.bottom(), x.left(), x.right()] for x in bb]
        return {"rects": rects}








