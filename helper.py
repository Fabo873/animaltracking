import requests

def registerData():
  data = []
  url_person = 'http://127.0.0.1:5000/person'
  resp = requests.get(url=url_person)
  persons = resp.json()['data']
  data.append(persons)

  url_type = 'http://127.0.0.1:5000/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  url_species = 'http://127.0.0.1:5000/species'
  resp = requests.get(url=url_species)
  species = resp.json()['data']
  data.append(species)

  url_gender = 'http://127.0.0.1:5000/gender'
  resp = requests.get(url=url_gender)
  genders = resp.json()['data']
  data.append(genders)

  url_age = 'http://127.0.0.1:5000/age'
  resp = requests.get(url=url_age)
  ages = resp.json()['data']
  data.append(ages)

  url_destination = 'http://127.0.0.1:5000/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  url_states = 'http://127.0.0.1:5000/state'
  resp = requests.get(url=url_states)
  states = resp.json()['data']
  data.append(states)

  url_municipalities = 'http://127.0.0.1:5000/municipality'
  resp = requests.get(url=url_municipalities)
  cities = resp.json()['data']
  data.append(cities)

  url_neig = 'http://127.0.0.1:5000/neighborhood'
  resp = requests.get(url=url_neig)
  neig = resp.json()['data']
  data.append(neig)

  return data

def trackingData():
  data = []

  url_destination = 'http://127.0.0.1:5000/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  url_specimen = 'http://127.0.0.1:5000/specimen'
  resp = requests.get(url=url_specimen)
  specimens = resp.json()['data']
  data.append(specimens)

  return data

def destinationData():
  data = []

  url_destination = 'http://127.0.0.1:5000/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)

  url_specimen = 'http://127.0.0.1:5000/specimen'
  resp = requests.get(url=url_specimen)
  specimens = resp.json()['data']
  data.append(specimens)

  return data

def speciesData():
  
  data = []
  
  url_type = 'http://127.0.0.1:5000/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  return data

def neighborhoodData():
  
  data = []
  url_states = 'http://127.0.0.1:5000/state'
  resp = requests.get(url=url_states)
  states = resp.json()['data']
  data.append(states)

  url_municipalities = 'http://127.0.0.1:5000/municipality'
  resp = requests.get(url=url_municipalities)
  cities = resp.json()['data']
  data.append(cities)

  return data

def specimenReportsData(person_id:int = None, species_id:int  = None, gender_id:int = None, age_id:int = None):
  data = []
  parameters = {}

  url_person = 'http://127.0.0.1:5000/person'
  resp = requests.get(url=url_person)
  persons = resp.json()['data']
  data.append(persons)

  url_type = 'http://127.0.0.1:5000/type'
  resp = requests.get(url=url_type)
  types = resp.json()['data']
  data.append(types)

  url_species = 'http://127.0.0.1:5000/species'
  resp = requests.get(url=url_species)
  species = resp.json()['data']
  data.append(species)

  url_gender = 'http://127.0.0.1:5000/gender'
  resp = requests.get(url=url_gender)
  genders = resp.json()['data']
  data.append(genders)

  url_age = 'http://127.0.0.1:5000/age'
  resp = requests.get(url=url_age)
  ages = resp.json()['data']
  data.append(ages)

  url_destination = 'http://127.0.0.1:5000/destination'
  resp = requests.get(url=url_destination)
  destinations = resp.json()['data']
  data.append(destinations)


  if person_id:
    parameters["person"]=person_id
  if species_id:
    parameters["species"]=species_id
  if gender_id:
    parameters["gender"]=gender_id
  if age_id:
    parameters["age"]=age_id
  
  url_specimen = 'http://127.0.0.1:5000/specimen'
  resp = requests.get(url=url_specimen, params=parameters)
  specimens = resp.json()['data']
  data.append(specimens)

  return data

def trackingReportsData(person_id:int = None, species_id:int  = None, gender_id:int = None, age_id:int = None):
  
  data = []
  parameters = {}
  
  url_specimen = 'http://127.0.0.1:5000/tracking'

  if person_id:
    parameters["person"]=person_id
  if species_id:
    parameters["species"]=species_id
  if gender_id:
    parameters["gender"]=gender_id
  if age_id:
    parameters["age"]=age_id

  resp = requests.get(url=url_specimen, params=parameters)
  specimens = resp.json()['data']
  data.append(specimens)

  return data

def finalDestinationReportsData():
  
  data = []
  
  url_specimen = 'http://127.0.0.1:5000/final'
  resp = requests.get(url=url_specimen)
  specimens = resp.json()['data']
  data.append(specimens)

  return data