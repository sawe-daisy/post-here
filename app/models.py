from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quotes:
     
     quote_list=[]


     def __init__(self, author,quote,permalink):
         self.author = author
         self.quote=quote
         self.permalink=permalink


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    pass_word= db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    upvotes = db.relationship('Upvotes', backref = 'user', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_word = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_word,password)


    def __repr__(self):
        return f'User {self.username}'

class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Blog(db.Model):
    __tablename__='blogs'

    id = db.Column(db.Integer, primary_key=True)
    blog_id= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    details= db.Column(db.String(), index=True)
    title = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment',backref='blog',lazy='dynamic')
    upvotes = db.relationship('Upvotes', backref = 'blog', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'blog', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def getblog(cls, id):
        blogs = Blog.query.order_by(blogId=id).desc().all()
        return blogs

    def __repr__(self):
        return f'Blog {self.details}'

class Comment(db.Model):
    __tablename__='comments'
    id =db.Column(db.Integer, primary_key=True)
    blogs_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    details = db.Column(db.Text)

    def __repr__(self):
        return f'Comment: id:{self.id} comment: {self.details}'

class Upvotes(db.Model):
    __tablename__='upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=0)
    blogs_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_upvotes(cls,id):
        upvote_pitch = Upvotes(user = current_user, blogs_id=id)
        upvote_pitch.save_upvotes()

    
    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvotes.query.filter_by(blogs_idid).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls,blogs_id):
        upvotes = Upvotes.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitches_id}'

class Downvote(db.Model):
    __tablename__= 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    downvote =db.Column(db.Integer, default= 0)
    blogs_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_downvotes(cls,id):
        downvote_blog = Downvote(user = current_user, blogs_id=id)
        downvote_blog.save_downvotes()

    
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(blogs_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls,blogs_id:
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.blogs_id}'