import os
import cv2
from classes import WBsRGB as wb_srgb
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		return render_template('index.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
    
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


in_img = '../example_images/figure3.jpg' 
out_dir = '.'
upgraded_model = 0
gamut_mapping = 2
imshow = 1 
wbModel = wb_srgb.WBsRGB(gamut_mapping=gamut_mapping, upgraded=upgraded_model)
os.makedirs(out_dir, exist_ok=True)
I = cv2.imread(in_img)  # read the image
outImg = wbModel.correctImage(I)  # white balance it
cv2.imwrite(out_dir + '/static/uploads/' + 'result.jpg', outImg * 255)  # save it


# @app.route('/display/<filename>')
# def display_image(filename):
# #print('display_image filename: ' + filename)
#     in_img = '../example_images/figure3.jpg' 
#     out_dir = '.'
#     upgraded_model = 0
#     gamut_mapping = 2
#     imshow = 1 
#     wbModel = wb_srgb.WBsRGB(gamut_mapping=gamut_mapping, upgraded=upgraded_model)
#     os.makedirs(out_dir, exist_ok=True)
#     I = cv2.imread(in_img)  # read the image
#     outImg = wbModel.correctImage(I)  # white balance it
#     cv2.imwrite(out_dir + '/' + 'result.jpg', outImg * 255)  # save it

#     return 0

if __name__ == "__main__":
    app.run()