
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

import json


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/banner', methods=['post', 'get'])
@cross_origin(origin='*')
def upload_banner():
    img = request.files["_"]
    #basedir = os.path.dirname(__file__)
    #upload_path = os.path.join(basedir, 'img')
    img.save('static/img/_.png')
    #res = make_response(img)
    #res.headers['Access-Control-Allow-Origin'] = '*'
    #res.headers['Access-Control-Allow-Methods'] = 'POST，GET,OPTIONS'
    #res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return ('', 204)


@app.route('/_', methods=['post', 'get'])
@cross_origin(origin='*')
def _():
    label = json.loads(request.form.get('_'))
    with open('_/_.txt', 'w') as fp:
        json.dump(_, fp)
    return ('', 204)


@app.route('/__', methods=['post', 'get'])
@cross_origin(origin='*')
def _():

    _ = request.files["__img"]
    file_read = open("_/_.txt", "r")
   __ = 'slide' + file_read.read() + '.png'
    slide_img.save('_/' +__)
    return ('', 204)


@app.route('/__', methods=['post', 'get'])
@cross_origin(origin='*')
def __():
    #slogan = request.form.get('_')
    slogan = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        #json.dump(__, fp)
        fp.write(__)
    #res = make_response(slogan)
    #res.headers['Access-Control-Allow-Origin'] = '*'
    #res.headers['Access-Control-Allow-Methods'] = 'POST，GET,OPTIONS'
    #res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return __


@app.route('/__', methods=['post', 'get'])
@cross_origin(origin='*')
def __():
    #slogan = request.form.get('_')
    slogan = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        json.dump(_, fp)
    return ('', 204)


@app.route('/__', methods=['post'])
@cross_origin(origin='*')
def _():
    #_ = request.form.get('_')
   _ = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        json.dump(_, fp)
    return ('', 204)


@app.route('/__', methods=['post'])
@cross_origin(origin='*')
def __():
    #_ = request.form.get('_')
    _ = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        json.dump(__, fp)
    return ('', 204)


@app.route('/__', methods=['post'])
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return read__


@app.route('/_')
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return jsonify(read__)


@app.route('/_')
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return jsonify(read___)


@app.route('/__')
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return jsonify(read___) 


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('info')
    with open('_/__.txt', 'w') as ffp:
        ffp.write(info)
	#res = make_response(_)
    return__


@app.route('/_, methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        fp.write(_)
    return _


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        fp.write(_)
    return _


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        fp.write(_)
    return_


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        fp.write(_)
    return _


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        fp.write(_)
    return _


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('__')
    with open('_/__.txt', 'w') as fp:
        fp.write(_)
    return _


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    info = request.form.get('_')
    with open('_/__.txt', 'w') as fp:
        fp.write(_)
    return _


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    img = request.files["_"]
    img.save('_/__.png')
    return ('', 204)


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    img = request.files["_"]
    img.save('_/__.png')
    return ('', 204)


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return  read__
	
	
@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return read__
	
	
@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def _():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return read__


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    readf = open("_/_.txt", "r")
    read__ = readf.read()
    readf.close()
    return read__
	

@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    readf = open("_/_.txt", "r")
    read__ = readf.read()
    readf.close()
    return read__


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__= readf.read()
    readf.close()
    return read__


@app.route('/__', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return read__


@app.route('/_', methods=['POST', 'GET'])
@cross_origin(origin='*')
def __():
    readf = open("_/__.txt", "r")
    read__ = readf.read()
    readf.close()
    return read__

	
@app.route('/_')
@cross_origin(origin='*')
def__():
    imgid = request.args.get('data')
    if imgid == '_':
        path = ['_.png']
        return jsonify(path)
    if imgid == '_':
        path = ['_1.png']
        return jsonify(path)
    if imgid == '_2':
        path = ['_2.png']
        return jsonify(path)
    if imgid == '_3':
        path = ['_3.png']
        return jsonify(path)
    if imgid == '_':
        path = [_.png']
        return jsonify(path)
    if imgid == '_':
        path = ['_.png']
        return jsonify(path)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug='True')