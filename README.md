# GeoLocationAPI
A GeoLocation Web Application created using Django Web Framework. Upload a excel file with list of address as input and the web app generates a list of matching co-ordinates (longitudes &amp; latitudes) using MapQuest's Geolocation API.

Demo:
https://geolocationapidjangoapp.herokuapp.com/

Software Requirements:

1. Python (Version: 3.8.5 or above) & pip.
2. Git CLI
3. Microsoft Excel (Optional)

Packages:
1. venv (Virtual Environment)
2. Django (Version: 2.2.17)
3. Requests
4. Pandas

Installation Steps:

1. Please clone the application using below command on Command Prompt\ Git\ Terminal (as per applicable OS).
   git clone https://github.com/adityamulik/GeoLocationAPI.git
2. Change directory to the downloaded application as per above.
   cd ..DIRECTORY
4. Create a virtual environment using Python3.
   python3 -m venv venv
4. Activate the virual environment.
   source venv\bin\activate or source venv/Scripts/activate
5. Install packages as mentioned in requirements.txt file available in the folder.
   pip3 install -r requirements.txt
6. Add config file (config.json) to the same folder with below configuration
   {
      "SECRET_KEY": "YOUR_SECRET_KEY_TO_RUN_DJANGO_APP",
      "MAPQUEST_API_KEY": "REGISTER_FOR_MAPQUEST_API_AND_ENTER_THE_SECRET_KEY_HERE"
   }
7. Run migrations and start the application.
   python manage.py makemigrations
   python manage.py migrate
8. Run the application 
   python manage.py runserver
9. Now the application should be running live on localhost on default port 8080. Please check if the port is not in use and run with an alternate port.
10. Launch the application on any browser to access it.
