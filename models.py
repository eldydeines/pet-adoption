from flask_sqlalchemy import SQLAlchemy

"""Initialize variable for database"""
db = SQLAlchemy()


def connect_db(app):
    """need to associate our app with db and connect"""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """PET MODEL"""

    __tablename__ = "pets"

    # table columns setup
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
