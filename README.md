# 🕋 open_mosque_dynamic_website 🕋
The Open Mosque Project is about developing a website and web services for all mosques for near enough free. The idea is that they would only need hosting and 1 person to help set it up.
The website will provide mosques auto-generated prayer times (with adjustable jamaa times) and pages for other services they may offer. 

The idea is to keep this open source so that others can take and build on it. 
It would be great to grow an open community with ideas and know-how to help develop this for all mosques in the world.

The project is being developed using a Django backend. We are still in early stages and needs people with the skills to help make this project a reality insha'Allah 🤲.


## 🔧 Setup 🔧

Before trying to run the server

### Django

- add a file named `.env` in the root folder
- create a variable called `SECRET_KEY='replace_this_part_with_secret_key'` in the `.env` file
- generate a secret key from here https://miniwebtool.com/django-secret-key-generator/
- between Git Pulls do not forget to run `pip install -r requirements.txt`
- run `python manage.py makemigrations` and `python manage.py migrate`

- *if* new dependencies have been added run `pip freeze > requirements.txt`

### Other info
There are 2 great APIs to that I have used in projects to generate prayer times. Most mosques in London use https://www.londonprayertimes.com/api/. You may wish to consider that if you are from the UK.
For this project I have used the excellent https://aladhan.com/prayer-times-api. No API Key needed.

### Attribution
resources I have used to put together this template
- https://colorlib.com/wp/template/carousel-07/ 
- https://colorlib.com/wp/template/carousel-19/
- Blue mosque image - https://commons.wikimedia.org/wiki/File:Blue_Mosque_2017.jpg
- Latitude, Longitude finder https://www.latlong.net/