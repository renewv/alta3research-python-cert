#!/usr/bin/env python3
""" Python Certification Project author: Rene Villatoro
    Description:
    A script to get Image  from:
    https://api.nasa.gov
    REST_API call to: Earth
    REST_API call to: Asteroids - NeoWs
    Simple Game: Test States-Capital knoledge  
"""
# Import all the libraries
import requests
import pandas
import random
import crayons
from datetime import date
from matplotlib import pyplot as plt


# Set NASA's base URI used in the script:
uri = 'https://api.nasa.gov/planetary/earth/assets'
uri1 = 'https://api.nasa.gov/neo/rest/v1/neo/browse'


# Funtion used to get API key  from file
def gettoken():
    with open ('key','r') as key:
        token = key.readline()
        token = token.rstrip("\n") # Remove the new line from the key
    return token # return the API Key


# Funcition used to Read Capitals from Json file, the output is a DataFrame
def getcapitals():
    capitals_file = 'capitals.json' # Set the File capitals.json
    df_capitals = pandas.read_json(capitals_file) # Read file and write into DataFrame with Pandas library
    return df_capitals # Return states and capitals DataFrame

# Function used to get random list of indexes in a range
def getrandomindex (start, end, num):
    rand = []  # Create an empty list
    for st in range(num):
        rand.append(random.randint(start, end)) # Append random number to a list
    return rand # Return the list
 

# Start the Main funtion
def main():

    ###  First REST API Request for: Asteroids - NeoWs API (Input required)
    # Get Parameters from User
    lat =  input('What is the Latitude?[1.5]') # Get lat
    lon =  input('What is the Longitude?[100.75]') # Get lon
    date = input('What is the Date?[2020-05-05]')
    dim = input('Width and height of image in degrees?[0.025]') # Get dim
    # Set dafault values:
    if lat == '':
        lat = 1.5
    if lon == '':
        lon = 100.75
    if dim == '':
        dim = 0.025
    if date == '':
        date = '2020-05-05'
    # Convert to Float
    lat = float(lat)
    lon = float(lon)
    dim = float(dim)
    api_key = gettoken() # Call gettoken function used to get API key
    # run request using "f" string
    response = requests.get(f"{uri}?lon={lon}&lat={lat}&date={date}&dim={dim}&api_key={api_key}")   # Run the REST API Request for:     https://api.nasa.gov/planetary/earth/imagery
    response = response.json() # Convert response to json format
    url =  (response.get('url'))
    print() # Print blank
    print('Click in the Link:') 
    print(url) # Print the Inage link
    print() # Print Blank


    ###  Second REST API Request for: Earth API (Not imput required)
    api_key = gettoken() # Call gettoken function used to get API key)
    resp_asteroid = requests.get(f"{uri1}?api_key={api_key}")   # Run the REST API Request for https://api.nasa.gov/neo/rest/v1/
    resp_asteroid = resp_asteroid.json() # Convert response to json format
    df_asteroid = pandas.DataFrame(resp_asteroid['near_earth_objects'], columns = ['name_limited','absolute_magnitude_h']) # Create DataFrame from json
    df_asteroid.to_csv("asteroids.csv", index = False) # Export DataFrame to csv file
    asteroid = pandas.read_csv("asteroids.csv") #Read csv file
    asteroid = asteroid.sort_values(by=['absolute_magnitude_h'], ascending=False)   #Sort by Magnitude
    asteroid = asteroid.head(5)
    names_x = asteroid['name_limited'].tolist() #Convert DF to list X
    magnitude_y = asteroid['absolute_magnitude_h'].tolist() #Convert DF to list Y
    plt.style.use ("fivethirtyeight") # Set Graph Style
    plt.bar(names_x,magnitude_y , color='#6a5acd', label= "ASTEROID MAGNITUDE") # Set the Graph Attributes such as Color and label
    plt.title("ASTEROID MAGNITUDE") # Set Graph Title
    plt.xlabel('Asteroid Name') # Set Label for X
    plt.ylabel('Magnitude') # Set Label for Y
    plt.tight_layout() # Adjusts subplot params so that the subplot(s) fits in to the figure area
    plt.savefig("/home/student/static/NASA.png") # Save the graphic
    print("Graphic Created: /home/student/static/NASA.png") # Print graphic location



    ### Now Start the Game
    capitals = getcapitals() # Call functin getcapitals. It is used to get capitals from capitals.json file
    print() # Print blank
    print("Starting Game....")
    print() # Print blank
    num = int(input("How many Attempts?")) #Get the number of Attempts
    start = 0 #Initial index of the DataFrame
    end = len(capitals.index) - 1 #Last Index of the DataFrame
    statelist = getrandomindex(start, end, num) # Call funtion getrandomindex() to get random list of index depending on the number of Attempts
    count = 0 #Initialize the counter
    for i in statelist: 
        state = capitals.state.loc[i] # Get the State for index i
        cap = capitals.capital.loc[i] # Get the Capital for the index i
        cap1 = capitals.capital.loc[i].lower() # Replace  Capital with lower case
        while True:         # Start infinite loop if the user does not enter a value
            print (f'what is the capirtal of {state}?') # Print question
            answer = input().lower() # Get input from the player
            if answer != '':
               break # Finish loop if answer is given
            else:
                print('Please enter the capital') # Request user to enter a capital
        if cap1 == answer: # Compare Answer
             count += 1 # Increase counter
             print (crayons.green(f'Correct! {cap} is the capital of {state}')) # Color Grenn if correct
        else:
             print (crayons.red(f'Sorry, that is wrong')) # Color Red if incorrect
    tries = str(num)
    print() # Print blank
    print(f'Final Score: {count} of {tries}') # Print final Score
    print() # Print blank

if __name__ == "__main__": # Main function
    main()
