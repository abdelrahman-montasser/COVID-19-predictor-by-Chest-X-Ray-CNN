import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

from predict import diagnosis
UPLOAD_FOLDER = 'C:\\Users\\dell\\Desktop\\x-ray\\UP\\'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER










@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    image = request.files['file']
   
    filename=image.name
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result = diagnosis(image)
    
    if result=='Covid':
        return render_template('index.html', prediction_text='HIgh Risk of COVID-19 ☹ ')
    elif result=='Viral Pneumonia':
        return render_template('index.html', prediction_text='Just HIgh Risk of Viral Pneumonia ')
    elif result=='Normal':
        return render_template('index.html', prediction_text='NO Risk of COVID-19 😀')
    #return render_template('index.html', prediction_text=' {}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)

