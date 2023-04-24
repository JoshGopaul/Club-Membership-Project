from App.database import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    time = db.Column(db.Integer, nullable =False)


    def __init__(self, title, description):
        self.title = title
        self.description = description

    def toJSON(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
