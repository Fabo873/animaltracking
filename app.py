from flask import Flask, render_template, request, json
from werkzeug.utils import redirect
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tracking")
def tracking():
    return render_template("tracking.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

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

    if request.method == "POST":
        if request.method == "POST":
            if request.form["person"] and request.form["type"] and request.form["gender"] and request.form["age"] and request.form["destination"]:
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
                if r.status_code < 399:
                    pload_reception = {"specimen_id":r.json()['data']['id'],
                    "deliver_person":request.form["deliverer"],
                    "reciever_person_id":request.form["person"],
                    "location_id":request.form["location"]
                    }

                    r = requests.post('http://127.0.0.1:5000/reception', json = pload_reception)

                    return render_template("index.html", message = r.json()['message'])
                else:
                    return render_template("index.html", message = r.json()['message'])
    else:
        return render_template("register.html", persons=persons, types = types,species=species, genders=genders, ages=ages, destinations=destinations )
        # return render_template("register.html")

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)