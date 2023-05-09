import phonenumbers
from phonenumbers import geocoder
import folium
from opencage.geocoder import OpenCageGeocode
location = (-86.000977, -86.000977)

result = geocoder.reverse_geocode(location)

print (result)