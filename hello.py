import requests
__author__ = 'Dmitriy.Rypalov'
print('Hello world')

print(requests.get('http://fhirtest.uhn.ca/baseDstu3','Organization?_format=json&_pretty=true').json())