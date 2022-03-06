from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import MasjidEditForm
from .models import *
# Create your views here.

masjid = CentreProfile.objects.get()
masjid_name = masjid.masjid_name


@login_required
def edit_profile(request):  
    if request.method == 'POST':
        user_form = MasjidEditForm(data=request.POST or None, instance=masjid)
        
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('masjidConfig:edit_profile'))
    else:
        user_form = MasjidEditForm(data=request.POST or None, instance=masjid)
    context = {
        'user_form':user_form,
        'masjid_name':masjid_name,
        }
    return render(request, 'masjidConfig/edit_profile.html', context)