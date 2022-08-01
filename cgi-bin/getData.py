#!/usr/bin/python

import cgi
import cgitb
from xml.etree.ElementTree import tostring
cgitb.enable()
import json

print("Content-Type: text/html\n")

filename = "database.json"
json_data = {}

def Form2Dict():
    D = {}
    F = cgi.FieldStorage()
    for k in F.keys():
        try:
            v = int( F.getvalue(k) )
        except:
            try:
                v = float( F.getvalue(k) )
            except:
                v = str( F.getvalue(k) )
        D[k] = v
    return D

D = Form2Dict()

D['status'] = True
print(json.dumps(D))

def get():
    json_data = {}
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)

    print(json.dumps(json_data))

trips = {}

def add():
    json_data = {}
    # Open file, read into local dict variable, edit.
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)

    # Add riders to the database
    json_data["riders"].append(
        {"id": D["id"], "name": D["name"], "surname": D["surname"], "birthdate": D["birthdate"], "trip": D["trip"], "location" : D['location'], 'waiver': D['waiver']}
    )

    # Update trips list in the database
    for trip in json_data['trips']:
        if D['trip'] in trip.keys():
            trip[D['trip']].append(D['id'])
        else:

            trip[D['trip']] = [D['id']]

    # Write local dict (edited) back to json file.
    with open(filename, "w") as json_file:
        json_data = json.dumps(json_data)
        json_file.write(json_data)
        json_file.close()

add()
