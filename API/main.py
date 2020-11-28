# way to upload image: endpoint
# way to save the image
# function to make prediction on the image
# show the results
import os
from flask import Flask
from flask import request
from flask import render_template
import cv2
import numpy as np
from keras.models import Model, load_model
from pymongo import MongoClient
import base64
import datetime
import socket
from datetime import date, timedelta
import random


app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MODEL = None

def predict(image_path, model):
    I = []
    img=cv2.imread(image_path)
    img=cv2.resize(img,(100,100))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    I.append(img)
    NP_ARRAY = np.array(I)
    X_VAL = NP_ARRAY/255.0
    R = MODEL.predict_classes(X_VAL)

    
    LABEL=''

    if(R[0]==0):
        LABEL = 'BOA SEM MANCHAS'
    if(R[0]==1):
        LABEL = 'RUIM'
    if(R[0]==2):
        LABEL = 'BOA COM MANCHAS'

    connect_and_save_mongo(LABEL, img)

    return LABEL
    
def connect_and_save_mongo(classification, img):
    
    cliente_prod = MongoClient('mongodb://admin:admin@localhost:27018/orange_classification?authSource=admin')
        
    db_prod   = cliente_prod.orange_classification

    coll_prod = db_prod.oranges

    if (classification == "BOA SEM MANCHAS"):
        label_classification = 'good_spotless'
    if (classification == "RUIM"):
        label_classification = 'bad'
    if (classification == "BOA COM MANCHAS"):
        label_classification = 'good_with_spots'

    orange = { "classification": label_classification, "image":base64.b64encode(img), 'date': datetime.datetime.now() }
    coll_prod.insert(orange)

@app.route("/", methods=["GET", "POST"])
def upload_predict():
    
    teste = []
    if request.method == "POST":
        image_file = request.files.getlist("image")
        
        PRED = []
        for image in image_file:

            if image:
                image_location = os.path.join(
                    UPLOAD_FOLDER,
                    image.filename
                )
                image.save(image_location)
                pred = predict(image_location, MODEL)
                PRED.append(pred)
                teste.append({'url': './static/'+image.filename, 'label': pred})

    FINAL = ''

    return render_template("index.html", image_locs=teste)


if __name__ == "__main__":
    
    MODEL=load_model('../rottenvsfresh.h5')
    
    app.run(host='0.0.0.0', port='5000', debug=True)
