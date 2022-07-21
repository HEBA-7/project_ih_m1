import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import functools as ft



sqlalchemy.__version__


connect_str = 'mysql+pymysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD'

engine = create_engine(connect_str)
type(engine)

inspector = inspect(engine)
inspector.get_table_names()

#Sacamos primero los datos de Bicimad con la query
query = """SELECT * 
FROM bicimad_stations"""

#la aplicamos y la imprimimos en DataFrame
bici_mad = pd.read_sql_query(query, engine)
df_bici_mad = pd.DataFrame(bici_mad)
df_bici_mad

#Creamos una función para reemplazar los [] de las funciones en vacío para que se aislen
def ll_replace(x):
    return x.replace(']','').replace('[','')
x= "hello, ]my [name, is hali"
type(ll_replace(x))

# primera parte separamos en dos columnas la longitude y la latidude
df_bici_mad[["longitude","latitude"]]=df_bici_mad["geometry.coordinates"].str.split(",",expand=True)

#una vez las tenemos separadas aplicamos la función ll_replace(x) que hemos definido arriba para que me la aplique en ambas columnas

df_bici_mad["longitude"]=df_bici_mad["longitude"].apply(ll_replace)
df_bici_mad["latitude"]=df_bici_mad["latitude"].apply(ll_replace)
df_bici_mad

#Seguimos con los datos de los Colegios públicos

import requests
import pandas as pd
import re
import json
import math
import numpy as pn

response = requests.get('https://datos.madrid.es/egob/catalogo/202311-0-colegios-publicos.json')
colegios = response.json()
colegios.keys()
colegios

info_cole = colegios['@graph']
info_cole

df_info_cole = pd.json_normalize(info_cole)
df_info_cole

#Separamos en dos la latitude y la longitude en dos columnas diferentes 

df_info_cole["latitude"] = df_info_cole["location.latitude"]
df_info_cole["longitude"] = df_info_cole["location.longitude"]
df_info_cole

#Seguimos con los datos de las escuelas infantiles públicos

response = requests.get('https://datos.madrid.es/egob/catalogo/202318-0-escuelas-infantiles.json')
esc_infan = response.json()
esc_infan.keys()
#esc_infan

info_infan = esc_infan['@graph']
print(type(info_infan))

df_info_infan = pd.json_normalize(info_infan)
df_info_infan

df_info_infan["latitude"] = df_info_infan["location.latitude"]
df_info_infan["longitude"] = df_info_infan["location.longitude"]
df_info_infan

df_info_infan = df_info_infan[['title', 'latitude', 'longitude', 'address.street-address']]
df_info_infan

#primero las tablas de los colegios y de las escuelas infantiles, las unimos en una misma tabla porque tienen las mismas columnas

df_coleinf = pd.concat([df_info_cole, df_info_infan], axis=0)
df_coleinf

#creo una columna nueva que es la que nos va a unir las dos tablas, la columna key
df_coleinf["key"]= 0
df_coleinf.shape

#creo también una columna que se llama Key para después realizar el merge
df_bici_mad['key'] = 0
df_bici_mad.shape

#creo un único df para introducirlo dentro de la función lambda con el merge

df_final = [df_coleinf, df_bici_mad]

df_distance = ft.reduce(lambda left, right: pd.merge(left, right, on='key'), df_final)
df_distance

#Convertimos en las columnas de latitude y longitude de ambas tablas en float para poder convertirlas en el mismo type
#y poder aplicar la función más adelante 

df_distance['latitude_x'] = df_distance['latitude_x'].astype(float)
df_distance['longitude_x'] = df_distance['longitude_x'].astype(float)
df_distance['latitude_y'] = df_distance['latitude_y'].astype(float)
df_distance['longitude_y'] = df_distance['longitude_y'].astype(float)
df_distance

#Una vez que he preparado las tablas, procedo a ejecutar la función para sacar la distancia

#Función para obtener la distancia entre el colegio o la escuela infantil y la estación de bicimad

from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas

def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(lat_start, long_start, lat_finish, long_finish):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)

    #Aplico la función arriba creando una nueva columna que es donde irá la distancia calculada

df_distance['distance'] = df_distance.apply(lambda x: distance_meters(x['latitude_y'], x['longitude_y'], x['latitude_x'], x['longitude_x']), axis=1)

df_distance

#Creo un DataFrame para sacar las columnas que me interesan de la orden que quiero
df_distance_final = pd.DataFrame(df_distance, columns= ["title", "address.street-address", "name","address", "distance"])
df_distance_final

#Ordeno la tabla por title del colegio/escuelas infantiles y la distancia de forma ascendente
df_distance_final = df_distance_final.sort_values(by=["title", "distance"])
df_distance_final

#Me quedo con el primero que es la mínima distancia porque lo hemos ordenado de forma ascendente
df_distance_final = df_distance_final.drop_duplicates("title", keep="first")
df_distance_final

df_distance_final.rename(columns = {'title':'School name', 'address.street-address':'Adress school', 'name':'Bicimad station', 'address': 'Bicimad adress', 'distance':'Distance'}, inplace = True)
df_distance_final

df_distance_final = df_distance_final.to_csv('bicimad_coles_escuelas.csv', index=False)








