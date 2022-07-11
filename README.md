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
- run `python manage.py collectstatic` to collect static files for ckRTF editor
- run `python manage.py makemigrations` and `python manage.py migrate`

- *if* new dependencies have been added run `pip freeze > requirements.txt`

### *Current bug* 🤷‍♂️
There is an issue with ~django-solo~ DB model settings which is what we are using to save the website profile.
This causes 2 issues. Before you can run the program for the first time, migrate to the DB or create a superuser be sure to:

- on line 3 of the base.html comment out --> {% get_solo 'masjidConfig.CentreProfile' as masjid %}
- on line 10 of masjidConfig views.py comment out --> masjid = CentreProfile.objects.get()
- on line 37 & 88 of posts views.py comment out --> masjid = CentreProfile.objects.get() 
- lastly again in posts views.py comment out the variables on lines 40-53 & 91-104

Unfortunately, this issue crops up again if you are making changes to the masjidConfig model so do the above again


### Other info
There are 2 great APIs to that I have used in projects to generate prayer times. Most mosques in London use https://www.londonprayertimes.com/api/. You may wish to consider that if you are from the UK.
For this project I have used the excellent https://aladhan.com/prayer-times-api. No API Key needed.

### Attribution
resources I have used to put together this template
- https://colorlib.com/wp/template/carousel-07/ 
- https://colorlib.com/wp/template/carousel-19/
- Blue mosque image - https://commons.wikimedia.org/wiki/File:Blue_Mosque_2017.jpg
- Latitude, Longitude finder https://www.latlong.net/
- https://www.embedgooglemap.net/