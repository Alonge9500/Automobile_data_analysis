from contextlib import redirect_stderr
from flask import render_template, url_for, request, abort,flash,redirect
from webpage.form import PredictionForm
from webpage import app
import secrets
import os
import numpy as np
import pickle



@app.route("/", methods=['GET', 'POST'])
def home():
    form = PredictionForm()
    if form.validate_on_submit():
        
        data = [form.width.data,form.height.data,form.curb_weight.data,form.engine_size.data,form.highway_mpg.data,form.make.data,form.body_style.data,form.drive_wheels.data,form.engine_location.data,form.engine_type_dict.data]
        data = [int(dat) for dat in data]

        data = np.array(data)
        data = data.reshape(1,-1)
        filename = 'car_price_predictor.pkl'
        model = pickle.load(open(filename, 'rb'))
        print(model)
        pred = model.predict(data)[0]
        print(model)
        pree = 'jshhsh'
        print(pred)
        
        return redirect(url_for('predict',pred=pree))
    
    return render_template('home.html',form=form)


@app.route("/predict/<pred>",methods=['GET','POST'])
def predict(pred):
    return render_template('result.html',pred=pred)