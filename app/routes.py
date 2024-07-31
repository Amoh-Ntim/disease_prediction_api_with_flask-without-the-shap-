# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 19:24:37 2024

@author: user
"""

from flask import Blueprint, request, jsonify
from .predict import predict_diabetes, predict_heart_disease, predict_kidney_disease, predict_liver_disease

api = Blueprint('api', __name__)

@api.route('/predict_diabetes', methods=['POST'])
def diabetes_prediction():
    data = request.json
    prediction, probability = predict_diabetes(data)
    return jsonify({
        'prediction': 'Diabetic' if prediction == 1 else 'Non-Diabetic',
        'probability': probability
    })

@api.route('/predict_heart_disease', methods=['POST'])
def heart_disease_prediction():
    data = request.json
    prediction, probability = predict_heart_disease(data)
    return jsonify({
        'prediction': 'Heart Disease' if prediction == 1 else 'No Heart Disease',
        'probability': probability
    })

@api.route('/predict_kidney_disease', methods=['POST'])
def kidney_disease_prediction():
    data = request.json
    prediction, probability = predict_kidney_disease(data)
    return jsonify({
        'prediction': 'Chronic Kidney Disease (CKD)' if prediction == 1 else 'Non-CKD',
        'probability': probability
    })

@api.route('/predict_liver_disease', methods=['POST'])
def liver_disease_prediction():
    data = request.json
    prediction, probability = predict_liver_disease(data)
    return jsonify({
        'prediction': 'Liver Disease' if prediction == 1 else 'No Liver Disease',
        'probability': probability
    })
