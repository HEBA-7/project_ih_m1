# **B-School** ![Screenshot](estacionamiento-de-bicicletas.png) <a href="https://www.flaticon.es/iconos-gratis/bicicleta" title="bicicleta iconos">Bicicleta iconos creados por Freepik - Flaticon</a>

### The app for finding the closest bicimad station from the school of your children to the place you want go. Be a friend for the planet, B-School.
**This is the project of Module 1 for Ironhack Data Analytics- V.0**
To enjoy this app, you have two options:
1. For the school you choose, you can filter it by the closest bicimad station in meters.
2. For all the schools, you'll recieve by email all the schools with their closest bicimad station in meters.

![Image](https://www.madridhappypeople.com/wp-content/uploads/2016/10/bicimad-1.jpg)

---

### :computer: **Technology stack**
- SQL
- Pandas
- Python
- Jupyter
- DBeaver

### :boom: **Core technical concepts and inspiration**
The app offers you an alternative of transport, clean and healthy for moving between the school of your children and your home, work or wherever you want just introducing the name of the school. And you could use it as a finder of public schools choosing the option of all.

### :wrench: **Configuration**
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
import re
import json
import math
import numpy as pn
import functools as ft
from shapely.geometry import Point
import geopandas as gpd
import argparse
import smtplib
import imghdr
from email.message import EmailMessage
import os
from dotenv import load_dotenv

### :see_no_evil: **Usage**
Option 1: "one" the input should be the name of the school, and returns all the next information:

![Screenshot](Screenshot 2022-07-21 at 17.11.27)

Option 2: "all" returns all the schools by email:

![Screenshot](Screenshot 2022-07-21 at 17.08.51)


### :file_folder: **Folder structure**
```
└── project_ih_m1
    ├── trash
    |   ├── bicimad_coles.ipynb
    │   └── bicimad_colesyenfant-final.ipynb
    |   ├── bicimad_colesyenfant.ipynb
    │   └── geo_calculations.ipynb
    |   ├── bicimad_coles_escuelas.csv
    │   └── bicimad_coleyescuelas.py
    ├── mailmodule
    |   ├── mailmodule.ipnynb
    │   └── mail.py
    │
    ├── dev_notebook_.ipynb
    └── bicimad_coles_escuelas.csv
    ├── .gitignore
    └── img
    ├── .env
    ├── main.py
    └── README.md
``` 

### :information_source: **Further info**
- [API_colegios públicos Madrid] https://datos.madrid.es/egob (/catalogo/202311-0-colegios-publicos.json)
- [API escuelas infantiles Madrid] https://datos.madrid.es/egob (/catalogo/202318-0-escuelas-infantiles.json)
- MySQL Online Database. The database contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). In order to access the database you may need the following credentials:
Server:        SERVER_IP
Database:      BiciMAD



