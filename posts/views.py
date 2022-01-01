from django.shortcuts import render
import datetime
#from datetime import datetime, timedelta
import requests
from .models import Post
# Create your views here.


##### Need to load these from a global profile
city = 'London'
country = 'GB'
method = 2
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
    context = {'posts':posts, 'fajr_j':fajr_j, 'dhuhr_j':dhuhr_j, 'asr_j':asr_j, 'maghrib_j':maghrib_j, 'isha_j':isha_j,
        'fajr':fajr,'sunrise':sunrise, 'dhuhr':dhuhr, 'asr':asr, 'maghrib':maghrib, 'isha':isha, 'today':today, 'hijri':hijri}
    
    return render(request, 'posts/home.html', context)