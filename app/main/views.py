from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import  User,Blog,Comment
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos
from . import main
from ..requests import get_quote

@main.route('/')
def index():
    quotes = get_quote()
    blogs = Blog.query.all()

    return render_template("index.html",blogs=blogs,quotes=quotes)

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
    
    return render_template('blog.html', blog_form=form)

@main.route('/blog/<blog_id>/update', methods = ['GET','POST'])
@login_required
def update_blog(blog_id):
    quotes = get_quote()
    blog = Blog.query.get(blog_id)
    if blog.user_id != current_user.id:
        abort(403)
        
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.blog = form.blog.data
        db.session.commit()
        
        
        
        return redirect(url_for('main.index',id = blog.id)) 
    
    if request.method == 'GET':
        form.title.data = blog.title
        form.blog.data = blog.blog
        
    return render_template('blog.html', blog_form = form,quotes = quotes, blog=blog)


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

@main.route('/blog/<int:blog_id>/delete')
@login_required
def delete(blog_id):
    quotes = get_quote()
    blogs = Blog.query.all()
    blog = Blog.query.get(blog_id)
    if blog.user_id != current_user.id:
         abort(403)
    
    Blog.delete_blog(blog)
    
    return redirect(url_for('.index',blog=blog,blogs=blogs,quotes = quotes))

@main.route('/comments/<int:comment_id>/delete')
@login_required
def delete_comment(comment_id):
    quotes = get_quote()
    comments = Comment.query.all()
    comment = Comment.query.get(comment_id)
    if comment.user_id != current_user.id:
        abort(403)
    
    Comment.delete_comment(comment)
    
    return redirect(url_for('.index', comments=comments, comment=comment,quotes = quotes))

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
       
    return render_template('subscribe.html')