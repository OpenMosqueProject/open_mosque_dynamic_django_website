from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import View 
from django.template.loader import get_template
from functools import lru_cache

from .utils import render_to_pdf

import requests, json, datetime
from .forms import PostForm
from .models import Post

from masjidConfig.models import CentreProfile

'''This function is used to round the time UP to the nearest 5,10,15
For more info, the idea is taken from 
https://stackoverflow.com/questions/13071384/ceil-a-datetime-to-next-quarter-of-an-hour
'''
def ceil_dt(dt, delta):
    return dt + (datetime.datetime.min - dt) % delta

''' The Jamaah Calculator function takes the desired "minutes after" from the masjid 
profile and adjusts the jamaah times accordingly by using Pythons datetime library.
'''
def jamaah_calculator(azaanTime, minutesAfter):

    if minutesAfter == "5":
        return datetime.datetime.strptime(azaanTime, '%H:%M') + datetime.timedelta(minutes = 5)
    elif minutesAfter == "10":
        return datetime.datetime.strptime(azaanTime, '%H:%M') + datetime.timedelta(minutes = 10)
    elif minutesAfter == "15":
        return datetime.datetime.strptime(azaanTime, '%H:%M') + datetime.timedelta(minutes = 15)
    elif minutesAfter == "round_to_fifteen":
        return ceil_dt(datetime.datetime.strptime(azaanTime, '%H:%M'), datetime.timedelta(minutes=15))
    else:
        return ceil_dt(datetime.datetime.strptime(azaanTime, '%H:%M'), datetime.timedelta(minutes=30))

# NOTE:
# Ternary statements below solves minutes being displayed as single digit eg
# 17:05 displaying as 17:5 or 20:00 displaying as 20:0
@lru_cache(maxsize=1)
def get_masjid_data():
    masjid = CentreProfile.load()
    #### Variables loaded from centre profile here #####
    masjid_name = masjid.masjid_Name 
    city = masjid.city 
    country = masjid.country 
    method = masjid.method
    longitude = masjid.longitude
    latitude = masjid.latitude
    current_time = datetime.datetime.now()
    month = current_time.month
    year = current_time.year
    fajr_jam_min = masjid.fajr_jamaah_minutes
    dh_jam_min = masjid.dhuhr_jamaah_minutes
    asr_jamaah_minutes = masjid.asr_jamaah_minutes
    maghrib_jamaah_minutes = masjid.maghrib_jamaah_minutes
    isha_jamaah_minutes = masjid.isha_jamaah_minutes
    return masjid, masjid_name,city, country, method, longitude, latitude, current_time, month, year, fajr_jam_min,dh_jam_min, asr_jamaah_minutes, maghrib_jamaah_minutes,isha_jamaah_minutes

def home(request):
    # Collecting masjid data from class
    masjid, masjid_name,city, country, method, longitude, latitude, current_time, month, year, fajr_jam_min,dh_jam_min, asr_jamaah_minutes, maghrib_jamaah_minutes,isha_jamaah_minutes = get_masjid_data()
    ###############################################
    posts = Post.objects.all().filter(published=True)
    
    api_data = requests.get(f'http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}')
    d = api_data.json()
    fajr = d['data']['timings']['Fajr']
    fj = jamaah_calculator(fajr, fajr_jam_min)
    fjmins = f"{fj.minute}" if len(str(fj.minute))==2 else f"0{fj.minute}"
    fajr_j = f"{fj.hour}:{fjmins}"
    sunrise = d['data']['timings']['Sunrise']
    dhuhr = d['data']['timings']['Dhuhr']
    dh = jamaah_calculator(dhuhr, dh_jam_min)
    dhmins = f"{dh.minute}" if len(str(dh.minute))==2 else f"0{dh.minute}"
    dhuhr_j = f"{dh.hour}:{dhmins}"
    asr = d['data']['timings']['Asr']
    asrj = jamaah_calculator(asr, asr_jamaah_minutes)
    asmins = f"{asrj.minute}" if len(str(asrj.minute))==2 else f"0{asrj.minute}"
    asr_j= f"{asrj.hour}:{asmins}"
    maghrib = d['data']['timings']['Maghrib']
    mg = jamaah_calculator(maghrib, maghrib_jamaah_minutes)
    mgmins = f"{mg.minute}" if len(str(mg.minute))==2 else f"0{mg.minute}"
    maghrib_j =  f"{mg.hour}:{mgmins}"
    isha = d['data']['timings']['Isha']
    ish = jamaah_calculator(isha, isha_jamaah_minutes)
    ismins = f"{ish.minute}" if len(str(ish.minute))==2 else f"0{ish.minute}"
    isha_j= f"{ish.hour}:{ismins}"
    today = d['data']['date']['readable']
    hijri = f"{d['data']['date']['hijri']['day']}-{d['data']['date']['hijri']['month']['en']}-{d['data']['date']['hijri']['year']}"
    context = {'masjid':masjid, 'posts':posts, 'fajr_j':fajr_j, 'dhuhr_j':dhuhr_j, 'asr_j':asr_j, 'maghrib_j':maghrib_j, 'isha_j':isha_j,
        'fajr':fajr,'sunrise':sunrise, 'dhuhr':dhuhr, 'asr':asr, 'maghrib':maghrib, 'isha':isha, 'today':today, 'hijri':hijri}
    
    return render(request, 'posts/home.html', context)

def get_month_tbl():
    # Collecting masjid data from class
    masjid, masjid_name,city, country, method, longitude, latitude, current_time, month, year, fajr_jam_min,dh_jam_min, asr_jamaah_minutes, maghrib_jamaah_minutes,isha_jamaah_minutes = get_masjid_data()
    ###############################################
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
        fj = jamaah_calculator(fajr, fajr_jam_min)
        fjmins = f"{fj.minute}" if len(str(fj.minute))==2 else f"0{fj.minute}"
        fajr_j = f"{fj.hour}:{fjmins}"
        dhuhr = row["timings"]["Dhuhr"][0:5]
        dh = jamaah_calculator(dhuhr, dh_jam_min)
        dhmins = f"{dh.minute}" if len(str(dh.minute))==2 else f"0{dh.minute}"
        dhuhr_j = f"{dh.hour}:{dhmins}"
        asr = row["timings"]["Asr"][0:5]
        asrj = jamaah_calculator(asr, asr_jamaah_minutes)
        asmins = f"{asrj.minute}" if len(str(asrj.minute))==2 else f"0{asrj.minute}"
        asr_j= f"{asrj.hour}:{asmins}"
        maghrib = row["timings"]["Maghrib"][0:5]
        mg = jamaah_calculator(maghrib, maghrib_jamaah_minutes)
        mgmins = f"{mg.minute}" if len(str(mg.minute))==2 else f"0{mg.minute}"
        maghrib_j =  f"{mg.hour}:{mgmins}"
        isha = row["timings"]["Isha"][0:5]
        ish = jamaah_calculator(isha, isha_jamaah_minutes)
        ismins = f"{ish.minute}" if len(str(ish.minute))==2 else f"0{ish.minute}"
        isha_j= f"{ish.hour}:{ismins}"
        day_no = row["date"]["gregorian"]["day"]
        day_ab = row["date"]["gregorian"]["weekday"]
        month_data.append({'fajr':fajr,'fajr_j':fajr_j,'sunrise':sunrise, 'dhuhr':dhuhr, 'dhuhr_j':dhuhr_j,'asr':asr,'asr_j':asr_j,'maghrib':maghrib,'maghrib_j':maghrib_j, 'isha':isha,'isha_j':isha_j,'month':mon, 'date':date, 'weekday':weekday,'day_no':day_no, 'day_ab':day_ab})
    return month_data

def month_view(request):
    month_data = get_month_tbl()
    context = {'d':json.dumps(month_data)}
    return render(request, 'posts/month.html', context)

def post_view(request, id):
    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request, 'posts/post_view.html', context)

@login_required
def post_form(request): 
    form = PostForm(request.POST, request.FILES) 
    if form.is_valid():
        form.save()
        return redirect('posts:home')
    else:
        form = PostForm()
        context = {'form':form}
        return render(request, 'posts/post_form.html', context)

@login_required
def edit_post_form(request, id): 
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts:post_view', kwargs={'id':id}))
    else:
        form = PostForm(instance=post)
        context = {'form':form, 'post':post}
        return render(request, 'posts/post_edit_form.html', context)

def post_list_view(request):
    posts = Post.objects.filter(type='News').order_by('-published_date').values()
    context = {'posts':posts}
    return render(request, 'posts/posts_list.html', context)

@login_required
def posts_admin(request):
    posts = Post.objects.filter(type='News').order_by('-published_date').values()
    context = {'posts':posts}
    return render(request, 'posts/posts_admin.html', context)


@require_http_methods(['DELETE'])
def delete_post(request, id):
    Post.objects.filter(id=id).delete()
    posts = Post.objects.filter(type='News').order_by('-published_date').values()
    return render(request, 'posts/partials/admin-posts-partial.html', {'posts': posts})

@login_required #@require_http_methods(['UPDATE'])
def hide_post_toggle(request, id):
    post = Post.objects.get(id=id)
    # print(f"Post ID: {post.id}")
    if not post.published:
        post.published = True
        post.save()
    else:
        post.published = False
        post.save()
    
    #post = Post.objects.get(id=id)
    return render(request, 'posts/partials/single_post.html', {'post': post})

class GeneratePdf(View): 
    def get(self, request, *args, **kwargs): 
        month_data = get_month_tbl()
        template = get_template('pdf/timetable.html')
        current_time = datetime.datetime.now()
        month = current_time.month
        year = current_time.year 
        context = {'data':month_data} 
        html = template.render(context) 
        pdf = render_to_pdf('pdf/timetable.html', context) 
        if pdf: 
            response = HttpResponse(pdf, content_type='application/pdf') 
            filename = f"Timetable_{month}_{year}.pdf" 
            content = "inline; filename='%s'" %(filename) 
            download = request.GET.get("download") 
            if download: 
                content = "attachment; filename='%s'" %(filename) 
            response['Content-Disposition'] = content 
            return response 
        return HttpResponse("Not found")