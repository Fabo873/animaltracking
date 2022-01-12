from datetime import date, datetime
import requests
import constants

def registerData():
  data = []
  url_person = constants.API_URL+'/person'
  resp = requests.get(url=url_person)
  persons = resp.json()['data']
  data.append(persons)

  url_type = constants.API_URL+'/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  url_species = constants.API_URL+'/species'
  resp = requests.get(url=url_species)
  species = resp.json()['data']
  data.append(species)

  url_gender = constants.API_URL+'/gender'
  resp = requests.get(url=url_gender)
  genders = resp.json()['data']
  data.append(genders)

  url_age = constants.API_URL+'/age'
  resp = requests.get(url=url_age)
  ages = resp.json()['data']
  data.append(ages)

  url_destination = constants.API_URL+'/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  url_states = constants.API_URL+'/state'
  resp = requests.get(url=url_states)
  states = resp.json()['data']
  data.append(states)

  url_municipalities = constants.API_URL+'/municipality'
  resp = requests.get(url=url_municipalities)
  cities = resp.json()['data']
  data.append(cities)

  url_neig = constants.API_URL+'/neighborhood'
  resp = requests.get(url=url_neig)
  neig = resp.json()['data']
  data.append(neig)

  return data

def trackingData():
  data = []

  url_destination = constants.API_URL+'/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  url_specimen = constants.API_URL+'/specimen'
  resp = requests.get(url=url_specimen)
  specimens = resp.json()['data']
  data.append(specimens)

  return data

def destinationData():
  data = []

  url_destination = constants.API_URL+'/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  url_specimen = constants.API_URL+'/specimen'
  resp = requests.get(url=url_specimen)
  specimens = resp.json()['data']
  data.append(specimens)

  return data

def speciesData():
  
  data = []
  
  url_type = constants.API_URL+'/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  url_species = constants.API_URL+'/species'
  resp = requests.get(url=url_species)
  species = resp.json()['data']
  data.append(species)

  return data

def neighborhoodData():
  
  data = []
  url_states = constants.API_URL+'/state'
  resp = requests.get(url=url_states)
  states = resp.json()['data']
  data.append(states)

  url_municipalities = constants.API_URL+'/municipality'
  resp = requests.get(url=url_municipalities)
  cities = resp.json()['data']
  data.append(cities)

  url_neig = constants.API_URL+'/neighborhood'
  resp = requests.get(url=url_neig)
  neig = resp.json()['data']
  data.append(neig)
  
  return data

def specimenReportsData(
    date:date = None,
    person_id:int = None, 
    type_id:int = None, 
    species_id:int = None, 
    gender_id:int = None, 
    age_id:int = None,
    destination_id:int = None,
    folio:str = None
  ):
  data = []
  parameters = {}

  url_person = constants.API_URL+'/person'
  resp = requests.get(url=url_person)
  persons = resp.json()['data']
  data.append(persons)

  url_type = constants.API_URL+'/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  url_species = constants.API_URL+'/species'
  resp = requests.get(url=url_species)
  species = resp.json()['data']
  data.append(species)

  url_gender = constants.API_URL+'/gender'
  resp = requests.get(url=url_gender)
  genders = resp.json()['data']
  data.append(genders)

  url_age = constants.API_URL+'/age'
  resp = requests.get(url=url_age)
  ages = resp.json()['data']
  data.append(ages)

  url_destination = constants.API_URL+'/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)


  if date:
    if date != "0":
      date_from = datetime.strptime(date, '%Y-%m-%d')
      parameters["date_from"]=date_from.strftime("%d-%m-%y")
  if person_id:
    parameters["person_id"]=person_id
  if type_id:
    parameters["animalType_id"]= type_id
  if species_id:
    parameters["species_id"]=species_id
  if gender_id:
    parameters["gender_id"]=gender_id
  if age_id:
    parameters["age_id"]=age_id
  if destination_id:
    parameters["destination_id"]=destination_id
  if folio:
    parameters["folio"]=folio
  
  url_specimen = constants.API_URL+'/specimen'
  resp = requests.get(url=url_specimen, params=parameters)
  specimens = resp.json()['data']
  data.append(specimens)

  return data

def trackingReportsData(
    date:date = None,
    person_id:int = None, 
    type_id:int = None, 
    species_id:int = None, 
    gender_id:int = None, 
    age_id:int = None,
    destination_id:int = None,
    folio:str = None
  ):
  
  data = []
  parameters = {}
  
  url_person = constants.API_URL+'/person'
  resp = requests.get(url=url_person)
  persons = resp.json()['data']
  data.append(persons)

  url_type = constants.API_URL+'/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  url_species = constants.API_URL+'/species'
  resp = requests.get(url=url_species)
  species = resp.json()['data']
  data.append(species)

  url_gender = constants.API_URL+'/gender'
  resp = requests.get(url=url_gender)
  genders = resp.json()['data']
  data.append(genders)

  url_age = constants.API_URL+'/age'
  resp = requests.get(url=url_age)
  ages = resp.json()['data']
  data.append(ages)

  url_destination = constants.API_URL+'/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  url_specimen = constants.API_URL+'/specimen'
  resp = requests.get(url=url_specimen, params=parameters)
  specimens = resp.json()['data']
  data.append(specimens)
  
  if date:
    if date != "0":
      date_from = datetime.strptime(date, '%Y-%m-%d')
      parameters["date_from"]=date_from.strftime("%d-%m-%y")

  if person_id:
    parameters["person_id"]=person_id
  if type_id:
    parameters["animalType_id"]= type_id
  if species_id:
    parameters["species_id"]=species_id
  if gender_id:
    parameters["gender_id"]=gender_id
  if age_id:
    parameters["age_id"]=age_id
  if destination_id:
    parameters["destination_id"]=destination_id
  if folio:
    parameters["folio"]=folio

  url_tracking = constants.API_URL+'/tracking'
  resp = requests.get(url=url_tracking, params=parameters)

  trackings = resp.json()['data']
  data.append(trackings)

  return data

def finalDestinationReportsData(
    date:date = None,
    person_id:int = None, 
    type_id:int = None, 
    species_id:int = None, 
    gender_id:int = None, 
    age_id:int = None,
    destination_id:int = None,
    folio:str = None
  ):
  data = []
  parameters = {}

  url_person = constants.API_URL+'/person'
  resp = requests.get(url=url_person)
  persons = resp.json()['data']
  data.append(persons)

  url_type = constants.API_URL+'/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  url_species = constants.API_URL+'/species'
  resp = requests.get(url=url_species)
  species = resp.json()['data']
  data.append(species)

  url_gender = constants.API_URL+'/gender'
  resp = requests.get(url=url_gender)
  genders = resp.json()['data']
  data.append(genders)

  url_age = constants.API_URL+'/age'
  resp = requests.get(url=url_age)
  ages = resp.json()['data']
  data.append(ages)

  url_destination = constants.API_URL+'/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)


  if date:
    if date != "0":
      date_from = datetime.strptime(date, '%Y-%m-%d')
      parameters["date_from"]=date_from.strftime("%d-%m-%y")
  if person_id:
    parameters["person_id"]=person_id
  if type_id:
    parameters["animalType_id"]= type_id
  if species_id:
    parameters["species_id"]=species_id
  if gender_id:
    parameters["gender_id"]=gender_id
  if age_id:
    parameters["age_id"]=age_id
  if destination_id:
    parameters["destination_id"]=destination_id
  if folio:
    parameters["folio"]=folio
  
  url_final = constants.API_URL+'/final'
  resp = requests.get(url=url_final, params=parameters)
  finals = resp.json()['data']
  data.append(finals)
  return data

def newGenderData():
  
  data = []
  
  url_gender = constants.API_URL+'/gender'
  resp = requests.get(url=url_gender)
  genders = resp.json()['data']
  data.append(genders)

  return data

def newAgeData():
  
  data = []
  
  url_age = constants.API_URL+'/age'
  resp = requests.get(url=url_age)
  ages = resp.json()['data']
  data.append(ages)

  return data

def newDestinationData():
  data = []
  
  url_destination = constants.API_URL+'/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  return data

def newTypeData():
  data = []
  
  url_type = constants.API_URL+'/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  return data

def newPersonData():
  data = []
  
  url_type = constants.API_URL+'/person'
  resp = requests.get(url=url_type)
  persons = resp.json()['data']
  data.append(persons)

  url_type = constants.API_URL+'/user'
  resp = requests.get(url=url_type)
  users = resp.json()['data']
  data.append(users)

  return data