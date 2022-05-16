#!/bin/bash
git clone http://www.github.com/Kevin-Duarte/handgun-detector /handgun-detector && cp /handgun-detector/docker/deepstack-models/best.pt /modelstore/detection;
/app/server/server & python /handgun-detector/main.py

