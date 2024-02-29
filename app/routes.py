from flask import render_template, request
from flask_mail import Message
import pickle
import numpy as np
from app import mail, app

model = pickle.load(open('app/serialized/model.pkl', 'rb'))
model1 = pickle.load(open('app/serialized/model1.pkl', 'rb'))
model2 = pickle.load(open('app/serialized/model2.pkl', 'rb'))
model3 = pickle.load(open('app/serialized/model3.pkl', 'rb'))


@app.route('/email', methods=['POST', 'GET'])
def mailing():
    email = request.form['Email']
    msg = Message('ANALYTICA RESPONSE', sender='analyticaesprit@gmail.com', recipients=[email])
    msg.body = "Your email has been sent successfully, we are doing our best to respond your demand as soon as possible!"
    mail.send(msg)
    return render_template('index.html')


@app.route('/dash')
def dash():
    """Renders a sample page."""
    return render_template('dash.html')


@app.route('/template.html')
def hello():
    """Renders a sample page."""
    return render_template('template.html')


@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('index.html')


@app.route('/template1.html')
def desc():
    """Renders a sample page."""
    return render_template('template1.html')


@app.route('/predictobese', methods=['POST', 'GET'])
def predict():
    int_features = [x for x in request.form.values()]
    lastElementIndex = len(int_features) - 1
    final1 = int_features[:lastElementIndex]
    final = [np.array(final1)]
    popu = request.form['population']
    print(float(popu))
    print(int_features)
    print(final1)
    prediction = model.predict(final)
    output = prediction * 100 / float(popu)
    output1 = np.round(output[0], 2)
    return render_template('template.html', pred='Probability of Obese population in your state is {}%'.format(output1))


@app.route('/predictgym', methods=['POST', 'GET'])
def predict1():
    int_features = [x for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model1.predict(final)
    output = np.round(prediction[0], 2)
    return render_template('template.html', pred1='The Total Number of Gym in your state is {}'.format(output[0]))


@app.route('/predictsnap', methods=['POST', 'GET'])
def predict2():
    int_features = [x for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model2.predict(final)
    output = np.round(prediction[0], 2)
    return render_template('template.html', pred2='The amount of HouseHold SNAP Benefit is {}$'.format(output[0]))


@app.route('/predictstore', methods=['POST', 'GET'])
def predict3():
    int_features = [x for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    ts = request.form['Total_Stores']
    prediction = model3.predict(final)
    output = prediction * 100 / float(ts)
    output1 = np.round(output[0], 2)
    return render_template('template.html', pred3='Probability of unauthorized stores to AP in your state is {}%'.format(output1))
