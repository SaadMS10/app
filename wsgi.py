# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:46:29 2020

@author: SAAD
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/exec')
def parse(name=None):
    import recognize
    print("done")
    return render_template('index.html',name=name)
  
if __name__ == "__main__": 
        app.run()
app.debug = True