from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as trans # for translating text


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


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
    (SHIA, trans("Shia Ithna-Ansari")),
    (UIS, trans("University of Islamic Sciences, Karachi")),
    (ISNA, trans("Islamic Society of North America")),
    (MWL,trans("Muslim World League")),
    (UAU,trans("Umm Al-Qura University, Makkah")),
    (EGAU,trans("Egyptian General Authority of Survey")),
    (IGUT,trans("Institute of Geophysics, University of Tehran")),
    (GR,trans("Gulf Region")),
    (KUW,trans("Kuwait")),
    (QAT,trans("Qatar")),
    (MUIS,trans("Majlis Ugama Islam Singapura, Singapore")),
    (UOIF,trans("Union Organization islamic de France")),
    (DIBT,trans("Diyanet İşleri Başkanlığı, Türkiye"))
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
    (FIVE, trans("Jamaat (Iqamah) is 5 minutes after Azan")),
    (TEN, trans("Jamaat (Iqamah) is 10 minutes after Azan")),
    (FIFTEEN, trans("Jamaat (Iqamah) is 15 minutes after Azan")),
    (NEAREST_FIFTEEN, trans("Jamaat (Iqamah) is rounded to closest 15 minutes after Azan")),
    (NEAREST_THIRTY, trans("Jamaat (Iqamah) is rounded to closest 30 minutes after Azan")),
]

DHUHR_JAMAAH = [
    (FIVE, trans("Jamaat (Iqamah) is 5 minutes after Azan")),
    (TEN, trans("Jamaat (Iqamah) is 10 minutes after Azan")),
    (FIFTEEN, trans("Jamaat (Iqamah) is 15 minutes after Azan")),
    (NEAREST_FIFTEEN, trans("Jamaat (Iqamah) is rounded to closest 15 minutes after Azan")),
    (NEAREST_THIRTY, trans("Jamaat (Iqamah) is rounded to closest 30 minutes after Azan")),
]

ASR_JAMAAH = [
    (FIVE, trans("Jamaat (Iqamah) is 5 minutes after Azan")),
    (TEN, trans("Jamaat (Iqamah) is 10 minutes after Azan")),
    (FIFTEEN, trans("Jamaat (Iqamah) is 15 minutes after Azan")),
    (NEAREST_FIFTEEN, trans("Jamaat (Iqamah) is rounded to closest 15 minutes after Azan")),
    (NEAREST_THIRTY, trans("Jamaat (Iqamah) is rounded to closest 30 minutes after Azan")),
]

MAGHRIB_JAMAAH = [
    (FIVE, trans("Jamaat (Iqamah) is 5 minutes after Azan")),
    (TEN, trans("Jamaat (Iqamah) is 10 minutes after Azan")),
    (FIFTEEN, trans("Jamaat (Iqamah) is 15 minutes after Azan")),
    (NEAREST_FIFTEEN, trans("Jamaat (Iqamah) is rounded to closest 15 minutes after Azan")),
    (NEAREST_THIRTY, trans("Jamaat (Iqamah) is rounded to closest 30 minutes after Azan")),
]

ISHA_JAMAAH = [
    (FIVE, trans("Jamaat (Iqamah) is 5 minutes after Azan")),
    (TEN, trans("Jamaat (Iqamah) is 10 minutes after Azan")),
    (FIFTEEN, trans("Jamaat (Iqamah) is 15 minutes after Azan")),
    (NEAREST_FIFTEEN, trans("Jamaat (Iqamah) is rounded to closest 15 minutes after Azan")),
    (NEAREST_THIRTY, trans("Jamaat (Iqamah) is rounded to closest 30 minutes after Azan")),
]

# Site settings model
class CentreProfile(SingletonModel):
    maintenance_mode = models.BooleanField(default=False)
    masjid_Name = models.CharField(trans("Name of mosque"), max_length=255, default='Open Mosque Project')
    masjid_Logo = models.ImageField(upload_to='images/', default='images/gsm_logo.png')
    masjid_Photo = models.ImageField(upload_to='images/', blank=True)
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
    fajr_jamaah_minutes = models.CharField(max_length=255, choices=FAJR_JAMAAH, blank=True)
    dhuhr_jamaah_minutes = models.CharField(max_length=255, choices=DHUHR_JAMAAH, blank=True)
    asr_jamaah_minutes = models.CharField(max_length=255, choices=ASR_JAMAAH, blank=True)
    maghrib_jamaah_minutes = models.CharField(max_length=255, choices=MAGHRIB_JAMAAH, blank=True)
    isha_jamaah_minutes = models.CharField(max_length=255, choices=ISHA_JAMAAH, blank=True)
    mainColour = models.CharField(max_length=7, default='#0d6efd')
    accentColour = models.CharField(max_length=7, default='#adb5bd')
    facebook = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
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
