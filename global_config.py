import os
import re
import requests
from subprocess import REALTIME_PRIORITY_CLASS
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address



ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
DEEPSTACK_QUERY_URL = "http://localhost:90/v1/vision/custom/best"

app = Flask(__name__, template_folder='template')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000 #16 megabytes max upload 
app.config['SECRET_KEY'] = 'longandsecret'
app.config['TEMPLATES_AUTO_RELOAD'] = True

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=['2 per second']
)


