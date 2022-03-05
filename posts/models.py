from django.db import models
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage
from solo.models import SingletonModel

SHIA = 0
UIS = 1
ISNA = 2
MWL = 3
UAU = 4
EGAU = 5
IGUT = 7
GR = 8
KUW = 9
QAT = 10
MUIS = 11
UOIF = 12
DIBT = 13
PRAYER_CALC_CHOICES = [
    (SHIA, "Shia Ithna-Ansari"),
    (UIS, "University of Islamic Sciences, Karachi"),
    (ISNA, "Islamic Society of North America"),
    (MWL,"Muslim World League"),
    (UAU,"Umm Al-Qura University, Makkah"),
    (EGAU,"Egyptian General Authority of Survey"),
    (IGUT,"Institute of Geophysics, University of Tehran"),
    (GR,"Gulf Region"),
    (KUW,"Kuwait"),
    (QAT,"Qatar"),
    (MUIS,"Majlis Ugama Islam Singapura, Singapore"),
    (UOIF,"Union Organization islamic de France"),
    (DIBT,"Diyanet İşleri Başkanlığı, Türkiye")
]

GEN = 'general'
AHM = 'ahmer'
ABY = 'abyad'
SHAFAQ_CHOICES = [
    (GEN, 'General'),
    (AHM, 'Ahmer'),
    (ABY, 'Abyad'),
]

SHAFI = 0
HANIFI = 1
SCHOOL_CHOICES = [
    (SHAFI,"Shafii (the standard method)"),
    (HANIFI,"Hanafi"),
]

FIVE = "5"
TEN = "10"
FIFTEEN = "15"
NEAREST_FIFTEEN = "round_to_fifteen"
NEAREST_THIRTY = "round_to_thirty"   

FAJR_JAMAAH = [
    (FIVE, "Jamaah is 5 minutes after Iqamah"),
    (TEN, "Jamaah is 10 minutes after Iqamah"),
    (FIFTEEN, "Jamaah is 15 minutes after Iqamah"),
    (NEAREST_FIFTEEN, "Jamaah is rounded to closest 15 minutes after Iqamah"),
    (NEAREST_THIRTY, "Jamaah is rounded to closest 30 minutes after Iqamah"),
]

DHUHR_JAMAAH = [
    (FIVE, "Jamaah is 5 minutes after Iqamah"),
    (TEN, "Jamaah is 10 minutes after Iqamah"),
    (FIFTEEN, "Jamaah is 15 minutes after Iqamah"),
    (NEAREST_FIFTEEN, "Jamaah is rounded to closest 15 minutes after Iqamah"),
    (NEAREST_THIRTY, "Jamaah is rounded to closest 30 minutes after Iqamah"),
]

ASR_JAMAAH = [
    (FIVE, "Jamaah is 5 minutes after Iqamah"),
    (TEN, "Jamaah is 10 minutes after Iqamah"),
    (FIFTEEN, "Jamaah is 15 minutes after Iqamah"),
    (NEAREST_FIFTEEN, "Jamaah is rounded to closest 15 minutes after Iqamah"),
    (NEAREST_THIRTY, "Jamaah is rounded to closest 30 minutes after Iqamah"),
]

MAGHRIB_JAMAAH = [
    (FIVE, "Jamaah is 5 minutes after Iqamah"),
    (TEN, "Jamaah is 10 minutes after Iqamah"),
    (FIFTEEN, "Jamaah is 15 minutes after Iqamah"),
    (NEAREST_FIFTEEN, "Jamaah is rounded to closest 15 minutes after Iqamah"),
    (NEAREST_THIRTY, "Jamaah is rounded to closest 30 minutes after Iqamah"),
]

ISHA_JAMAAH = [
    (FIVE, "Jamaah is 5 minutes after Iqamah"),
    (TEN, "Jamaah is 10 minutes after Iqamah"),
    (FIFTEEN, "Jamaah is 15 minutes after Iqamah"),
    (NEAREST_FIFTEEN, "Jamaah is rounded to closest 15 minutes after Iqamah"),
    (NEAREST_THIRTY, "Jamaah is rounded to closest 30 minutes after Iqamah"),
]

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = VersatileImageField('Image', upload_to='images/', 
            blank=True,
            placeholder_image=OnStoragePlaceholderImage(
                path='images/default_image.jpg'
        ))

    def __str__(self):
        return self.title

# Site settings model
class CentreProfile(SingletonModel):
    maintenance_mode = models.BooleanField(default=False)
    masjid_name = models.CharField(max_length=255, default='Open Mosque Project')
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

    
    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
    
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