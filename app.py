from flask import Flask, render_template, request, redirect, flash
from flask.helpers import url_for
import requests
from datetime import datetime
import helper
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# New register
@app.route("/register", methods=["GET","POST"])
def register():
    
    data = helper.registerData()

    if request.method == "POST":
        if request.form["person"] and request.form["type"] and request.form["gender"] and request.form["age"] and request.form["destination"] and request.form["specie"]:
            
            weigth = None
            size = None
            if request.form["weigth"]:
                weigth = float(request.form["weigth"])
            if request.form["size"]:
                size = float(request.form["size"])
            
            pload_specimen = {"person_id":request.form["person"],
            "animalType_id":request.form["type"],
            "species_id":request.form["specie"],
            "gender_id":request.form["gender"],
            "age_id":request.form["age"],
            "destination_id":request.form["destination"],
            "condition":request.form["condition"],
            "weigth":weigth,
            "size":size
            }

            r = requests.post('http://127.0.0.1:5000/specimen', json = pload_specimen)
            print(r.status_code)
            if r.status_code < 399:
                pload_reception = {
                    "specimen_id":r.json()['data']['id'],
                    "deliver_person":request.form["deliverer"],
                    "reciever_person_id":request.form["person"],
                    "neighborhood_id":request.form["neighborhood"]
                }

                r = requests.post('http://127.0.0.1:5000/reception', json = pload_reception)

                return render_template("index.html", message = "Registro creado satisfactoriamente!", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
    else:
        return render_template("register.html", 
            persons=data[0], 
            types = data[1],
            species=data[2], 
            genders=data[3], 
            ages=data[4], 
            destinations=data[5],
            states=data[6],
            cities=data[7],
            neig=data[8]
        )

# Tracking and final destination
@app.route("/tracking", methods=["GET","POST"])
def tracking():

    data = helper.trackingData()

    if data[1]:
        specimens = data[1][::-1]
    else:
        return render_template("tracking.html", 
            destinations=data[0], 
            specimens=data[1]
        )

    if request.method == "POST":
        if request.form["destination"] and request.form["folio"] and request.form["date"] :
            
            url_specimen = 'http://127.0.0.1:5000/specimen?folio={}'.format(request.form["folio"])
            resp = requests.get(url=url_specimen)
            specimens = resp.json()['data']
            weigth = None
            size = None
            if request.form["weigth"]:
                weigth = float(request.form["weigth"])
            if request.form["size"]:
                size = float(request.form["size"])

            if not specimens:
                return render_template("index.html", message = "Specimen no encontrado!", category = "danger")
            date = datetime.strptime(request.form["date"], '%Y-%m-%d')
            pload = {
                "specimen_id":specimens[0]["id"],
                "date":date.strftime("%y-%m-%d"),
                "reviewed":"false",
                "weight": weigth,
                "size" : size,
                "condition":request.form["condition"],
                "destination_id":request.form["destination"]
            }
            print(pload)
            r = requests.post('http://127.0.0.1:5000/tracking', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = "Seguimiento creado satisfactoriamente", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
    else:
        return render_template("tracking.html", 
            destinations=data[0], 
            specimens=data[1]
        )
        
@app.route("/destination", methods=["GET","POST"])
def destination():

    data = helper.destinationData()

    if data[1]:
        specimens = data[1][::-1]
    else:
        return render_template("destination.html", 
            destinations=data[0], 
            specimens=data[1]
        )

    if request.method == "POST":
        if request.form["destination"] and request.form["folio"]:
            url_specimen = 'http://127.0.0.1:5000/specimen?folio={}'.format(request.form["folio"])
            resp = requests.get(url=url_specimen)
            specimens = resp.json()['data']

            weigth = None
            size = None
            if request.form["weigth"]:
                weigth = float(request.form["weigth"])
            if request.form["size"]:
                size = float(request.form["size"])

            pload = {
                "specimen_id":specimens[0]["id"],
                "destination_id":request.form["destination"],
                "condition":request.form["condition"],
                "weigth":weigth,
                "size":size,
                "notes":request.form["notes"]
            }

            r = requests.post('http://127.0.0.1:5000/final', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = "Destino final creado!", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
    else:
        return render_template("destination.html", 
            destinations=data[0], 
            specimens=data[1]
        )

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
                return render_template("index.html", message = "Nuevo destino agregado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'],category = "danger")
    else:
        return render_template("newDestination.html")

@app.route("/newGender", methods=["GET","POST"])
def newGender():
    if request.method == "POST":
        if request.form["gender"]:
            pload = {"name":request.form["gender"]}

            r = requests.post('http://127.0.0.1:5000/gender', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nuevo genero agregado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
    else:
        return render_template("newGender.html")

@app.route("/newAge", methods=["GET","POST"])
def newAge():
    if request.method == "POST":
        if request.form["age"]:
            pload = {"name":request.form["age"]}

            r = requests.post('http://127.0.0.1:5000/age', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nueva edad agregada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'],category = "danger")
    else:
        return render_template("newAge.html")

@app.route("/newFamily", methods=["GET","POST"])
def newFamily():

    if request.method == "POST":
        if request.form["family"]:
            pload = {"name":request.form["family"]}

            r = requests.post('http://127.0.0.1:5000/type', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nueva familia agregada",category = "success")
            else:
                return render_template("index.html", message = r.json()['message'],category = "danger")
    else:
        return render_template("newFamily.html")

@app.route("/newSpecie", methods=["GET","POST"])
def newSpecie():
    
    data = helper.speciesData()

    if request.method == "POST":
        if request.form["common_name"] and request.form["scientific_name"] and request.form["type"]:
            pload = {
                "common_name":request.form["common_name"],
                "animal_type_id":request.form["type"],
                "scientific_name":request.form["scientific_name"],        
            }

            r = requests.post('http://127.0.0.1:5000/species', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nuevas especie agregada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
    else:
        return render_template("newSpecie.html",types = data[0])

@app.route("/newNeighborhood", methods=["GET","POST"])
def newNeighborhood():
    data = helper.neighborhoodData()

    if request.method == "POST":
        if request.form["neighborhood"] and request.form["city"]:
            pload = {
                "name":request.form["neighborhood"],
                "municipality_id":request.form["city"],        
            }

            r = requests.post('http://127.0.0.1:5000/neighborhood', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nuevo barrio agregado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
    else:
        return render_template("newNeighborhood.html",
            states=data[0],
            cities=data[1]
        )

# main
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)