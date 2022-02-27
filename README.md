# alta3research-python-cert
Alta3 Research Python Certification.
This python script
1- REST_API call to: Earth
   Example query: https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&api_key=DEMO_KEY
   Parameter	Type	  Default	    Description
    lat	      float	  1.5	        Latitude
    lon	      float	  100.75	    Longitude
    dim	      float	  0.025	      width and height of image in degrees
    date	    date    2020-05-05  format YYYY-MM-DD
   Example:
   What is the Latitude?[1.5]
   What is the Longitude?[100.75]
   What is the Date?[2020-05-05]
   Width and height of image in degrees?[0.025]

   Click in the Link: https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/thumbnails/d0d7714027bc0cd652fb5876778657d8-3997bc0eae5dbd91d9ea3741177bc192:getPixels
    
2- REST_API call to: Asteroids - NeoWs
   Example query https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY
   Parameters: None
   the sript creates a Bar Graph with the Asteorid sort by Magnitude.
   Example:
   Graphic Created: /home/student/static/NASA.png
   
3- Simple Game: Test States-Capital knoledge 
   Starting Game....
   How many Attempts? Enter the number of Attemps you want to try
   what is the capirtal of <State>? Enter the capital of a random State, if the answer is correct you will get 1 point if it is wrong you will get 0.
   Example:
     How many Attempts?2
     what is the capirtal of Alaska?
     Juneau
     Correct! Juneau is the capital of Alaska
     what is the capirtal of New Mexico?
     Santa Fe
     Correct! Santa Fe is the capital of New Mexico

     Final Score: 2 of 2

## Getting Started

Clone: git clone https://github.com/renewv/alta3research-python-cert.git
  
Create a file called key then copy your own key generated from https://api.nasa.gov/ to the key file in the Project Directory
XXXXXpGdCaccDbVzYYYYYBFlX0X5Ofdre1hXXXXX
  
Copy File capitals.json with the State and Capitals

### Prerequisites

Install python and python3 using apt:
sudo apt install python3-pip

Install libraries:
python3 -m pip install crayons
python3 -m pip install requests
python3 -m pip install pandas xlrd openpyxl
python3 -m pip install matplotlib

## Built With

* [Python](https://www.python.org/) - The coding language used

## Authors

**Rene Villatoro**

