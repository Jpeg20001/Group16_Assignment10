#functions.py

import json
import requests #Web Requests Library 

def api_Info(objectNumber):
    '''
    Configures an API request that will be used to print useful information to the console  
    @Param: objectNumber: an Object Number associated to an art piece 
    @return: useful output regarding an artwork, its creator, and when it was created 
    '''
    #Handles the error if the obj number does not exist 
    try:
        #Harvrd Manifest link
        response = requests.get('https://iiif.harvardartmuseums.org/manifests/object/'+objectNumber+'?apikey=f4dab4cd-6815-48a2-9683-e0611ef47a88')
        
        json_string = response.content
        
        parsed_json = json.loads(json_string) # Now we have a python dictionary
        
        #Prints all information in 'Metadata'
        # for art in parsed_json['metadata']:
        #     print (art)
        
        #Creates a variable to store the artist information list 
        artist = parsed_json['metadata'][4]['value']
        
        #instantiates a variable that will store the string of list elements 
        artistString = ''
        
        #This loop converts the list into a string
        for x in artist:
            artistString += ' ' + x
        #Stores the artists name 
        artistName = artistString[9:20]
        
        artPiece = parsed_json['label']
        
        year = parsed_json['metadata'][0]['value']
        
        print(artistName, "created", artPiece, "in", year)
    
    except: 
        pass