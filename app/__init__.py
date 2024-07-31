# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 19:24:21 2024

@author: user
"""

from flask import Flask
from .routes import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    return app
