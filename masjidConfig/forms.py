from django.forms import ModelForm, widgets
from django.forms.widgets import TextInput, EmailInput
from .models import *
from django import forms
from.constants import PRAYER_CALC_CHOICES, SHAFAQ_CHOICES, SCHOOL_CHOICES, FAJR_JAMAAH, DHUHR_JAMAAH, ASR_JAMAAH, MAGHRIB_JAMAAH, ISHA_JAMAAH, COLOR_CHOICES, SHAFI, GEN
import json

class MasjidEditForm(forms.ModelForm):
    class Meta:
        model = CentreProfile
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={
                'class':'input is-primary',
                'type': 'email',
                'placeholder':'Email'
            }),
            'weekly_schedule': forms.HiddenInput(),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        
        # Parse the weekly_schedule JSON from the hidden input
        if 'weekly_schedule' in self.data:
            try:
                weekly_schedule_json = self.data['weekly_schedule']
                # Parse and revalidate the JSON
                schedule = json.loads(weekly_schedule_json)
                cleaned_data['weekly_schedule'] = schedule
            except (json.JSONDecodeError, KeyError) as e:
                self.add_error('weekly_schedule', f'Invalid schedule format: {str(e)}')
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Ensure weekly_schedule is set from cleaned_data
        if 'weekly_schedule' in self.cleaned_data:
            instance.weekly_schedule = self.cleaned_data['weekly_schedule']
        
        if commit:
            instance.save()
        
        return instance