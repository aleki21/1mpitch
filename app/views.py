from .models import review
from .forms import ReviewForm
from flask import render_template
from app import app
from flask_login import login_required, current_user

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
@app.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(pitch.id,title,review)
        new_review.save_review()
        return redirect(url_for('pitch',id = movie.id ))

    title = f'{pitch.title} review'
    
    return render_template('new_review.html',review_form=form, pitch=pitch)
   