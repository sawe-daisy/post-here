from flask import render_template,request,redirect,url_for,abort, flash, abort
from . import main
from flask_fontawesome import FontAwesome
from .. import db, photos
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment, Upvotes,Downvote, PhotoProfile
from .forms import AddPitch, UpdateProfile, CommentsForm, UpvoteForm,DownvoteForm
from flask.views import View, MethodView
import markdown2
from ..req import get_quotes

@main.route('/')
def index():
    quotes= get_quotes()

    return render_template('index.html', quotes=quotes)