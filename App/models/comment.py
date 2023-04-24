from App.database import db
from datetime import date, time, datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    text = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, user_id, post_id, text):
        self.user_id = user_id
        self.post_id = post_id
        self.text = text

    def toJSON(self):
        return{
            'id': self.id,
            'post_id': self.post_id,
            'user_id': self.user_id,
            'text': self.text,
            'date': self.date
        }
