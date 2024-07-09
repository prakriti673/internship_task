# Setup and Run Locally:
1. Clone the repository
2. Create your own virtual environment
3. Change directory to: task
4. Make your migrations:``` python manage.py makemigrations``` ```python manage.py migrate```
5. Create a new superuser ```python manage.py createsuperuser``` .
6. Run ```python manage.py runserver```
7. Visit (http://127.0.0.1:8000/) in your browser and view.


## Create your own API Key by signing up on the website: ```https://api-ninjas.com/```
## Change the API Key in ```app/views.py``` ```def home()``` ```response = requests.get(api_url, headers={'X-Api-Key': '```Your API Key```'})```
## To submit data, enter data in the form on the home page
## To view data of all users, click on ```List of Users``` in the header section.
