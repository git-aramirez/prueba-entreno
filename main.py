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


#----------------------------
#Segunda consulta a la API
#----------------------------

def consult2(link):
    response = requests.get(link)
    api_result = json.loads(response.content)

    # Informacion para la conexion con la base de datos
    host = "127.0.0.1"
    user = "postgres"
    password = "ander123"
    database = "swapi"
    port = "5432"

    #Recorrido de los planetos
    for i in range(len(api_result['results'])):

        try:

            #conexion
            connection = psycopg2.connect(user=user, password=password, host=host, port=port,
                                              database=database)
            cursor = connection.cursor()
            #Inserción

            postgres_insert_query = "INSERT INTO people (name) VALUES ('"+ api_result['results'][i]['name']+ "')"
            cursor.execute(postgres_insert_query)


            print(postgres_insert_query)
            #cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()


        except (Exception, psycopg2.Error) as error:
                 if (connection):
                         print("Failed to insert record into mobile table", error)

        finally:
         # closing database connection.
            if (connection):
                 cursor.close()
                 connection.close()
                 print("PostgreSQL connection is closed")

    # conexion
    connection = psycopg2.connect(user=user, password=password, host=host, port=port,
                                               database=database)
    cursor = connection.cursor()
    cursor.execute("SELECT * from people")

    for i in cursor:
        print(i)


consult2('https://swapi.dev/api/planets');




