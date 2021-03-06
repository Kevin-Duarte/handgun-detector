from flask import render_template, request
from global_config import *
from api_anon import api_anon
from waitress import serve


# Importing restful APIs
app.register_blueprint(api_anon)

@app.route('/more-information', methods=['GET', 'POST'])
def more_information():
  return render_template('more-information.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if (__name__) == '__main__':
    #app.run(host='0.0.0.0', debug=False, port=80)
    serve(app, host='0.0.0.0', port=80)


