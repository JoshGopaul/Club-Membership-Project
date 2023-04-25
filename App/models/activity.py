from App.database import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    time_spent = db.Column(db.Integer, nullable=False)
    calories_burnt = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    
    def __init__(self, title, description, time_spent, calories_burnt):
        self.title = title
        self.description = description
        self.time_spent = time_spent
        self.calories_burnt = calories_burnt

    def toJSON(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'time_spent': self.time_spent,
            'calories_burnt': self.calories_burnt,
            'date': self.date
        }
