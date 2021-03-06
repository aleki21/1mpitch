from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Create class for Users
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    image_path = db.Column(db.String)
    pitch_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(pitch_id=id).all()
        return reviews


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


        @classmethod
        def get_category_pitch(cls,id):
                category_pitches = Pitch.query.filter_by(category_id = id).order_by(Pitch.posted.desc())
                return category_pitches

        @classmethod
        def get_pitch_id(cls,id):
                pitch_id = Pitch.query.filter_by(id = id).order_by(Pitch.id.desc()) 
                return pitch_id


        def __repr__(self):
                return f"Pitch {self.title}"


class Category(db.Model):
    __tablename__ = 'categories'


    id = db.Column(db.Integer,primary_key= True)
    category_name = db.Column(db.string())
    pitches = db.relationship("Pitch", backref ="category", lazy= "dynamic")

    @classmethod
    def get_category_name(cls,category_name):
        categoryName = Category.query.filter_by(category_name = category_name).first()
        return categoryName.id

    def __repr__(self):
        return f'category(self.category_name)'

