"""Pet Adoption Application"""
"""Eldy Deines"""
"""App incorporates WTForms"""

"""Import necessary libraries and models"""
from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

"""Configure flask object and set database"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ohsecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

""" --------------------------------------------------------------------------------"""
"""This section will connect, drop existing tables,and add new tables based on model"""
"""Section will add sample data into tables ----------------------------------------"""
""" --------------------------------------------------------------------------------"""
connect_db(app)
db.drop_all()
db.create_all()

Boser = Pet(name="Boser", species="dog", age=2, available=True, notes="Loving and playful", photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6wRawbXVgyoGMqmM66KRRH3Q7iHpm3wsEmA&usqp=CAU")
Tiger = Pet(name="Tiger", species="cat", age=1, available=True, notes="Fun and serious", photo_url="https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/slideshows/is_my_cat_normal_slideshow/1800x1200_is_my_cat_normal_slideshow.jpg")
Prickly = Pet(name="Prickly", species="porcupine", age=4, available=False, notes="Swims a lot", photo_url="https://www.petmd.com/sites/default/files/styles/article_image/public/goldfish-swimmingtoward_285011336_0.jpg?itok=ZZaLxiFQ")

db.session.add_all([Boser, Tiger, Prickly])
db.session.commit()


""" -----------------------------------------------------------------------"""
""" ------------------------   ROUTES -------- ----------------------------"""
""" -----------------------------------------------------------------------"""

@app.route('/')
def list_users():
    """List all pets"""
    all_pets = Pet.query.all()
    return render_template('pets.html', pets=all_pets)


@app.route('/add', methods=["GET","POST"])
def add_pet():
    """Provide Form to add Pets and validate"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else: 
        return render_template("add-pet.html",form=form)


@app.route('/<int:id>', methods=["GET","POST"])
def edit_pet(id):
    """Get pet from db and edit pet based on submission from validated from"""
    edit_pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=edit_pet)
    if form.validate_on_submit():
        edit_pet.photo_url = form.photo_url.data
        edit_pet.notes = form.notes.data
        edit_pet.available = bool(form.available.data)
        db.session.add(edit_pet)
        db.session.commit()
        return redirect('/')
    else: 
        return render_template("edit-pet.html",form=form,pet=edit_pet)