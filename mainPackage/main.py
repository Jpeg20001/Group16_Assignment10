# Name: Michael Gonzales, Emmett Webb 
# email: gonzame@mail.uc.edu, webbc7@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/09/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates the use python to generate a configured api requests that will be used to generate useful output.
# Citations:https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
# Anything else that's relevant:[1]https://harvardartmuseums.org/collections/api
#                               [2]https://github.com/harvardartmuseums/api-docsv
#                               [3]https://iiif.harvardartmuseums.org/manifests/object/262968?apikey=f4dab4cd-6815-48a2-9683-e0611ef47a88
import json
import requests
from functionsPackage.functions import *

if __name__ == "__main__":
    #262968 == Andy Wharhols 'Chicken Noodle Soup'
    #apikey=f4dab4cd-6815-48a2-9683-e0611ef47a88  
    api_Info('262968')