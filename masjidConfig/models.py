from email.policy import default
from django.db import models
from django.utils.translation import gettext as trans # for translating text

from .singleton import SingletonModel
from.constants import PRAYER_CALC_CHOICES, SHAFAQ_CHOICES, SCHOOL_CHOICES, FAJR_JAMAAH, DHUHR_JAMAAH, ASR_JAMAAH, MAGHRIB_JAMAAH, ISHA_JAMAAH, COLOR_CHOICES, SHAFI, GEN

# Default schedule: Open Monday-Friday with all prayers, closed weekends
DEFAULT_SCHEDULE = {
    "monday": {"open": True, "fajr_jamaah": True, "dhuhr_jamaah": True, "asr_jamaah": True, "maghrib_jamaah": True, "isha_jamaah": True},
    "tuesday": {"open": True, "fajr_jamaah": True, "dhuhr_jamaah": True, "asr_jamaah": True, "maghrib_jamaah": True, "isha_jamaah": True},
    "wednesday": {"open": True, "fajr_jamaah": True, "dhuhr_jamaah": True, "asr_jamaah": True, "maghrib_jamaah": True, "isha_jamaah": True},
    "thursday": {"open": True, "fajr_jamaah": True, "dhuhr_jamaah": True, "asr_jamaah": True, "maghrib_jamaah": True, "isha_jamaah": True},
    "friday": {"open": True, "fajr_jamaah": True, "dhuhr_jamaah": True, "asr_jamaah": True, "maghrib_jamaah": True, "isha_jamaah": True},
    "saturday": {"open": True, "fajr_jamaah": True, "dhuhr_jamaah": True, "asr_jamaah": True, "maghrib_jamaah": True, "isha_jamaah": True},
    "sunday": {"open": True, "fajr_jamaah": True, "dhuhr_jamaah": True, "asr_jamaah": True, "maghrib_jamaah": True, "isha_jamaah": True},
}

def get_default_schedule():
    return DEFAULT_SCHEDULE.copy()
# Create your models here.

class Theme(models.Model):
    color = models.CharField(max_length=100, choices=COLOR_CHOICES, default='light')
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default="light" , related_name='user_theme')

    def __str__(self):
        return f"{self.color}"
    
class CentreProfile(SingletonModel):
    maintenance_mode = models.BooleanField(default=False)
    masjid_Name = models.CharField(trans("Name of mosque"), max_length=255, default='Open Mosque Project')
    masjid_Logo = models.ImageField(upload_to='images/', default='images/gsm_logo.png')
    masjid_Photo = models.ImageField(upload_to='images/', blank=True)
    established = models.DateField(blank=True, null=True)
    about = models.TextField(max_length=2000, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    town = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, default='London')
    country = models.CharField(max_length=255, default='GB')
    postcode = models.CharField(max_length=10, blank=True)    
    method = models.IntegerField(choices=PRAYER_CALC_CHOICES, default=3)
    shafaq = models.CharField(max_length=10, choices=SHAFAQ_CHOICES, default=GEN)
    school = models.IntegerField(choices=SCHOOL_CHOICES, default=SHAFI)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=51.443909)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.219730)
    
    # Weekly schedule: which days open and which prayers have jamaah each day
    weekly_schedule = models.JSONField(default=get_default_schedule, help_text="Schedule of operating days and prayers with jamaah times")
    
    # Jamaah timing fields (for adjusting jamaah times relative to prayer times)
    fajr_jamaah_minutes = models.CharField(max_length=255, choices=FAJR_JAMAAH, blank=True)
    dhuhr_jamaah_minutes = models.CharField(max_length=255, choices=DHUHR_JAMAAH, blank=True)
    asr_jamaah_minutes = models.CharField(max_length=255, choices=ASR_JAMAAH, blank=True)
    maghrib_jamaah_minutes = models.CharField(max_length=255, choices=MAGHRIB_JAMAAH, blank=True)
    isha_jamaah_minutes = models.CharField(max_length=255, choices=ISHA_JAMAAH, blank=True)
    
    theme_choice = models.CharField(max_length=255, choices=COLOR_CHOICES, default='light')
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    tiktok = models.CharField(max_length=255, blank=True)
    imam = models.CharField(max_length=255, blank=True)
    landline = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    what3words = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return trans(f"{self.masjid_Name} Site Configuration")

    class Meta:
        verbose_name = trans("Site Configuration")
    
    """
    Adjustments we have not currently added

    Tune - "tune" (string) -
    Comma Separated String of integers to offset timings returned by the API in minutes. Example: 5,3,5,7,9,7. See https://aladhan.com/calculation-methods
    
    "midnightMode" (number) -
    0 for Standard (Mid Sunset to Sunrise), 1 for Jafari (Mid Sunset to Fajr). If you leave this empty, it defaults to Standard.

    "timezonestring" (string) -
    A valid timezone name as specified on http://php.net/manual/en/timezones.php . Example: Europe/London. If you do not specify this, we'll calcuate it using the co-ordinates you provide.

    "latitudeAdjustmentMethod" (number) -
    Method for adjusting times higher latitudes - for instance, if you are checking timings in the UK or Sweden.
    1 - Middle of the Night
    2 - One Seventh
    3 - Angle Based

    "adjustment" (number) -
    Number of days to adjust hijri date(s). Example: 1 or 2 or -1 or -2
    """

