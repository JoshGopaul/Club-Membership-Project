from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import *
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')


@index_views.route('/', methods=['GET'])
@login_required
def login_page():
    return render_template('login.html')

@index_views.route('/home', methods=['GET'])
@login_required
def home_page():
    return render_template('layout.html')                    


@index_views.route('/community/<int:post_id>', methods=['GET'])
@login_required
def community_page(post_id=1):
    id = current_user.id
    posts = Post.query.all()
    comments = Comments.query.all()
    selected_post = Post.query.filter_by(post_id=post_id).first()
    selected_post_comments = Comments.query.filter_by(post_id=post_id).all()
    return render_template('community.html', posts=posts, comments=comments, selected_post=selected_post, selected_post_comments=selected_post_comments)


@index_views.route('/membership', methods=['GET'])
@login_required
def membership_page():
    return render_template('membership.html')


@index_views.route('/activities', methods=['GET'])
@login_required
def activity_page():
    activities = Activity.query.all()
    return render_template('activity.html', activities=activities)

@index_views.route('/progress', methods=['GET'])
@login_required
def progress_page():
    reviews = Review.query.all()
    return render_template('progress.html', reviews=reviews)



@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/index', methods=['GET'])
def index_page():
    return render_template('index.html')


#form actions

@index_views.route('/post', methods=['POST'])
@login_required
def post_action():
    data = request.form
    id = current_user.id 
    post = make_post(user_id=id,title=data['title'],text=data['text'])
    return redirect('/community')

@index_views.route('/post<int:post_id>', methods=['POST'])
@login_required
def edit_post_action(post_id):
    data = request.form
    id = current_user.id 
    post = edit_post(user_id=id,post_id=post_id,title=data['title'],text=data['text'])
    return redirect('/community')

@index_views.route('/post<int:post_id>', methods=['POST'])
@login_required
def remove_post_action(post_id):
    data = request.form
    id = current_user.id 
    post = remove_post(user_id=id,post_id=post_id)
    return redirect('/community')


@index_views.route('/comment/<int:post_id>', methods=['POST'])
@login_required
def comment_action(post_id):
    data = request.form
    id = current_user.id 
    comment = make_comment(user_id=id,post_id=post_id,text=data['text'])
    return redirect('/community')

@index_views.route('/comment/<int:post_id>/<int:comment_id>', methods=['POST'])
@login_required
def edit_comment_action(post_id, comment_id):
    data = request.form
    id = current_user.id 
    post = edit_comment(user_id=id,comment_id=comment_id,text=data['text'])
    return redirect('/community')

@index_views.route('/comment/<int:post_id>/<int:comment_id>', methods=['POST'])
@login_required
def remove_comment_action(post_id, comment_id):
    data = request.form
    id = current_user.id 
    post = remove_comment(user_id=id,comment_id=comment_id)
    return redirect('/community')



@index_views.route('/activity/<int:activity_id>', methods=['POST'])
@login_required
def review_activity_action(actitvity_id):
    data = request.form
    user_id = current_user.id 
    review = make_review(user_id=user_id, actitvity_id = actitvity_id ,rating=data['rating'],text=data['text'])
    return redirect('/activities')


