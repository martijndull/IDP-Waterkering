"""Deze code wordt gebruikt voor de grafische user interface voor de simulatie van het eerste commandocentrum. Op het scherm worden de huidige weersomstandigheden, de huidige waterstand, de status van de Maeslantkering en een klok met de huidige tijd weergegeven."""

from tkinter import *
import sys
import pywapi
import requests
import json
import time

#status van kering, input nog aanpassen als rest van code er is.
status_maeslantkering = "geopend"

weather_com_pred_hvh = pywapi.get_weather_from_weather_com( 'NLXX0025', units = 'metric' )
weather_com_pred_r = pywapi.get_weather_from_weather_com( 'NLXX0015', units = 'metric' )
weather_com_pred_d = pywapi.get_weather_from_weather_com( 'NLXX0006', units = 'metric' )

global dag
dag = 1

def weersvoorspelling_scherm():
    root_wvs = Tk()
    root_wvs.title("Weersvoorspelling")
    root_wvs.wm_state('zoomed')

    weersvoorspelling_frame = LabelFrame(root_wvs, text="Weersomstandigheden", bg='white')
    weersvoorspelling_frame.grid()
    weersvoorspelling_frame.place(relx=0.05, rely=0.05)

    def weersvoorspelling():

        def volgende_dag():
            global dag
            dag += 1
            weersvoorspelling()


        def vorige_dag():
            global dag
            dag -= 1
            weersvoorspelling()

        if dag == 1:
            knop_status2 = DISABLED
        else:
            knop_status2 = NORMAL

        if dag == 4:
            knop_status1 = DISABLED
        else:
            knop_status1 = NORMAL

        def sluiten():
            root_wvs.destroy()

        weersvoorspelling_knop2 = Button(root_wvs, text='Vorige dag', bg='#003399', fg='white', command=vorige_dag, state=knop_status2)
        weersvoorspelling_knop2.pack()
        weersvoorspelling_knop2.place(width=150, height=50, relx=0.05, rely=0.90)

        weersvoorspelling_knop = Button(root_wvs, text='Volgende dag', bg='#003399', fg='white',  command=volgende_dag, state=knop_status1)
        weersvoorspelling_knop.pack()
        weersvoorspelling_knop.place(width=150, height=50, relx=0.15, rely=0.90)

        scherm_sluiten_knop = Button(root_wvs, text='Terug', bg='#003399', fg='white',  command=sluiten)
        scherm_sluiten_knop.pack()
        scherm_sluiten_knop.place(width=150, height=50, relx=0.25, rely=0.90)

        Label(weersvoorspelling_frame, text='Datum', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
        Label(weersvoorspelling_frame, text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW,)
        Label(weersvoorspelling_frame, text='Min / Max temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW)
        Label(weersvoorspelling_frame, text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW)
        Label(weersvoorspelling_frame, text='Regenkans', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)
        Label(weersvoorspelling_frame, text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0, sticky=NSEW)
        Label(weersvoorspelling_frame, text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=0, sticky=NSEW)
        Label(weersvoorspelling_frame, text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=0, sticky=NSEW)

        #datum
        Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][dag]['date'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW)

        #Hoek van Holland
        Label(weersvoorspelling_frame, text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW,)
        Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][dag]['low'] + "°C / " + weather_com_pred_hvh['forecasts'][dag]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][dag]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][dag]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][dag]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][dag]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=1, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][dag]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=1, sticky=NSEW)


        #Rotterdam
        Label(weersvoorspelling_frame, text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW,)
        Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][dag]['low'] + "°C / " + weather_com_pred_r['forecasts'][dag]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][dag]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][dag]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][dag]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][dag]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=2, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][dag]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=2, sticky=NSEW)


        #Dordrecht
        Label(weersvoorspelling_frame, text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW,)
        Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][dag]['low'] + "°C / " + weather_com_pred_d['forecasts'][dag]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][dag]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][dag]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][dag]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][dag]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=3, sticky=NSEW)
        Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][dag]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=3, sticky=NSEW)


    weersvoorspelling()

    mainloop()

def Commandocentrum_scherm():
    """Maakt GUI voor commandocentrum"""
    root = Tk()
    root.title("Commandocentrum Alpha")
    root.wm_state('zoomed')
    root.configure(background='#F0F2F2')

    weersvoorspelling_knop = Button(text='Weersvoorspelling', bg='#003399', fg='white', command=weersvoorspelling_scherm)
    weersvoorspelling_knop.pack()
    weersvoorspelling_knop.place(width=150, height=50, relx=0.15, rely=0.90)

    waterstand_knop = Button(text='Archief waterstand', bg='#003399', fg='white')
    waterstand_knop.pack()
    waterstand_knop.place(width=150, height=50, relx=0.30, rely=0.90)

    waterkering_knop = Button(text='Logboek Maeslantkering', bg='#003399', fg='white')
    waterkering_knop.pack()
    waterkering_knop.place(width=150, height=50, relx=0.45, rely=0.90)

    weer_frame = LabelFrame(root, text="Weersomstandigheden", bg='white')
    weer_frame.grid()
    weer_frame.place(relx=0.05, rely=0.05)

    bericht_frame = LabelFrame(root, text="Berichten", bg='white', padx=5, pady=5)
    bericht_frame.grid()
    bericht_frame.place(relx=0.55, rely=0.05)

    tijd_frame = LabelFrame(root, text="Tijd", bg='white', padx=5, pady=5)
    tijd_frame.grid()
    tijd_frame.place(relx=0.85, rely=0.05)

    def weersomstandigheden():
        """Haalt huidige weersomstandigheden van weather.com."""
        global weather_com_result_hvh, weather_com_result_r, weather_com_result_d

        weather_com_result_hvh = pywapi.get_weather_from_weather_com('NLXX0025', units='metric')
        weather_com_result_r = pywapi.get_weather_from_weather_com('NLXX0015', units='metric')
        weather_com_result_d = pywapi.get_weather_from_weather_com('NLXX0006', units='metric')

        root.after(60000, weersomstandigheden)

    def waterstanden():
        """Haalt huidige waterstand op van rijkswaterstaat site"""
        r = requests.get('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=waterstanden&loadprojects=0')
        index_waterstand = 0
        global waterhoogte_hvh, waterhoogte_r, waterhoogte_d

        for i in r.json()['features']:
            if r.json()['features'][index_waterstand]['locatienaam'] == 'Hoek van Holland':
                waterhoogte_hvh = r.json()['features'][index_waterstand]['waarde']

            if r.json()['features'][index_waterstand]['locatienaam'] == 'Rotterdam':
                waterhoogte_r = r.json()['features'][index_waterstand]['waarde']

            if r.json()['features'][index_waterstand]['locatienaam'] == 'Dordrecht':
                waterhoogte_d = r.json()['features'][index_waterstand]['waarde']

            index_waterstand += 1

        #kleur waterhoogte in tabel
        global kleur_waterhoogte_hvh, kleur_waterhoogte_r, kleur_waterhoogte_d

        if int(waterhoogte_hvh) >= 300:
            kleur_waterhoogte_hvh = 'red'
        else:
            kleur_waterhoogte_hvh = '#003399'

        if int(waterhoogte_r) >= 300:
            kleur_waterhoogte_r = 'red'
        else:
            kleur_waterhoogte_r = '#003399'

        if int(waterhoogte_d) >= 300:
            kleur_waterhoogte_d = 'red'
        else:
            kleur_waterhoogte_d = '#003399'

        root.after(60000, waterstanden)

    waterstanden()
    weersomstandigheden()

    def weer():
        """"Maakt tabel voor weersomstandigheden"""

        Label(weer_frame, text='Locatie', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=0,column=0, sticky=NSEW)
        Label(weer_frame, text='Tijd laatste update', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=1,column=0, sticky=NSEW)
        Label(weer_frame, text='Waterniveau', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=2,column=0, sticky=NSEW)
        Label(weer_frame, text='Verwacht waterniveau', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=3,column=0, sticky=NSEW)
        Label(weer_frame, text='Temperatuur', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=4,column=0, sticky=NSEW)
        Label(weer_frame, text='Huidige omstandigheden', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=5,column=0, sticky=NSEW)
        Label(weer_frame, text='Luchtvochtigheid', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=6,column=0, sticky=NSEW)
        Label(weer_frame, text='Luchtdruk', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=7,column=0, sticky=NSEW)
        Label(weer_frame, text='Windkracht', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=8,column=0, sticky=NSEW)
        Label(weer_frame, text='Richting', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=0, sticky=NSEW)

        #Hoek van Holland
        Label(weer_frame, text="Hoek van Holland", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=0,column=1, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_hvh['current_conditions']['last_updated'][0:16], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=1,column=1, sticky=NSEW)
        Label(weer_frame, text=waterhoogte_hvh + str("cm NAP"), anchor = NW, bg = 'white', fg=kleur_waterhoogte_hvh, font = ('Ariel',10, 'bold')).grid(ipadx=25, row=2,column=1, sticky=NSEW)
        Label(weer_frame, text="placeholder", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=3,column=1, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_hvh['current_conditions']['temperature'] + "°C", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=4,column=1, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_hvh['current_conditions']['text'], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=5,column=1, sticky=NSEW,)
        Label(weer_frame, text=weather_com_result_hvh['current_conditions']['humidity'] + "%", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=6,column=1, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_hvh['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=7,column=1, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_hvh['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=8,column=1, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_hvh['current_conditions']['wind']['text'], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=1, sticky=NSEW)

        #Rotterdam
        Label(weer_frame, text="Rotterdam", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx= 25, row=0,column=2, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_r['current_conditions']['last_updated'][0:16], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=1,column=2, sticky=NSEW)
        Label(weer_frame, text=waterhoogte_r + str("cm NAP"), anchor = NW, bg = 'white', fg=kleur_waterhoogte_r, font = ('Ariel',10, 'bold')).grid(ipadx=25, row=2,column=2, sticky=NSEW)
        Label(weer_frame, text="placeholder", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=3,column=2, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_r['current_conditions']['temperature'] + "°C", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=4,column=2, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_r['current_conditions']['text'], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=5,column=2, sticky=NSEW,)
        Label(weer_frame, text=weather_com_result_r['current_conditions']['humidity'] + "%", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=6,column=2, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_r['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=7,column=2, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_r['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=8,column=2, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_r['current_conditions']['wind']['text'], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=2, sticky=NSEW)

        #Dordrecht
        Label(weer_frame, text="Dordrecht", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=0,column=3, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_d['current_conditions']['last_updated'][0:16], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=1,column=3, sticky=NSEW)
        Label(weer_frame, text=waterhoogte_d + str("cm NAP"), anchor = NW, bg = 'white', fg=kleur_waterhoogte_d, font = ('Ariel',10, 'bold')).grid(ipadx=25, row=2,column=3, sticky=NSEW)
        Label(weer_frame, text="placeholder", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=3,column=3, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_d['current_conditions']['temperature'] + "°C", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=4,column=3, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_d['current_conditions']['text'], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=5,column=3, sticky=NSEW,)
        Label(weer_frame, text=weather_com_result_d['current_conditions']['humidity'] + "%", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=6,column=3, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_d['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=7,column=3, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_d['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=8,column=3, sticky=NSEW)
        Label(weer_frame, text=weather_com_result_d['current_conditions']['wind']['text'], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=3, sticky=NSEW)

        weer_frame.after(60000, weer)

    def status_waarschuwing():
        """Status van de Maeslantkering en eventuele waarschuwingen"""
        Label(bericht_frame, text="Status:", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10,'bold')).grid(row=1, column=0, sticky=NSEW)
        Label(bericht_frame, text="De Maeslantkering is op dit moment " + status_maeslantkering + ".", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10,'bold')).grid(row=2, column=0, sticky=NSEW)

        Label(bericht_frame, text="Waarschuwingen:", anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=3, column=0, sticky=NSEW)
        Label(bericht_frame, text="waarschuwing invoegen", anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=4, column=0, sticky=NSEW)

        bericht_frame.after(10000, status_waarschuwing)

    def update_clock():
        now = time.strftime("%I:%M %p")
        date = time.strftime("%a, %m/%d/%Y")
        Label(tijd_frame, text=now, font=20, bg= 'white').grid(sticky=E, row=0, column=0)
        Label(tijd_frame, text=date, font=20, bg= 'white').grid(sticky=E, row=1, column=0)
        tijd_frame.after(1000, update_clock)

    weer()
    status_waarschuwing()
    update_clock()
    mainloop()

Commandocentrum_scherm()