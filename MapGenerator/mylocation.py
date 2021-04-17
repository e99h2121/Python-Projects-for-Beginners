## https://qiita.com/shira11/items/58a186fde9d22a88b3d3
## https://qiita.com/pork_steak/items/f551fa09794831100faa

import folium
from geopy.geocoders import Nominatim

location = input("場所を入力:")
copyright_osm = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'

geolocator = Nominatim(user_agent="test")
location = geolocator.geocode(location)
lat, long = location.latitude, location.longitude
print("full address = ", location.address)

map = folium.Map(location=[lat, long],
  attr=copyright_osm,
)
map.save("mylocation.html")
