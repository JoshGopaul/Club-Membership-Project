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


@index_views.route('/community', methods=['GET'])
@login_required
def community_page():
    id = current_user.id
    posts = Post.query.all()
    return render_template('community.html', posts=posts)


@index_views.route('/membership', methods=['GET'])
@login_required
def membership_page():
    return render_template('membership.html')


@index_views.route('/activities', methods=['GET'])
@login_required
def activity_page():
    return render_template('activity.html')

@index_views.route('/progress', methods=['GET'])
@login_required
def progress_page():
    return render_template('progress.html')



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
def post_action():
    data = request.form
    id = current_user.id 
    post = make_post(user_id=id,title=data['title'],text=data['text'])
    return redirect('/community')

@index_views.route('/activity/<int:activity_id>', methods=['POST'])
def create_activity(actitvity_id):
    data = request.form
    user_id = current_user.id 
    review = make_review(user_id=user_id, actitvity_id = actitvity_id ,rating=data['rating'],text=data['text'])
    return redirect('/activities')


@index_views.route('/activity/<int:activity_id>', methods=['POST'])
def activityReview_action(actitvity_id):
    data = request.form
    user_id = current_user.id 
    review = make_review(user_id=user_id, actitvity_id = actitvity_id ,rating=data['rating'],text=data['text'])
    return redirect('/activities')


    


