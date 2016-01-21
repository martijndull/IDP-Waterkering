import requests, json

def waterstanden():
    r = requests.get('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=waterstanden&loadprojects=0')
    index = 0
    global waterhoogte_hvh, waterhoogte_r, waterhoogte_d

    for i in r.json()['features']:
        if r.json()['features'][index]['locatienaam'] == 'Hoek van Holland':
            waterhoogte_hvh = r.json()['features'][index]['waarde'] + str("cm boven NAP")

        if r.json()['features'][index]['locatienaam'] == 'Rotterdam':
            waterhoogte_r = r.json()['features'][index]['waarde']  + str("cm boven NAP")

        if r.json()['features'][index]['locatienaam'] == 'Dordrecht':
            waterhoogte_d = r.json()['features'][index]['waarde']  + str("cm boven NAP")

        index += 1

waterstanden()

print (waterhoogte_hvh)