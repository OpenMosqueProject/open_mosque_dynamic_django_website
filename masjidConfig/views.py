from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import lru_cache

from .forms import MasjidEditForm
from .models import *


@login_required
def edit_profile(request):  
    masjid = CentreProfile.load()    
    if request.method == 'POST':
        user_form = MasjidEditForm(request.POST, request.FILES, instance=masjid)
        
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('masjidConfig:edit_profile'))
    else:
        # Force reload from database
        masjid.refresh_from_db()
        user_form = MasjidEditForm(instance=masjid)
    
    context = {
        'form':user_form,
        'masjid':masjid,
        }
    return render(request, 'masjidConfig/edit_profile.html', context)

@lru_cache(maxsize=1)
def about(request):  
    masjid = CentreProfile.load()  
    context = {
        'masjid':masjid,
        }
    return render(request, 'masjidConfig/about.html', context)
