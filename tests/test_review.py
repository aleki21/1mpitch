from app.models import Review,User
from app import db

def setUp(self):
        self.user_Alex = User(username = 'Alex',password = 'password', email = 'alex@ms.com')
        self.new_review = Review(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )