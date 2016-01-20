#Deze code wordt gebruikt voor de grafische user interface voor de simulatie van het eerste commandocentrum
#toevoegen: weersomstandigheden via API, status / waarschuwing open/sluiten waterkering


from tkinter import *
import sys
import pywapi

weather_com_result_hvh = pywapi.get_weather_from_weather_com('NLXX0025')
weather_com_result_r = pywapi.get_weather_from_weather_com('NLXX0015')
weather_com_result_d = pywapi.get_weather_from_weather_com('NLXX0006')

def Commandocentrum_scherm():
    root = Tk()
    root.title("Commandocentrum Alpha")
    root.wm_state('zoomed')

    weersvoorspelling_knop = Button(text='Weersvoorspelling', bg='#003399', fg='white')
    weersvoorspelling_knop.pack()
    weersvoorspelling_knop.place(width=130, height=50, relx=0.15, rely=0.90)

    waterstand_knop = Button(text='Archief waterstand', bg='#003399', fg='white')
    waterstand_knop.pack()
    waterstand_knop.place(width=130, height=50, relx=0.30, rely=0.90)


    def weer():

        Label(text='Locatie', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
        Label(text='Temperatuur', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW)
        Label(text='Windkracht', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW)
        Label(text='Richting', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW)
        Label(text='Luchtvochtigheid', anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)

        #Hoek van Holland
        Label(text=weather_com_result_hvh['current_conditions']['station'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW,)
        Label(text=weather_com_result_hvh['current_conditions']['temperature'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['wind']['speed'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
        Label(text=weather_com_result_hvh['current_conditions']['humidity'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)

        #Rotterdam
        Label(text=weather_com_result_r['current_conditions']['station'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=2, sticky=NSEW,)
        Label(text=weather_com_result_r['current_conditions']['temperature'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['wind']['speed'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2, sticky=NSEW)
        Label(text=weather_com_result_r['current_conditions']['humidity'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2, sticky=NSEW)

        #Dordrecht
        Label(text=weather_com_result_d['current_conditions']['station'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=3, sticky=NSEW,)
        Label(text=weather_com_result_d['current_conditions']['temperature'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['wind']['speed'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['wind']['text'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3, sticky=NSEW)
        Label(text=weather_com_result_d['current_conditions']['humidity'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3, sticky=NSEW)


    weer()
    mainloop()

Commandocentrum_scherm()

