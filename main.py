import json
import requests
import psycopg2
import mysql.connector

#-------------------------
#Primera consulta a la API
#-------------------------

def consult(link):
    response = requests.get(link)
    api_result = json.loads(response.content)

    #Se imprimen todos los datos de la persona
    print(api_result);

    for i in range(len(api_result['results'])):
        print(api_result['results'][i]['name'])


consult('https://swapi.dev/api/planets');

