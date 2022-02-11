from xml.dom import NotFoundErr
from flask import Flask, request
from person import Person
from redis_om import Migrator
from redis_om.model import NotFoundError

app = Flask(__name__)

# Create a new person.
@app.route("/person/new", methods=["POST"])
def create_person():
    # TODO error handling
    new_person = Person(**request.json)
    print("Creating:")
    print(new_person)
    new_person.save()
    return new_person.pk

# Update a person's age.
@app.route("/person/<id>/age/<int:new_age>", methods=["POST"])
def update_age(id, new_age):
    # TODO Error handling...
    person = Person.get(id)
    person.age = new_age
    person.save()
    return "ok"

# Delete a person by ID.
@app.route("/person/<id>/delete", methods=["POST"])
def delete_person(id):
    # TODO Error handling...
    person = Person.get(id)
    person.delete()
    return "ok"

# Find a person by ID.
@app.route("/person/byid/<id>", methods=["GET"])
def find_by_id(id):
    try:
        person = Person.get(id)
        print(person)
        return person.dict()
    except NotFoundError:
        print(f"{id} not found.")
        return {}

# Find people with a given first and last name.
@app.route("/people/byname/<first_name>/<last_name>", methods=["GET"])
def find_by_name(first_name, last_name):
    return "find_by_name {first_name} {last_name}"

# Find people within a given age range.
@app.route("/people/byage/<int:min_age>/<int:max_age>", methods=["GET"])
def find_in_age_range(min_age, max_age):
    return f"find_in_age_range {min_age}-{max_age}"

# Find people whose personal statements contain a full text search match.
@app.route("/people/bystatement/<text>", methods=["GET"])
def find_matching_statements():
    return "find_matching_statements TODO"

# Find people located within a given radius of a specified point.
@app.route("/people/bylocation/lat/lng/radius/radius_unit", methods=["GET"])
def find_by_radius():
    return "find_by_radius TODO not yet supported..."

@app.route("/", methods=["GET"])
def home_page():
    return "<p>TODO Home Page...</p>"

# Create a RediSearch index for instances of the Person model.
Migrator().run()
