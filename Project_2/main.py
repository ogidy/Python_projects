# First install the package "phonenumbers" (pip install phonenumbers)
# The import the package here

import phonenumbers
from test import number

from phonenumbers import geocoder

#below is to show phone number location
ch_number = phonenumbers.parse(number, "CH")

print(geocoder.description_for_number(ch_number, "en"))

