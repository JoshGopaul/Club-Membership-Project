from App.database import db
from datetime import date, time, datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    title =  db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, user_id, title, text):
        self.user_id = user_id
        self.title = title
        self.text = text

    def toJSON(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'text': self.text,
            'date': self.date
        }
