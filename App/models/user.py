from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from datetime import date, time, datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def make_post(self, title, text):
        try:
            post = Post(self.id, title, text)
            db.session.add(post)
            db.session.commit()
            return post
        except Exception:
            db.session.rollback()
            return None

    def edit_post(self, post_id, title, text):
        post = Post.query.get(post_id)
        if post:
            if title:
                post.title = title
            if text:
                post.text = text
            db.session.add(post)
            db.session.commit()
            return True
        return None

    def remove_post(self, post_id):
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        return None

    def make_payment(self, amount):
        #code for payment

     def make_comment(self, post_id, text):
        post = Post.query.get(post_id)
        if post:
            try:
                comment = Comment(self.id, post_id, text)
                db.session.add(comment)
                db.session.commit()
                return comment
            except Exception:
                db.session.rollback()
                return None
        return None
        

    def edit_comment(self, comment_id, text):
        comment = Comment.query.get(commment_id)
        if comment:
            if text:
                comment.text = text
                comment.date = datetime.utcnow
            db.session.add(comment)
            db.session.commit()
            return True
        return None

    def remove_comment(self, comment_id):
        comment = Comment.query.get(commment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
            return True
        return None

    def make_review(self, actitvity_id, rating, text):
        try:
            review = Review(self.id, actitvity_id, rating, text)
            db.session.add(review)
            db.session.commit()
            return review
        except Exception:
            db.session.rollback()
            return None

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


