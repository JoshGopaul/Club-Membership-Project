from App.models import* 
from App.database import db
from sqlalchemy.exc import IntegrityError



def create_review(userId, rating, text):
    user = User.query.filter_by(user_id=userId).first()    
    if user:
       review = User.make_review(user, rating, text)
       return review
    return None

def get_review(id):
    return Review.query.get(id)

def get_all_reviews():
    return Review.query.all()

def get_all_reviews_json():
    reviews = get_all_reviews()
    if reviews:
       return[review.toJSON() for review in reviews]
    return None

