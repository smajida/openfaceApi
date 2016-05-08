#!/bin/env python

import requests
import os
import json
import cv2

def get_face_bb(imgPath):
    url = "http://192.168.99.100:5000/api/score"
    bgrImg = cv2.imread(imgPath)
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    payload = {'image': rgbImg.flatten().tolist(), 'dim': rgbImg.shape}
    r = requests.post(url, json=payload, headers= {})
    r.raise_for_status()
    return r.json()


print(get_face_bb("test_img/royal.jpg"))
print(get_face_bb("test_img/clapton.jpg"))
print(get_face_bb("test_img/family.jpg"))