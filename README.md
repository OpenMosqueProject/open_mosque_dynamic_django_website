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
- run `python manage.py createsuperuser`
- run `python manage.py runserver`

- *if* new dependencies have been added run `pip freeze > requirements.txt`

### *Current bug* 🤷‍♂️
There is an issue with the fact that Django currently does not have a solution to creating a singleton model. This means that when first running the `makemigrations` command, you will come across the error that `django.db.utils.OperationalError: no such table: masjidConfig_centreprofile`.
In order to overcome this, we need to comment out references to queries of the singleton object. 
These exist in both `views.py` files in the `posts` and `masjidConfig` apps. They will be commented for you to see. Once you have created the table for the singleton model, `CentreProfile` by running the commands, `python manage.py makemigrations` and `python manage.py migrate`, you can then uncomment the queries in reference.

- on line 10 of masjidConfig views.py comment out --> masjid = CentreProfile.load()
- lastly again in posts views.py comment out the variables on lines 43-60

Unfortunately, this issue crops up again if you are making changes to the masjidConfig model so do the above again


### Other info
There are 2 great APIs to that I have used in projects to generate prayer times. Most mosques in London use https://www.londonprayertimes.com/api/. You may wish to consider that if you are from the UK.
For this project I have used the excellent https://aladhan.com/prayer-times-api. No API Key needed.

### Attribution
resources I have used to put together this template
- Homepage Carousel - https://colorlib.com/wp/template/carousel-07/ 
- Default Post Blue mosque image - https://commons.wikimedia.org/wiki/File:Blue_Mosque_2017.jpg
- Default Homepage Arial view of Blue Mosque from https://theistanbulinsider.com/the-blue-mosque-one-of-the-most-famous-misunderstandings/
- Latitude, Longitude finder - https://www.latlong.net/
- About page Google maps embed - https://www.embedgooglemap.net/
- Theme ideas taken from https://bootswatch.com/