from App.models import* 
from App.database import db
from sqlalchemy.exc import IntegrityError


def make_comment(user_id, comment_id, text):
    user = User.query.filter_by(id=user_id).first()
    if user:
       comment = User.make_comment(user,comment_id, text)
       return comment
    return None
        

def edit_comment(user_id, comment_id, text):
    user = User.query.filter_by(id=user_id).first()
    if user:
       comment = User.edit_comment(user,comment_id, text)
       return comment
    return None

def remove_comment(user_id, comment_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
       comment = User.remove_comment(user,comment_id, text)
       return True
    return None


def get_comments(id):
    return Comment.query.get(id)

def get_all_comments():
    return Comment.query.all()

def get_all_reviews_json():
    comments = get_all_comments()
    if comments:
       return[comment.toJSON() for comment in comments]
    return None