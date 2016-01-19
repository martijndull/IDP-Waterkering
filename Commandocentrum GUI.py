#Deze code wordt gebruikt voor de grafische user interface voor de simulatie van het eerste commandocentrum
#toevoegen: weersomstandigheden via API, status / waarschuwing open/sluiten waterkering

#test


from tkinter import *
import sys
import pywapi

weather_com_result = pywapi.get_weather_from_weather_com('NLXX0025')

print (weather_com_result['current_conditions']['temperature'])

def Commandocentrum_scherm():
    root = Tk()
    root.title("Commandocentrum 1")
    root.wm_state('zoomed')

    def weer():

        Label(text='Locatie', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
        Label(text='Temperatuur', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW)
        Label(text='Windkracht', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW)
        Label(text='Richting', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW)
        Label(text='Luchtvochtigheid', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)

        Label(text=weather_com_result['current_conditions']['station'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW,)
        Label(text=weather_com_result['current_conditions']['temperature'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
        Label(text=weather_com_result['current_conditions']['wind']['speed'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
        Label(text=weather_com_result['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
        Label(text=weather_com_result['current_conditions']['humidity'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)

    weer()
    mainloop()

Commandocentrum_scherm()

