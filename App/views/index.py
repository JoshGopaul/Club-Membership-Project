from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')


@index_views.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@index_views.route('/home', methods=['GET'])
def home_page():
    return render_template('layout.html')


@index_views.route('/community', methods=['GET'])
def community_page():
    return render_template('community.html')


@index_views.route('/membership', methods=['GET'])
def membership_page():
    return render_template('membership.html')


@index_views.route('/activities', methods=['GET'])
def activity_page():
    return render_template('activity.html')

@index_views.route('/progress', methods=['GET'])
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
