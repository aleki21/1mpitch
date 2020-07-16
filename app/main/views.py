from flask import render_template,request,redirect,url_for,abort
from ..models import User
from flask_login import login_required
from .. import db,photos
from . import main

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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

@main.route('/user/ <uname>/addpitch',methods =['GET', 'POST'])
@login_required
def add_pitch(uname):
    title = "Add pitch"
    form = addPitch()
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    if form.validate_on_submit():
        title = form.title.data
        categorydata = form.category.data
        category_id = (Category.get_category_name(categorydata))
        description = form.description.data
        upvotes = 0
        downvotes = 0
        
        
        new_pitch = Pitch(title=title, category_id = category_id, description = description, user = user, upvotes = upvotes, downvotes = downvotes)
        new_pitch.save_pitch()

        return redirect(url_for("main.index"))
    return render_template("addpitch.html", form = form, title = title)

@main.route('/home/comments/new/<int:id>', methods = ['GET','POST'])
@login_requireddef new_review(id):

    form = ReviewForm()

    pitch = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        new_review = Review()
        new_review.save_review()

        return redirect(url_for('.movie',id = piych.id ))

    title = f'{pitch.title} review'
    return render_template('new_review.html',title = title, review_form=form)def new_review(id):

