# Adoption Agency Requirements

## Database & Model
- [X] Create a Flask and Flask-SQLAlchemy project, “adopt”.
- [X] Create a single model, Pet. This models a pet potentially available for adoption:

* id: auto-incrementing integer
* name: text, required
* species: text, required
* photo_url: text, optional
* age: integer, optional
* notes: text, optional
* available: true/false, required, should default to available

## Homepage Listing Pets
- [X] The homepage (at route /) should list the pets: name, show photo(if present), display “Available” in bold if the pet is available for adoption

## Create Add Pet Form
- [X] Create a form for adding pets. 
- [X] This should use Flask-WTF, and should have the following fields: Pet name, Species, Photo URL, Age, Notes.  
- [X] This should be at the URL path /add. Add a link to this from the homepage.

## Create Handler for Add Pet Form
This should validate the form:
- [X] if it doesn’t validate, it should re-render the form
- [X] if it does validate, it should create the new pet, and redirect to the homepage
- [X] This should be a POST request to the URL path /add.

## Add Validation
- [X] WTForms gives us lots of useful validators; we want to use these for validating our fields more carefully:
* the species should be either “cat”, “dog”, or “porcupine”
* the photo URL must be a URL (but it should still be able to be optional!)
* the age should be between 0 and 30, if provided

## Add Display/Edit Form
- [X] Make a page that shows some information about the pet: Name, Species, Photo (if present), Age (if present)
- [X] It should also show a form that allows us to edit this pet: Photo URL, Notes, Available
- [X] This should be at the URL /[pet-id-number]. Make the homepage link to this.

## Handle Edit Form
This should validate the form:
- [X] if it doesn’t validate, it should re-render the form
- [X] if it does validate, it should edit the pet
- [X] This should be a POST request to the URL path /[pet-id-number].

