from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import  User,Blog,Comment
from .forms import UpdateProfile
from .. import db,photos
from . import main
from ..requests import get_quotes

@main.route('/')
def index():

    return render_template("index.html")

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
       abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/blog', methods=['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = form.blog.data
        title = form.title.data
        new_blog=Blog(blog=blog,title=title,user_id=current_user.id)
        
        new_blog.save_blog()
        
        return redirect(url_for('main.index'))
    
    return render_template('blog.html', form=form)


@main.route('/comments/<int:blog_id>', methods=['GET','POST'])
@login_required
def new_comment(blog_id):
    form = CommentForm
    blogs = Blog.query.get(blog_id)
    comment = Comment.query.filter_by(blog_id=blog_id).all()
    form = CommentForm()
    if form.validate_on_submit():
        comments = form.comment.data
        title = form.title.data
        
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment= Comment(comments=comments,title=title,blog_id=blog_id, user_id=user_id)
        new_comment.save_comment()      
       
        return redirect(url_for('main.new_comment', blog_id=blog_id))
    
    return render_template('comment.html', form=form, comment=comment, blog_id=blog_id,blogs=blogs)
