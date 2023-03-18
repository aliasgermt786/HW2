from flask import Flask,jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>' % self.name
    


    with app.app_context():
        db.create_all()
    

        
data =[
{
    
    'name': 'Aliasger',
    'points': '5000',
    'id' : '5253',
    
},
{
    'name': 'rajat',
    'points': '7458',
    'id' : '345',
}
]


@app.route("/")
def hello_world():
    return render_template('Home.html', data=data, title= 'hello')

@app.route("/about")
def about():
    return jsonify( "about")

if __name__ == "__main__":
        app.run(debug = True)