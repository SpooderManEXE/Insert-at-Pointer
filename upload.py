# -*- coding: utf-8 -*-
import os
import screenpoint
import cv2
import pyscreenshot
import numpy as np
from flask import Flask, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import pointer

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'],name='temp.jpg')
        file_url = photos.url(filename)
        image = cv2.imread("temp.jpg", 1)
        half = cv2.resize(image, (0, 0), fx = 0.05, fy = 0.05)
        screen = pyscreenshot.grab()
        cv2.imwrite('view.jpg',image)
        cv2.imwrite('temp.png',np.array(screen))
        os.remove("temp.jpg")
        x,y=pointer.show('ubi.png')
        os.remove("temp.png")
        os.remove("view.jpg")
        return html + '<br>'+str(x)+' : '+str(y)
    return html

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)