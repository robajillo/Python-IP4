from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

    
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    blog = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow())
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_blog(cls,id):
        blogs = Blog.query.filter_by(user_id=id).all()
        return blogs
