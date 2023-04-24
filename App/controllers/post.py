from App.models import* 
from App.database import db
from sqlalchemy.exc import IntegrityError



def make_post(user_id, post_id, text):
    user = User.query.filter_by(id=user_id).first()
    if user:
       post = User.make_post(user,post_id, text)
       return post
    return None
        

def edit_post(user_id, post_id, text):
    user = User.query.filter_by(id=user_id).first()
    if user:
       post = User.edit_post(user,post_id, text)
       return post
    return None

def remove_post(user_id, post_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
       post = User.remove_post(user,post_id, text)
       return True
    return None


def get_post(id):
    return Posts.query.get(id)

def get_all_posts():
    return Post.query.all()

def get_all_posts_json():
    posts = get_all_posts()
    if posts:
       return[post.toJSON() for post in posts]
    return None