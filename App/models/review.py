from App.database import db
from datetime import date, time, datetime

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable = False)
    rating =  db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, user_id, rating, text):
        self.user_id = user_id
        self.rating = rating
        self.text = text

    def toJSON(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'rating': self.rating,
            'text': self.text,
            'date': self.date
        }
