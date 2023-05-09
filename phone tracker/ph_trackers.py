import phonenumbers
from phonenumbers import geocoder
import folium
from phone_number import numb

key = "Input your API key from OpenCage Geocode site"

check_number = phonenumbers.parse(numb)

location = geocoder.description_for_number(check_number, "en")

print(f"location is: {location}")

from phonenumbers import carrier

serv_prov = phonenumbers.parse(numb)

print(carrier.name_for_number(serv_prov, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)
query = str(location)

results = geocoder.geocode(query)

lat = results[0]["geometry"]["lat"]

lng = results[0]["geometry"]["lng"]

print(lat, lng)

map_location = folium.Map(location=[lat, lng], zoom_start=20)

folium.Marker([lat, lng], popup=location).add_to(map_location)

map_location.save("mylocation.html")

location = (lat, lng)

rev_result = geocoder.reverse_geocode(lat, lng)

print(rev_result)
