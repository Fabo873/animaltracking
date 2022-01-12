from flask import Flask, render_template, request, redirect, flash
from flask.helpers import url_for
import requests
from datetime import datetime
import helper
import constants
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# New register
@app.route("/register", methods=["GET","POST"])
def register():
    data = helper.registerData()
    if request.method == "POST":

        if request.form.get("person") and request.form.get("type") and request.form.get("gender") and request.form.get("age") and request.form.get("destination") and request.form.get("specie"):
            
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

            r = requests.post(constants.API_URL+'/specimen', json = pload_specimen)
            if r.status_code < 399:
                pload_reception = {
                    "specimen_id":r.json()['data']['id'],
                    "deliver_person":request.form["deliverer"],
                    "reciever_person_id":request.form["person"],
                    "neighborhood_id":request.form["neighborhood"]
                }

                r = requests.post(constants.API_URL+'/reception', json = pload_reception)

                return render_template("index.html", message = "Registro creado satisfactoriamente!", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        else:
            return render_template("index.html", message = "Porfavor llenar los campos obligatorios", category = "danger")
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
@app.route("/tracking/<folio>", methods=["GET","POST"])
def tracking(folio):
    data = helper.trackingData()

    if data[1]:
        specimens = data[1][::-1]
    else:
        return render_template("tracking.html", 
            destinations=data[0], 
            specimens=data[1]
        )

    if request.method == "POST":
        if request.form.get("destination") and request.form.get("folio") and request.form.get("date") :
            
            url_specimen = constants.API_URL+'/specimen?folio={}'.format(request.form.get("folio"))
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
                "date":date.strftime("%d-%m-%y"),
                "reviewed":"false",
                "weight": weigth,
                "size" : size,
                "condition":request.form["condition"],
                "destination_id":request.form["destination"]
            }

            r = requests.post(constants.API_URL+'/tracking', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Seguimiento creado satisfactoriamente", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("tracking.html", 
            destinations=data[0], 
            specimens=data[1],
            folio=folio
        )
        
@app.route("/destination/<folio>", methods=["GET","POST"])
def destination(folio):

    data = helper.destinationData()

    if data[1]:
        specimens = data[1][::-1]
    else:
        return render_template("destination.html", 
            destinations=data[0], 
            specimens=data[1]
        )

    if request.method == "POST":
        if request.form.get("destination") and request.form.get("folio"):
            url_specimen = constants.API_URL+'/specimen?folio={}'.format(request.form["folio"])
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
            # print(pload)
            r = requests.post(constants.API_URL+'/final', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Destino final creado!", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("destination.html", 
            destinations=data[0], 
            specimens=data[1],
            folio= folio
        )

# Reports
@app.route("/specimenReports", methods=["GET","POST"])
def specimenReports():
    data = helper.specimenReportsData()
    if request.method == "POST":
        date = request.form["date"]
        person_id = request.form["person"]
        type_id = request.form["type"]
        species_id = request.form["specie"]
        gender_id = request.form["gender"]
        age_id = request.form["age"]
        destination_id = request.form["destination"]
        folio = request.form["folio"]
        filteredData = helper.specimenReportsData(date, person_id, type_id, species_id, gender_id, age_id, destination_id, folio)
        return render_template("specimenReports.html", 
            persons = filteredData[0], 
            types = filteredData[1],
            species = filteredData[2], 
            genders = filteredData[3], 
            ages = filteredData[4], 
            destinations = filteredData[5],
            specimens = filteredData[6][::-1],
        )
    return render_template("specimenReports.html", 
        persons = data[0], 
        types = data[1],
        species = data[2], 
        genders = data[3], 
        ages = data[4], 
        destinations = data[5],
        specimens = data[6][::-1]
    )
# Reports
@app.route("/trackingReports", methods=["GET","POST"])
def trackingReports():

    data = helper.trackingReportsData()
    if request.method == "POST":
        
        date = request.form["date"]
        person_id = request.form["person"]
        type_id = request.form["type"]
        species_id = request.form["specie"]
        gender_id = request.form["gender"]
        age_id = request.form["age"]
        destination_id = request.form["destination"]
        folio = request.form["folio"]

        filteredData = helper.trackingReportsData(date, person_id, type_id, species_id, gender_id, age_id, destination_id, folio)
        return render_template("trackingReports.html",
        persons = filteredData[0], 
        types = filteredData[1],
        species = filteredData[2], 
        genders = filteredData[3], 
        ages = filteredData[4], 
        destinations = filteredData[5],
        specimens = filteredData[6],
        trackings = filteredData[7][::-1]
        )
    
    else:
        return render_template("trackingReports.html",
            persons=data[0], 
            types = data[1],
            species=data[2], 
            genders=data[3], 
            ages=data[4], 
            destinations=data[5],
            specimens = data[6],
            trackings = data[7][::-1]
        )

# Reports
@app.route("/finalDestinationReports", methods=["GET","POST"])
def finalDestinationReports():
    data = helper.finalDestinationReportsData()
    if request.method == "POST":
        date = request.form["date"]
        person_id = request.form["person"]
        type_id = request.form["type"]
        species_id = request.form["specie"]
        gender_id = request.form["gender"]
        age_id = request.form["age"]
        destination_id = request.form["destination"]
        folio = request.form["folio"]
        filteredData = helper.finalDestinationReportsData(date, person_id, type_id, species_id, gender_id, age_id, destination_id, folio)
        return render_template("finalDestinationReports.html", 
            persons = filteredData[0], 
            types = filteredData[1],
            species = filteredData[2], 
            genders = filteredData[3], 
            ages = filteredData[4], 
            destinations = filteredData[5],
            finals = filteredData[6][::-1],
        )
    return render_template("finalDestinationReports.html", 
        persons = data[0], 
        types = data[1],
        species = data[2], 
        genders = data[3], 
        ages = data[4], 
        destinations = data[5],
        finals = data[6][::-1]
    )


# Add new destination, gender, age, family and species types
@app.route("/newDestnation", methods=["GET","POST"])
def newDestination():
    data = helper.newDestinationData()
    if request.method == "POST":
        if request.form.get("destination"):
            pload = {"name":request.form["destination"]}

            r = requests.post(constants.API_URL+'/destination', json = pload)
            print(r.status_code)
            if r.status_code < 399:
                return render_template("index.html", message = "Nuevo destino agregado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'],category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("newDestination.html", destinations = data[0])

@app.route("/newGender", methods=["GET","POST"])
def newGender():
    data = helper.newGenderData()
    if request.method == "POST":
        if request.form.get("gender"):
            pload = {"name":request.form["gender"]}

            r = requests.post(constants.API_URL+'/gender', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nuevo genero agregado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("newGender.html", genders = data[0])

@app.route("/newAge", methods=["GET","POST"])
def newAge():
    data = helper.newAgeData()
    if request.method == "POST":
        if request.form.get("age"):
            pload = {"name":request.form["age"]}

            r = requests.post(constants.API_URL+'/age', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nueva edad agregada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'],category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("newAge.html", ages = data[0])

@app.route("/newFamily", methods=["GET","POST"])
def newFamily():
    data = helper.newTypeData()
    if request.method == "POST":
        if request.form.get("family"):
            pload = {"name":request.form["family"]}

            r = requests.post(constants.API_URL+'/type', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nueva familia agregada",category = "success")
            else:
                return render_template("index.html", message = r.json()['message'],category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("newFamily.html", types=data[0])

@app.route("/newSpecie", methods=["GET","POST"])
def newSpecie():
    data = helper.speciesData()

    if request.method == "POST":
        if request.form.get("common_name") and request.form.get("scientific_name") and request.form.get("type"):
            pload = {
                "common_name":request.form["common_name"],
                "animal_type_id":request.form["type"],
                "scientific_name":request.form["scientific_name"],        
            }

            r = requests.post(constants.API_URL+'/species', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nuevas especie agregada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("newSpecie.html",types = data[0], species = data[1])

@app.route("/newNeighborhood", methods=["GET","POST"])
def newNeighborhood():
    data = helper.neighborhoodData()

    if request.method == "POST":
        if request.form.get("neighborhood") and request.form.get("city"):
            pload = {
                "name":request.form["neighborhood"],
                "municipality_id":request.form["city"],        
            }

            r = requests.post(constants.API_URL+'/neighborhood', json = pload)

            if r.status_code < 399:
                return render_template("index.html", message = "Nueva colonia agregada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("newNeighborhood.html",
            states=data[0],
            cities=data[1],
            ns = data[2]
        )


@app.route("/newPerson", methods=["GET","POST"])
def newPerson():
    data = helper.newPersonData()
    if request.method == "POST":
        if request.form.get("username") and request.form.get("password") and request.form.get("name") and request.form.get("first_lastname") and request.form.get("second_lastname"):

            pload = {
                "username":request.form["username"],
                "password": request.form["password"],
            }

            r = requests.post(constants.API_URL+'/user', json = pload)
            url_users = constants.API_URL+'/user'
            resp = requests.get(url=url_users)
            users = resp.json()['data']
            user_id = 0
            for user in users:
                if user["username"] == request.form["username"]:
                    user_id = user["id"]
            if r.status_code < 399:
                pload = {
                "user_id":user_id,
                "name":request.form["name"],
                "first_lastname": request.form["first_lastname"],
                "second_lastname": request.form["second_lastname"]
                }
                r = requests.post(constants.API_URL+'/person', json = pload)
                if r.status_code < 399:
                    return render_template("index.html", message = "Nueva persona creada",category = "success")
                else:
                    return render_template("index.html", message = r.json()['message'],category = "danger")  
            else:
                return render_template("index.html", message = r.json()['message'],category = "danger")
        else:
            return render_template("index.html", message = "Por favor llena todos los campos obligatorios", category = "danger")
    else:
        return render_template("newPerson.html", persons=data[0],users=data[0])

@app.route("/delete/<endPoint>/<int:id>", methods=["POST"])
def delete(endPoint,id):
    # print(endPoint,id)
    if request.method == "POST":
        if endPoint == 'gender':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Genero borrado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        
        elif endPoint == 'age':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Edad borrada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        
        elif endPoint == 'destination':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Destino borrado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        
        elif endPoint == 'type':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Familia borrada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")

        elif endPoint == 'species':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Especie borrada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")

        elif endPoint == 'neighborhood':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Barrio borrado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        
        elif endPoint == 'person':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Persona borrada", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        
        elif endPoint == 'trackingReports':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Record borrado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        elif endPoint == 'specimenReports':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Record borrado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
        elif endPoint == 'finalReports':
            r = requests.delete(constants.API_URL+'/'+endPoint+'/'+str(id))
            if r.status_code < 399:
                return render_template("index.html", message = "Record borrado", category = "success")
            else:
                return render_template("index.html", message = r.json()['message'], category = "danger")
# main

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)