from flask import Flask, render_template, request, json
from werkzeug.utils import redirect
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# OK
@app.route("/destination", methods=["GET","POST"])
def destination():
    if request.method == "POST":
        # if request.form["destination"]
        pload = {"name":request.form["destination"]
        }
        r = requests.post('http://127.0.0.1:5000/destination', json = pload)
        print(r.text)
        return render_template("index.html")
    else:
        return render_template("destination.html")

# OK
@app.route("/reception", methods=["GET","POST"])
def reception():
    if request.method == "POST":
        # if request.form["specimen"] and request.form["reciever"] and request.form["location"]
        pload = {"specimen_id":request.form["specimen"],
        "deliver_person":request.form["deliverer"],
        "reciever_person_id":request.form["reciever"],
        "location_id":request.form["location"]
        }
        r = requests.post('http://127.0.0.1:5000/reception', json = pload)
        print(r.text)
        return render_template("index.html")
    else:
        return render_template("reception.html")

@app.route("/specimen", methods=["GET","POST"])
def specimen():
    url = 'http://127.0.0.1:5000/person'

    resp = requests.get(url=url)
    data = resp.json()
    print(data)

    if request.method == "POST":
        # if request.form["person"] and request.form["type"] and request.form["gender"] and request.form["age"] and request.form["destination"]
        pload = {"person_id":request.form["person"],
        "animalType_id":request.form["type"],
        "species_id":request.form["specie"],
        "gender_id":request.form["gender"],
        "age_id":request.form["age"],
        "destination_id":request.form["destination"],
        "condition":request.form["condition"],
        "weigth":request.form["weigth"],
        "size":request.form["size"]
        }

        print(pload)
        print(type(pload))
        r = requests.post('http://127.0.0.1:5000/specimen', json = pload)
        print(r.text)
        return render_template("index.html")
    else:
        return render_template("specimen.html")

@app.route("/tracking", methods=["GET","POST"])
def tracking():
    if request.method == "POST":
        # if request.form["person"] and request.form["type"] and request.form["gender"] and request.form["age"] and request.form["destination"]
        pload = {"specimen_id":request.form["specimen"],
        "date":request.form["date"],
        "reviewed":request.form["specie"],
        "destination_id":request.form["destination"],
        "condition":request.form["condition"],
        "weigth":request.form["weigth"],
        "size":request.form["size"]
        }
        r = requests.post('http://127.0.0.1:5000/tracking', json = pload)
        print(r.text)
        return render_template("index.html")
    else:
        return render_template("tracking.html")


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)