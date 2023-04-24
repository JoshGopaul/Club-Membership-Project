from App.models import* 
from App.database import db
from sqlalchemy.exc import IntegrityError

def make_activity(user_id, title, description):
    user = User.query.filter_by(id=user_id).first()
    if user:
       activity = User.make_activity(user, title, description)
       return activity
    return None
        

def edit_activity(user_id, activity_id, title, description):
    user = User.query.filter_by(id=user_id).first()
    if user:
       activity = User.edit_activity(user, activity_id, title, description)
       return activity
    return None

def remove_activity(user_id, activity_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
       activity = User.remove_activity(user, activity_id)
       return True
    return None


def get_activities(id):
    return Activity.query.get(id)

def get_all_activities():
    return Activity.query.all()

def get_all_activities_json():
    activities = get_all_activities()
    if activities:
       return[activity.toJSON() for activity in activities]
    return None
