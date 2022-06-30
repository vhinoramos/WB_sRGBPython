# from flask import Flask, render_template,request

# import cv2
# import os
# from classes import WBsRGB as wb_srgb

# app = Flask(__name__)

# @app.route('/',methods=['GET'])
# def hello_world():
#     return render_template('index.html')

# @app.route('/', methods=['Post'])
# def enhance():
#     imagefile = request.files['imagefile']
#     image_path = "./images/" + imagefile.filename
#     imagefile.save(image_path)
#     images_names = os.listdir(image_path)
#     render_template('index.html', image_name=image_names)


#     return render_template('index.html')

# if __name__ == '__main__':
#        app.run(port=3000, debug=True) 


from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "1234567899"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
