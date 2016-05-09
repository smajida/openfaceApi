#!/bin/env python

import requests
import os
import json
import cv2

class OpenFaceClient:
    def __init__(self, url = "http://192.168.99.100:5000"):
        self.url = url


    def read_image(self, imgPath):
        bgrImg = cv2.imread(imgPath)
        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
        fltImg = rgbImg.flatten().tolist()
        return fltImg, rgbImg.shape


    def check_status(self):
        cmd = self.url + "/api/health"
        r = requests.post(cmd)
        r.raise_for_status()
        return r.json()


    def get_face_bb(self, imgPath):
        cmd = self.url + "/api/bbox"
        fltImg, dim = self.read_image(imgPath)
        payload = {'image': fltImg, 'dim': dim}
        r = requests.post(cmd, json=payload, headers= {})
        r.raise_for_status()
        return r.json()
