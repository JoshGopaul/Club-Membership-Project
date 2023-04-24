from App.database import db
from datetime import date, time, datetime

class UserActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable = False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, user_id, activity_id):
        self.user_id = user_id
        self.activity_id = activity_id

    def toJSON(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'activity_id': self.activity_id,
            'date': self.date
        }
