import requests
__author__ = 'Dmitriy.Rypalov'


import requests
import json

FHIR_URL = 'http://fhirtest.uhn.ca/baseDstu2/Patient'


def list():
    r = requests.get(FHIR_URL, dict(_format='json', _pretty=True))
    return r.json()


def create():
    data = {
        "resourceType": "Patient",
        "name": [
            {
                "family": [
                    "Fletchers"
                ],
                "given": [
                    "Arturo",
                    "F"
                ]
            }
        ],
        "gender": "unknown",
        "birthDate": "1942-01-28",
        "deceasedBoolean": False
    }

    r = requests.post(FHIR_URL, json.dumps(data))
    r.headers = {'Accept': 'application/json+fhir', "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    return r.json()

def update(id):
    data = {
        "resourceType": "Patient",
        "name": [
            {
                "family": [
                    "HELLO"
                ],
                "given": [
                    "WORLD",
                    "F"
                ]
            }
        ],
        "gender": "unknown",
        "birthDate": "1942-01-28",
        "deceasedBoolean": False
    }

    r = requests.put(FHIR_URL+'/'+id, json.dumps(data))
    r.headers = {'Accept': 'application/json+fhir', "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    return r.json()

a = create()

print('___________________')
print(a)
print('___________________')
id = '128844'
print(requests.get(FHIR_URL+'/'+id).json())
update(id)
print(requests.get(FHIR_URL+'/'+id).json())

r = requests.delete(FHIR_URL+'/'+id)

#print(list()