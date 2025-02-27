from django.utils.translation import gettext as trans # for translating text

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

COLOR_CHOICES = (
    ('light', 'light'),
    ('dark', 'dark'),
    ('cupcake', 'cupcake'),
    ('bumblebee', 'bumblebee'),
    ('emerald', 'emerald'),
    ('corporate', 'corporate'),
    ('synthwave', 'synthwave'),
    ('retro', 'retro'),
    ('cyberpunk', 'cyberpunk'),
    ('valentine', 'valentine'),
    ('halloween', 'halloween'),
    ('garden', 'garden'),
    ('forest', 'forest'),
    ('aqua', 'aqua'),
    ('lofi', 'lofi'),
    ('pastel', 'pastel'),
    ('fantasy', 'fantasy'),
    ('wireframe', 'wireframe'),
    ('black', 'black'),
    ('luxury', 'luxury'),
    ('dracula', 'dracula'),
    ('cmyk', 'cmyk'),
    ('autumn', 'autumn'),
    ('business', 'business'),
    ('acid', 'acid'),
    ('lemonade', 'lemonade'),
    ('night', 'night'),
    ('coffee', 'coffee'),
    ('winter', 'winter'),
)