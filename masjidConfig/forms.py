from django.forms import ModelForm,widgets
from django.forms.widgets import TextInput, EmailInput
from .models import *
from django import forms

class MasjidEditForm(forms.ModelForm):
    class Meta:
        model = CentreProfile
        fields = '__all__'
        widgets = {
            'mainColour': TextInput(attrs={'type': 'color'}),
            'accentColour': TextInput(attrs={'type': 'color'}),
            'email': EmailInput(attrs={
                'class':'input is-primary',
                'type': 'email',
                'placeholder':'Email'
            }),

        }
    maintenance_mode = models.BooleanField(default=False)
    masjid_name = models.CharField(max_length=255, default='Open Mosque Project')
    masjidLogo = models.ImageField(upload_to='images/', default='images/gsm_logo.png')
    city = models.CharField(max_length=255, default='London')
    country = models.CharField(max_length=255, default='GB')    
    method = models.IntegerField(max_length=2, choices=PRAYER_CALC_CHOICES, default=3)
    shafaq = models.CharField(max_length=10, choices=SHAFAQ_CHOICES, default=GEN)
    school = models.IntegerField(choices=SCHOOL_CHOICES, default=SHAFI)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=51.443909)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.219730)
    fajr_jamaah_minutes = models.CharField(max_length=255, choices=FAJR_JAMAAH)
    dhuhr_jamaah_minutes = models.CharField(max_length=255, choices=DHUHR_JAMAAH)
    asr_jamaah_minutes = models.CharField(max_length=255, choices=ASR_JAMAAH)
    maghrib_jamaah_minutes = models.CharField(max_length=255, choices=MAGHRIB_JAMAAH)
    isha_jamaah_minutes = models.CharField(max_length=255, choices=ISHA_JAMAAH)
    landline = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)