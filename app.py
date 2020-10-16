import numpy as np
from flask import Flask, request, jsonify, render_template
import gzip, pickle, pickletools


app=Flask(__name__)
with gzip.open('random_forest.pkl','rb') as f:
	p=pickle.Unpickler(f)
	model=p.load()
# model=pickle.load(open('D:\\impact prediction deployment\\Model.pkl','rb'))
# Use pickle to load in the pre-trained model.

@app.route('/')

def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
	int_features=[int(x) for x in request.form.values()]
	final_features=[np.array(int_features)]
	prediction=model.predict(final_features)

	output=prediction

	return render_template('index.html',prediction_text='Impact for given particular incident is $ {}'.format(output))

@app.route('/results',methods=['POST'])

def results():

	data=request.get_json(force=True)
	prediction=model.predict([np.array(list(data.values()))])

	output=prediction[0]
	return jasonify(output)

if __name__ =='main':
	app.run(debug=True)
