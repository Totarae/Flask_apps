from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from index_calc import *

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='True'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:user@localhost/pgdb1'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="mhdata"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)
    weight_=db.Column(db.Integer)
    bmi_=db.Column(db.Numeric)
    broc_ =db.Column(db.Numeric)

    def __init__(self,email_,height_,weight_,bmi_,broc_):
        self.email_=email_
        self.height_=height_
        self.weight_=weight_
        self.bmi_=bmi_
        self.broc_=broc_


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        weight=request.form["weight_name"]
        bmi = calc_bmi(height, weight)
        broc = calc_broc(height)
        print(email, height, weight, bmi, broc)
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height,weight,bmi,broc)
            db.session.add(data)
           # send_email(email,height)
            db.session.commit()
            return render_template("success.html")

        return render_template("index.html",text="Doubled email. Try another.")

if __name__ == '__main__':
    app.debug=True
    app.run()
