#!/usr/bin/env sh

docker build -t face_detect .
docker run -i -p 5000:5000 -t face_detect
