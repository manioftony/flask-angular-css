from flask import Flask, render_template, jsonify, session, g
from flask_sqlalchemy import SQLAlchemy
import os




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s/mani.db' % (os.getcwd())
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html',**locals())


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    code = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name




# from base import createprofile,db
# createprofile('manikandan','mani@gmail.com')
# db.create_all()




def createprofile(name,email):
    try:
        user = Profile(name=name,email=email)
        db.session.add(user)
        db.session.commit()
        return "sucuess"
    except Exception as er:
        return er


def createsubject(name,code):
    try:
        user = Subject(name=name,code=code)
        db.session.add(user)
        db.session.commit()
        return "sucuess"
    except Exception as er:
        return er


@app.route('/api/<model>/')
def status(model):
    try:
        # import ipdb; ipdb.set_trace()
        if model =='profile':
            p_obj = Profile.query.all()
            json = [{'name':i.name,"email":i.email} for i in p_obj]
        elif model == 'subject':
            s_obj = Subject.query.all()
            json = [{'name':i.name,"code":i.code} for i in s_obj]

        return jsonify({'status': True,'data':json})
    except:
        return jsonify({'status': True,'message':'no exist'})




    # if session.get('logged_in'):
    #     if session['logged_in']:
    #         return jsonify({'status': True})
    # else:
    #     return jsonify({'status': False})



if __name__=='__main__':
    app.run(debug=True)

