from flask import Flask, render_template, redirect, request
import joblib

# __name__ = __main__
app = Flask(__name__) # instantiation of Flask

model = joblib.load("new_model.pkl")

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        hours = float(request.form['hours'])

        marks = model.predict([[hours]])[0][0]/10 # [0][0] indexing is done to get the firs value of 2-d matrix
        if marks>100:
            marks = 100
        marks = str(marks)

    return render_template("index.html", your_marks=marks)


if __name__ == '__main__':
    app.run(debug=True)
