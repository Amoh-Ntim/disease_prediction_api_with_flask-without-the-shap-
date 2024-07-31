# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 19:24:03 2024

@author: user
"""

import os
from pycaret.classification import load_model, predict_model
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))

# Load models
diabetes_model = load_model(os.path.join(base_dir, '../models/diabetes_prediction_model'))
heart_model = load_model(os.path.join(base_dir, '../models/best_heart_disease_model'))
kidney_model = load_model(os.path.join(base_dir, '../models/best_kidney_disease_model'))
liver_model = load_model(os.path.join(base_dir, '../models/best_liver_disease_model'))

def predict_diabetes(data):
    df = pd.DataFrame([data])
    prediction = predict_model(diabetes_model, data=df)
    return int(prediction['prediction_label'][0]), float(prediction['prediction_score'][0])

def predict_heart_disease(data):
    df = pd.DataFrame([data])
    prediction = predict_model(heart_model, data=df)
    return int(prediction['prediction_label'][0]), float(prediction['prediction_score'][0])

def predict_kidney_disease(data):
    df = pd.DataFrame([data])
    prediction = predict_model(kidney_model, data=df)
    return int(prediction['prediction_label'][0]), float(prediction['prediction_score'][0])

def predict_liver_disease(data):
    df = pd.DataFrame([data])
    prediction = predict_model(liver_model, data=df)
    return int(prediction['prediction_label'][0]), float(prediction['prediction_score'][0])
