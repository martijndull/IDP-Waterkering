"""Deze code wordt gebruikt voor de grafische user interface voor de simulatie van het eerste commandocentrum. Op het scherm worden de huidige weersomstandigheden, de huidige waterstand, de status van de Maeslantkering en een klok met de huidige tijd weergegeven."""

from tkinter import *
import tkinter
import sys
import pywapi
import requests
import json
import time
import tkinter.messagebox as tm
from weersvoorspelling import weersvoorspelling_scherm
from login import login
from PIL import Image, ImageTk
import io
import urllib.request as ur

global bericht_r, bericht_d, status_kering, geen_webcam, geen_klok, geen_weersomstandigheden, geen_waterstand, geen_weertabel
bericht_r = ""
bericht_d = ""
status_kering = ""
geen_webcam = ""
geen_klok = ""
geen_weersomstandigheden = ""
geen_waterstand = ""
geen_weertabel = ""

def Commandocentrum_scherm():
    """Maakt GUI voor commandocentrum"""
    root = Tk()
    root.title("Commandocentrum Alpha")
    #root.wm_state('zoomed')
    root.attributes("-fullscreen", True)

    bottomframe = Frame(root, bg='#6399E6', width=1700, height=70)
    bottomframe.grid()
    bottomframe.pack_propagate(0)
    bottomframe.place(rely=0.92)

    commandocentrum_tekst = Frame(root, bg='#F0F2F2')
    commandocentrum_tekst.grid()
    commandocentrum_tekst.place(relx=0.05, rely=0.01)

    Label(commandocentrum_tekst, text='Maeslantkering Commandocentrum Alpha', anchor = NW, bg='#F0F2F2', fg='#003399', font = ('Ariel',18, 'bold')).grid(row=1,column=0, ipadx=5, sticky=NSEW,)


    weersvoorspelling_knop = Button(text='Weersvoorspelling', bg='#003399', fg='white', command=weersvoorspelling_scherm)
    weersvoorspelling_knop.pack()
    weersvoorspelling_knop.place(width=150, height=50, relx=0.05, rely=0.93)

    waterkering_knop = Button(text='Logboek Maeslantkering', bg='#003399', fg='white')
    waterkering_knop.pack()
    waterkering_knop.place(width=150, height=50, relx=0.15, rely=0.93)

    afsluiten_knop = Button(text='Afsluiten', bg='#003399', fg='white', command=login)
    afsluiten_knop.pack()
    afsluiten_knop.place(width=150, height=50, relx=0.85, rely=0.93)

    weer_frame = LabelFrame(root, text="Weersomstandigheden", bg='white')
    weer_frame.grid()
    weer_frame.place(relx=0.05, rely=0.05)

    bericht_frame = LabelFrame(root, text="Berichten", bg='white', width=641, height=742)
    bericht_frame.grid()
    bericht_frame.grid_propagate(False)
    bericht_frame.place(relx=0.55, rely=0.05)

    tijd_frame = LabelFrame(root, text="Tijd", bg='white', padx=5, pady=5)
    tijd_frame.grid()
    tijd_frame.place(relx=0.86, rely=0.05)

    def lezen():
        global bericht_r, bericht_d, status_kering
        try:
            try:
                bestandr = open('waterstandrotterdam.txt', 'r')
                datar=bestandr.read()
                bestandr.close()
            except:
                print("Kan waterstandrotterdam.txt niet lezen.")

            if datar == "laag":
                bericht_r = "De waterstand in Rotterdam is op dit moment laag."
            elif datar == "hoog":
                bericht_r = "De waterstand in Rotterdam is op dit moment hoog."

            try:
                bestandd = open('waterstanddordrecht.txt', 'r')
                datad=bestandd.read()
                bestandd.close()
            except:
                print("Kan waterstanddordrecht.txt niet lezen")

            if datad == "laag":
                bericht_d = "De waterstand in Dordrecht is op dit moment laag."
            elif datad == "hoog":
                bericht_d = "De waterstand in Dordrecht is op dit moment hoog."

            if datad == "laag" and datar == "laag":
                status_kering = "geopend"
            elif datad == "hoog" or datar == "hoog":
                status_kering = "gesloten"
        except:
            print("Fout.")

        root.after(1000, lezen)

    def webcam():
        global geen_webcam
        try:
            URL = "http://webcams.dirkzwager.com/cam_hvh.jpg"
            u = ur.urlopen(URL)

            s = io.BytesIO(u.read())
            pil_image = Image.open(s)
            tk_image = ImageTk.PhotoImage(pil_image)
            Label = tkinter.Label(root, image=tk_image)
            Label.image = tk_image
            Label.place(relx=0.08, rely=0.35)
            geen_webcam = ""
        except:
            geen_webcam = "Er is geen verbinding met de webcam. Controleer de internetverbinding."
        root.after(30000, webcam)


    def weersomstandigheden():
        """Haalt huidige weersomstandigheden van weather.com."""
        global weather_com_result_hvh, weather_com_result_r, weather_com_result_d
        weather_com_result_hvh = pywapi.get_weather_from_weather_com('NLXX0025', units='metric')
        weather_com_result_r = pywapi.get_weather_from_weather_com('NLXX0015', units='metric')
        weather_com_result_d = pywapi.get_weather_from_weather_com('NLXX0006', units='metric')

        root.after(60000, weersomstandigheden)

    def waterstanden():
        """Haalt huidige waterstand op van rijkswaterstaat site"""
        global waterhoogte_hvh, waterhoogte_r, waterhoogte_d, kleur_waterhoogte_hvh, kleur_waterhoogte_r, kleur_waterhoogte_d, geen_waterstand

        try:
            r = requests.get('http://www.rijkswaterstaat.nl/apps/geoservices/rwsnl/?mode=features&projecttype=waterstanden&loadprojects=0')
            index_waterstand = 0

            for i in r.json()['features']:
                if r.json()['features'][index_waterstand]['locatienaam'] == 'Hoek van Holland':
                    waterhoogte_hvh = r.json()['features'][index_waterstand]['waarde']

                if r.json()['features'][index_waterstand]['locatienaam'] == 'Rotterdam':
                    waterhoogte_r = r.json()['features'][index_waterstand]['waarde']

                if r.json()['features'][index_waterstand]['locatienaam'] == 'Dordrecht':
                    waterhoogte_d = r.json()['features'][index_waterstand]['waarde']

                index_waterstand += 1

            #kleur waterhoogte in tabel
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

            geen_waterstand = ""
        except:
            geen_waterstand = "Kan actuele waterstand niet ophalen. Controleer de internetverbinding."

        root.after(60000, waterstanden)

    waterstanden()
    weersomstandigheden()

    def weer():
        global geen_weertabel
        """"Maakt tabel voor weersomstandigheden"""
        try:

            #Hoek van Holland
            Label(weer_frame, text=weather_com_result_hvh['current_conditions']['last_updated'][0:16], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=1,column=1, sticky=NSEW)
            #Label(weer_frame, text="placeholder", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=3,column=1, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_hvh['current_conditions']['temperature'] + "°C", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=4,column=1, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_hvh['current_conditions']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=5,column=1, sticky=NSEW,)
            Label(weer_frame, text=weather_com_result_hvh['current_conditions']['humidity'] + "%", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=6,column=1, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_hvh['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=7,column=1, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_hvh['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=8,column=1, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_hvh['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=1, sticky=NSEW)
            Label(weer_frame, text="Hoek van Holland", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=0,column=1, sticky=NSEW)

            #Rotterdam
            Label(weer_frame, text=weather_com_result_r['current_conditions']['last_updated'][0:16], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=1,column=2, sticky=NSEW)
            #Label(weer_frame, text="placeholder", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=3,column=2, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_r['current_conditions']['temperature'] + "°C", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=4,column=2, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_r['current_conditions']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=5,column=2, sticky=NSEW,)
            Label(weer_frame, text=weather_com_result_r['current_conditions']['humidity'] + "%", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=6,column=2, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_r['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=7,column=2, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_r['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=8,column=2, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_r['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=2, sticky=NSEW)
            Label(weer_frame, text="Rotterdam", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx= 25, row=0,column=2, sticky=NSEW)

            #Dordrecht
            Label(weer_frame, text=weather_com_result_d['current_conditions']['last_updated'][0:16], anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=1,column=3, sticky=NSEW)
            #Label(weer_frame, text="placeholder", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=3,column=3, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_d['current_conditions']['temperature'] + "°C", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=4,column=3, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_d['current_conditions']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=5,column=3, sticky=NSEW,)
            Label(weer_frame, text=weather_com_result_d['current_conditions']['humidity'] + "%", anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=6,column=3, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_d['current_conditions']['barometer']['reading'] + "mb", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=7,column=3, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_d['current_conditions']['wind']['speed'] + str("km/h"), anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=8,column=3, sticky=NSEW)
            Label(weer_frame, text=weather_com_result_d['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=3, sticky=NSEW)
            Label(weer_frame, text="Dordrecht", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=0,column=3, sticky=NSEW)

            Label(weer_frame, text='Locatie', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=0,column=0, sticky=NSEW)
            Label(weer_frame, text='Tijd laatste update', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=1,column=0, sticky=NSEW)
            Label(weer_frame, text='Waterniveau', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=2,column=0, sticky=NSEW)
            #Label(weer_frame, text='Verwacht waterniveau', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=3,column=0, sticky=NSEW)
            Label(weer_frame, text='Temperatuur', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=4,column=0, sticky=NSEW)
            Label(weer_frame, text='Huidige omstandigheden', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=5,column=0, sticky=NSEW)
            Label(weer_frame, text='Luchtvochtigheid', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=6,column=0, sticky=NSEW)
            Label(weer_frame, text='Luchtdruk', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=7,column=0, sticky=NSEW)
            Label(weer_frame, text='Windkracht', anchor = NW, bg = '#F7F7F7', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, ipady=2, row=8,column=0, sticky=NSEW)
            Label(weer_frame, text='Richting', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(ipadx=25, row=9,column=0, sticky=NSEW)

            try:
                Label(weer_frame, text=waterhoogte_hvh + str("cm NAP"), anchor = NW, bg = 'white', fg=kleur_waterhoogte_hvh, font = ('Ariel',10, 'bold')).grid(ipadx=25, row=2,column=1, sticky=NSEW)
                Label(weer_frame, text=waterhoogte_r + str("cm NAP"), anchor = NW, bg = 'white', fg=kleur_waterhoogte_r, font = ('Ariel',10, 'bold')).grid(ipadx=25, row=2,column=2, sticky=NSEW)
                Label(weer_frame, text=waterhoogte_d + str("cm NAP"), anchor = NW, bg = 'white', fg=kleur_waterhoogte_d, font = ('Ariel',10, 'bold')).grid(ipadx=25, row=2,column=3, sticky=NSEW)
            except:
                print("geen waterstand")

            geen_weertabel = ""
        except:
            geen_weertabel = "Kan actuele weersomstandigheden niet ophalen. Controleer de internetverbinding."

        weer_frame.after(60000, weer)

    def update_clock():
        global geen_klok
        try:
            now = time.strftime("%I:%M %p")
            date = time.strftime("%a, %m/%d/%Y")
            Label(tijd_frame, text=now, font=20, bg= 'white').grid(sticky=E, row=0, column=0)
            Label(tijd_frame, text=date, font=20, bg= 'white').grid(sticky=E, row=1, column=0)
            tijd_frame.after(1000, update_clock)

            geen_klok = ""
        except:
            geen_klok = "Kan geen klok weergeven."

    def status_waarschuwing():
        """Status van de Maeslantkering en eventuele waarschuwingen"""
        global bericht_r, bericht_d, status_kering

        try:
            Label(bericht_frame, text="Status:", anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10,'bold')).grid(row=1, column=0, sticky=NSEW)
            Label(bericht_frame, text=status_kering, anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10,'bold')).grid(row=2, column=0, sticky=NSEW)
            Label(bericht_frame, text="", anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=3, column=0, sticky=NSEW)
            Label(bericht_frame, text="", anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=4, column=0, sticky=NSEW)
            Label(bericht_frame, text="", anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=5, column=0, sticky=NSEW)
            Label(bericht_frame, text="Waarschuwingen:", anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=6, column=0, sticky=NSEW)
            Label(bericht_frame, text="", anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=7, column=0, sticky=NSEW)
            Label(bericht_frame, text=bericht_r, anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=8, column=0, sticky=NSEW)
            Label(bericht_frame, text=bericht_d, anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=9, column=0, sticky=NSEW)
            Label(bericht_frame, text=geen_webcam, anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=10, column=0, sticky=NSEW)
            Label(bericht_frame, text=geen_klok, anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=11, column=0, sticky=NSEW)
            Label(bericht_frame, text=geen_weersomstandigheden, anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=12, column=0, sticky=NSEW)
            Label(bericht_frame, text=geen_waterstand, anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=13, column=0, sticky=NSEW)
            Label(bericht_frame, text=geen_weertabel, anchor = NW, bg = 'white', fg='red', font = ('Ariel',10,'bold')).grid(row=14, column=0, sticky=NSEW)



        except:
            print("Kan waarschuwing niet weergeven.")

        bericht_frame.after(1000, status_waarschuwing)

    weer()
    status_waarschuwing()
    update_clock()
    webcam()
    lezen()
    mainloop()

Commandocentrum_scherm()