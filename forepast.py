import requests

def get(date, state, city):
	date = date.strftime('%Y%m%d')
	r = requests.get("http://api.wunderground.com/api/da56b35422df63cd/history_%s/q/%s/%s.json" % (date,state,city))
	return r.json()

def ziptocity(zipcode):
	location = requests.get("http://api.wunderground.com/api/da56b35422df63cd/geolookup/q/%s.json" % (zipcode)).json().get('location')
	state = location.get('state')
	city = location.get('city').replace(" ", "_")
	return(city, state)

def cordstocity(latitude, longitude):
	location = requests.get("http://api.wunderground.com/api/da56b35422df63cd/geolookup/q/%s,%s.json" % (latitude,longitude)).json().get('location')
	state = location.get('state')
	city = location.get('city').replace(" ", "_")
	return (city, state)