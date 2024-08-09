from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anirban.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 

db = SQLAlchemy(app)

class Anirban(db.Model) :
    sno = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(200) , nullable = False)
    desc = db.Column(db.String(500) , nullable = False)
    date_created = db.Column(db.DateTime , default = datetime.utcnow )

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def hello_world():
    # code to create and save data to db 
    anirban = Anirban(desc = "my name is anirban" , title = "name" )
    db.session.add(anirban)
    db.session.commit()
    # get all the data from db 
    alldata = Anirban.query.all()
    return render_template('index.html' , alldata=alldata)
    # return 'Hello, World!'

@app.route('/show')
def show():
    alldata = Anirban.query.all()
    print(alldata)
    return 'this is a about page'

if __name__ == "__main__" : 
    app.run(debug=True)