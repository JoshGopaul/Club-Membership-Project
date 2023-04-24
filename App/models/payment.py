from App.database import db
from datetime import date, time, datetime

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, amount):
        self.amount = amount

    def toJSON(self):
        return{
            'id': self.id,
            'customer_id': self.customer_id,
            'amount': self.amount,
            'date': self.date
        }
