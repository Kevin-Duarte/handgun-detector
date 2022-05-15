from ast import Bytes
from xml.etree.ElementTree import tostring
from flask import Blueprint
from numpy import byte
from global_config import *
from PIL import Image
from io import BytesIO

api_anon = Blueprint('api_anon', __name__)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api_anon.route('/anon/gun-check', methods=['POST'])
@limiter.limit("2 per second")
def gun_check():
    try:
        image = request.files['image']
        
        if image and allowed_file(image.filename):
            image_converted = Image.open(image.stream).convert('L')
            image_bytes = BytesIO()
            image_converted.save(image_bytes, 'png')
            image_bytes.seek(0)
            
            response = requests.post(DEEPSTACK_QUERY_URL,files={"image":image_bytes}).json()
            print(response)
            for object in response["predictions"]:
                    if object['label'] == 'gun':
                        return jsonify(detection = 'true', confidence=object['confidence'])
            return jsonify(detection = 'false', confidence= '0')
        return jsonify(message='Error, please ensure your image file is valid.')
    except Exception as e:
        return jsonify(message='Error, could not process this transaction: ' + tostring(e))
