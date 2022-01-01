# open_mosque_website
An open source solution for mosques complete with a homepage, about page and customisable prayer times


## 🔧 Setup 🔧

Before trying to run the server

### Django

- add a file named `.env` in the root folder
- create a variable like `SECRET_KEY='replace_this_part_with_secret_key'` in the `.env` file
- generate a secret key from here https://miniwebtool.com/django-secret-key-generator/
- between Git Pulls do not forget to run `pip install -r requirements.txt`

- *if* new dependencies have been added run `pip freeze > requirements.txt`

### Other info
There are 2 great APIs to that I have used in projects to generate prayer times. Most mosques in London use https://www.londonprayertimes.com/api/. You may wish to consider that if you are from the UK.
For this project I have used the excellent https://aladhan.com/prayer-times-api. No API Key needed.

### Attribution
resources I have used to put together this template
- https://colorlib.com/wp/template/carousel-07/ 
- https://colorlib.com/wp/template/carousel-19/
- Blue mosque image - https://commons.wikimedia.org/wiki/File:Blue_Mosque_2017.jpg
- 