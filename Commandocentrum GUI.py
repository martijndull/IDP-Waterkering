#Deze code wordt gebruikt voor de grafische user interface voor de simulatie van het eerste commandocentrum
#toevoegen: weersomstandigheden via API, status / waarschuwing open/sluiten waterkering


"""
locatie
tijd
waterniveau
verwacht waterniveau
temperatuur
huidige omstandigheden (bewolking etc)
luchtvochtigheid
luchtdruk
windkracht
windrichting"""


from tkinter import *
import sys
import pywapi
import requests
import json

def waterstanden():
    """Haalt huidige waterstand op van rijkswaterstaat site"""
    r = requests.get('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=waterstanden&loadprojects=0')
    index_waterstand = 0
    global waterhoogte_hvh, waterhoogte_r, waterhoogte_d

    for i in r.json()['features']:
        if r.json()['features'][index_waterstand]['locatienaam'] == 'Hoek van Holland':
            waterhoogte_hvh = r.json()['features'][index_waterstand]['waarde'] + str("cm boven NAP")

        if r.json()['features'][index_waterstand]['locatienaam'] == 'Rotterdam':
            waterhoogte_r = r.json()['features'][index_waterstand]['waarde']  + str("cm boven NAP")

        if r.json()['features'][index_waterstand]['locatienaam'] == 'Dordrecht':
            waterhoogte_d = r.json()['features'][index_waterstand]['waarde']  + str("cm boven NAP")

        index_waterstand += 1

waterstanden()

def weersomstandigheden():
    """Haalt huidige weersomstandigheden van weather.com."""
    global weather_com_result_hvh, weather_com_result_r, weather_com_result_d

    weather_com_result_hvh = pywapi.get_weather_from_weather_com('NLXX0025')
    weather_com_result_r = pywapi.get_weather_from_weather_com('NLXX0015')
    weather_com_result_d = pywapi.get_weather_from_weather_com('NLXX0006')

weersomstandigheden()

#status van kering, input nog aanpassen als rest van code er is
status_maeslantkering = input("Maeslantkering: geopend/gesloten?")

def Commandocentrum_scherm():
    """Maakt GUI voor commandocentrum"""
    root = Tk()
    root.title("Commandocentrum Alpha")
    root.wm_state('zoomed')
    root.configure(background='white')

    weersvoorspelling_knop = Button(text='Weersvoorspelling', bg='#003399', fg='white')
    weersvoorspelling_knop.pack()
    weersvoorspelling_knop.place(width=150, height=50, relx=0.15, rely=0.90)

    waterstand_knop = Button(text='Archief waterstand', bg='#003399', fg='white')
    waterstand_knop.pack()
    waterstand_knop.place(width=150, height=50, relx=0.30, rely=0.90)

    waterkering_knop = Button(text='Logboek Maeslantkering', bg='#003399', fg='white')
    waterkering_knop.pack()
    waterkering_knop.place(width=150, height=50, relx=0.45, rely=0.90)


    def weer():
        """"Maakt tabel voor weersomstandigheden"""

        Label(text='Locatie', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
        Label(text='Tijd update', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW,)
        Label(text='Waterniveau', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW,)
        Label(text='Verwacht waterniveau', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW,)
        Label(text='Temperatuur', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)
        Label(text='Huidige omstandigheden', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0, sticky=NSEW)
        Label(text='Luchtvochtigheid', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=0, sticky=NSEW)
        Label(text='Luchtdruk', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=0, sticky=NSEW)
        Label(text='Windkracht', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=8,column=0, sticky=NSEW)
        Label(text='Richting', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=9,column=0, sticky=NSEW)

        #Hoek van Holland
        Label(text="Hoek van Holland", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW,)
        Label(text=weather_com_result_hvh['current_conditions']['last_updated'][0:15], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
        Label(text=waterhoogte_hvh, anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
        Label(text="placeholder", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['temperature'] + "°C", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1, sticky=NSEW,)
        Label(text=weather_com_result_hvh['current_conditions']['humidity'] + "%", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=8,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=9,column=1, sticky=NSEW)

        #Rotterdam
        Label(text="Rotterdam", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=2, sticky=NSEW,)
        Label(text=weather_com_result_r['current_conditions']['last_updated'][0:15], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW)
        Label(text=waterhoogte_r, anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2, sticky=NSEW)
        Label(text="placeholder", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['temperature'] + "°C", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2, sticky=NSEW,)
        Label(text=weather_com_result_r['current_conditions']['humidity'] + "%", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=8,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=9,column=2, sticky=NSEW)

        #Dordrecht
        Label(text="Dordrecht", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=3, sticky=NSEW,)
        Label(text=weather_com_result_d['current_conditions']['last_updated'][0:15], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW)
        Label(text=waterhoogte_d, anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3, sticky=NSEW)
        Label(text="placeholder", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['temperature'] + "°C", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3, sticky=NSEW,)
        Label(text=weather_com_result_d['current_conditions']['humidity'] + "%", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=8,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=9,column=3, sticky=NSEW)

        Label(text="Status:", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10,'bold')).grid(row=0, column=6, sticky=NSEW)
        Label(text="De Maeslantkering is op dit moment " + status_maeslantkering + ".", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10,'bold')).grid(row=1, column=6, sticky=NSEW)


    weer()
    mainloop()

Commandocentrum_scherm()

