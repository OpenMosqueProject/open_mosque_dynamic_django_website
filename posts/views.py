from django.shortcuts import render
from django.utils.safestring import SafeString

import requests, json, datetime
from .models import Post

from masjidConfig.models import CentreProfile
masjid = CentreProfile.objects.get()

##### Variables loaded from centre profile here #####
masjid_name = masjid.masjid_name 
city = masjid.city 
country = masjid.country 
method = masjid.method
longitude = masjid.longitude
latitude = masjid.latitude
current_time = datetime.datetime.now()
month = current_time.month
year = current_time.year
fajr_jamaah_minutes = 15
dhuhr_jamaah_minutes = 15
asr_jamaah_minutes = 15
maghrib_jamaah_minutes = 15
isha_jamaah_minutes = 15
###############################################


def home(request):
    posts = Post.objects.all()

    api_data = requests.get(f'http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}')
    d = api_data.json()
    fajr = d['data']['timings']['Fajr']
    fj = datetime.datetime.strptime(fajr, '%H:%M') + datetime.timedelta(minutes = fajr_jamaah_minutes)
    fajr_j = f"{fj.hour}:{fj.minute}"
    sunrise = d['data']['timings']['Sunrise']
    dhuhr = d['data']['timings']['Dhuhr']
    dh = datetime.datetime.strptime(dhuhr, '%H:%M') + datetime.timedelta(minutes = dhuhr_jamaah_minutes)
    dhuhr_j = f"{dh.hour}:{dh.minute}"
    asr = d['data']['timings']['Asr']
    asrj = datetime.datetime.strptime(asr, '%H:%M') + datetime.timedelta(minutes = asr_jamaah_minutes)
    asr_j= f"{asrj.hour}:{asrj.minute}"
    maghrib = d['data']['timings']['Maghrib']
    mg = datetime.datetime.strptime(maghrib, '%H:%M') + datetime.timedelta(minutes = maghrib_jamaah_minutes)
    maghrib_j =  f"{mg.hour}:{mg.minute}"
    isha = d['data']['timings']['Isha']
    ish = datetime.datetime.strptime(dhuhr, '%H:%M') + datetime.timedelta(minutes = isha_jamaah_minutes)
    isha_j= f"{ish.hour}:{ish.minute}"
    today = d['data']['date']['readable']
    hijri = f"{d['data']['date']['hijri']['day']}-{d['data']['date']['hijri']['month']['en']}-{d['data']['date']['hijri']['year']}"
    context = {'masjid':masjid, 'posts':posts, 'fajr_j':fajr_j, 'dhuhr_j':dhuhr_j, 'asr_j':asr_j, 'maghrib_j':maghrib_j, 'isha_j':isha_j,
        'fajr':fajr,'sunrise':sunrise, 'dhuhr':dhuhr, 'asr':asr, 'maghrib':maghrib, 'isha':isha, 'today':today, 'hijri':hijri}
    
    return render(request, 'posts/home.html', context)

def month_view(request):
    month_api = requests.get(f'http://api.aladhan.com/v1/calendar?latitude={latitude}&longitude={longitude}&country={country}&method={method}&month={month}&year={year}')
    data = month_api.json()
    d = data['data']
    month_data = []
    for row in d:
        date = row["date"]["gregorian"]["date"]
        weekday =row["date"]["gregorian"]["weekday"]["en"]
        mon = row["date"]["gregorian"]["month"]["en"]
        fajr = row["timings"]["Fajr"][0:5]
        sunrise = row["timings"]["Sunrise"][0:5]
        dhuhr = row["timings"]["Dhuhr"][0:5]
        asr = row["timings"]["Asr"][0:5]
        maghrib = row["timings"]["Maghrib"][0:5]
        isha = row["timings"]["Isha"][0:5]
        day_no = row["date"]["gregorian"]["day"]
        day_ab = row["date"]["gregorian"]["weekday"]
        month_data.append({'fajr':fajr, 'sunrise':sunrise, 'dhuhr':dhuhr, 'asr':asr,'maghrib':maghrib, 'isha':isha,'month':mon, 'date':date, 'weekday':weekday})
    #print(month_data)
    #print(d)
    #####
    # The data for the table needs to be parsed in HTML. 
    # TODO - see if there is a built in HTMX module for parsing the JSON data from the backend.
    # The backend will be continued to source the data as opposed to making the API call from the front end
    # because the backend will have user data eg latitude etc. although...... This can be passed to the front end easily!
    context = {'d':json.dumps(month_data), 'masjid':masjid}
    return render(request, 'posts/month.html', context)