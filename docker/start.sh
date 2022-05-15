#!/bin/bash
git clone http://www.github.com/Kevin-Duarte/handgun-detector && cp ./handgun-detector/deepstack-models/best.pt /modelstore/detection
/app/server/server & python ./handgun-detector/main.py

