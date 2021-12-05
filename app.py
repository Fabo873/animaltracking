from flask import Flask, render_template, request, json
from werkzeug.utils import redirect
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# New register
@app.route("/register", methods=["GET","POST"])
def register():
    url_person = 'http://127.0.0.1:5000/person'
    resp = requests.get(url=url_person)
    persons = resp.json()['data']

    url_type = 'http://127.0.0.1:5000/type'
    resp = requests.get(url=url_type)
    types = resp.json()['data']

    url_species = 'http://127.0.0.1:5000/species'
    resp = requests.get(url=url_species)
    species = resp.json()['data']

    url_gender = 'http://127.0.0.1:5000/gender'
    resp = requests.get(url=url_gender)
    genders = resp.json()['data']

    url_age = 'http://127.0.0.1:5000/age'
    resp = requests.get(url=url_age)
    ages = resp.json()['data']

    url_destination = 'http://127.0.0.1:5000/destination'
    resp = requests.get(url=url_destination)
    destinations = resp.json()['data']

    url_states = 'http://127.0.0.1:5000/state'
    resp = requests.get(url=url_states)
    states = resp.json()['data']

    url_municipalities = 'http://127.0.0.1:5000/municipality'
    resp = requests.get(url=url_municipalities)
    cities = resp.json()['data']

    url_neig = 'http://127.0.0.1:5000/state'
    resp = requests.get(url=url_neig)
    neig = resp.json()['data']

    if request.method == "POST":
        
        if request.form["person"] and request.form["type"] and request.form["gender"] and request.form["age"] and request.form["destination"] and request.form["specie"]:
            pload_specimen = {"person_id":request.form["person"],
            "animalType_id":request.form["type"],
            "species_id":request.form["specie"],
            "gender_id":request.form["gender"],
            "age_id":request.form["age"],
            "destination_id":request.form["destination"],
            "condition":request.form["condition"],
            "weigth":request.form["weigth"],
            "size":request.form["size"]
            }

            r = requests.post('http://127.0.0.1:5000/specimen', json = pload_specimen)
            print(r.status_code)
            return render_template("index.html", message = r.json()['message'])
            # if r.status_code < 399:
            #     pload_reception = {"specimen_id":r.json()['data']['id'],
            #     "deliver_person":request.form["deliverer"],
            #     "reciever_person_id":request.form["person"],
            #     "neighborhood_id":request.form["location"]
            #     }

            #     r = requests.post('http://127.0.0.1:5000/reception', json = pload_reception)

            #     return render_template("index.html", message = r.json()['message'])
            # else:
            #     return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("register.html", persons=persons, types = types,species=species, genders=genders, ages=ages, destinations=destinations,states=states,cities=cities, neig=neig)

# Tracking and final destination
@app.route("/tracking", methods=["GET","POST"])
def tracking():
    url_destination = 'http://127.0.0.1:5000/destination'
    resp = requests.get(url=url_destination)
    destinations = resp.json()['data']

    if request.method == "POST":
        if request.form["destination"] and request.form["specimen"] and request.form["date"] :
            pload = {
                "specimen_id":request.form["specimen"],
                "date":request.form["date"],
                "reviewed":"false",
                "condition":request.form["condition"],
                "weigth":request.form["weigth"],
                "size":request.form["size"],
                "destination_id":request.form["destination"]
            }
            print(pload)
            r = requests.post('http://127.0.0.1:5000/tracking', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = r.json()['message'])
            else:
                return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("tracking.html", destinations=destinations )
        
@app.route("/destination", methods=["GET","POST"])
def destination():
    url_destination = 'http://127.0.0.1:5000/destination'
    resp = requests.get(url=url_destination)
    destinations = resp.json()['data']

    if request.method == "POST":
        if request.form["destination"] and request.form["specimen"]:
            pload = {
                "specimen_id":request.form["specimen"],
                "destination_id":request.form["destination"],
                "condition":request.form["condition"],
                "weigth":request.form["weigth"],
                "size":request.form["size"],
                "notes":request.form["notes"]
            }

            r = requests.post('http://127.0.0.1:5000/final', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = r.json()['message'])
            else:
                return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("destination.html", destinations=destinations )

# Reports
@app.route("/reports", methods=["GET","POST"])
def reports():
    return render_template("reports.html")


# Add new destination, gender, age, family and species types
@app.route("/newDestnation", methods=["GET","POST"])
def newDestination():
    if request.method == "POST":
        if request.form["destination"]:
            pload = {"name":request.form["destination"]}

            r = requests.post('http://127.0.0.1:5000/destination', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = r.json()['message'])
            else:
                return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("newDestination.html")

@app.route("/newGender", methods=["GET","POST"])
def newGender():
    if request.method == "POST":
        if request.form["gender"]:
            pload = {"name":request.form["gender"]}

            r = requests.post('http://127.0.0.1:5000/gender', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = r.json()['message'])
            else:
                return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("newGender.html")

@app.route("/newAge", methods=["GET","POST"])
def newAge():
    if request.method == "POST":
        if request.form["age"]:
            pload = {"name":request.form["age"]}

            r = requests.post('http://127.0.0.1:5000/age', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = r.json()['message'])
            else:
                return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("newAge.html")

@app.route("/newFamily", methods=["GET","POST"])
def newFamily():

    if request.method == "POST":
        if request.form["family"]:
            pload = {"name":request.form["family"]}

            r = requests.post('http://127.0.0.1:5000/type', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = r.json()['message'])
            else:
                return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("newFamily.html")

@app.route("/newSpecie", methods=["GET","POST"])
def newSpecie():
    url_type = 'http://127.0.0.1:5000/type'
    resp = requests.get(url=url_type)
    types = resp.json()['data']

    if request.method == "POST":
        if request.form["common_name"] and request.form["scientific_name"] and request.form["type"]:
            pload = {
                "common_name":request.form["common_name"],
                "animal_type_id":request.form["type"],
                "scientific_name":request.form["scientific_name"],        
            }

            r = requests.post('http://127.0.0.1:5000/species', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = r.json()['message'])
            else:
                return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("newSpecie.html",types = types)

# main
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)