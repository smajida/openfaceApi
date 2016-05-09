#!/bin/env python

from openface_client import OpenFaceClient

ofc = OpenFaceClient()

ofc.check_status())
ofc.get_face_bb("test_img/royal.jpg")
ofc.get_face_bb("test_img/clapton.jpg")
ofc.get_face_bb("test_img/family.jpg")
ofc.get_face_bb("test_img/students.jpg")
