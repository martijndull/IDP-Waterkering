from tkinter import *
import pywapi

def weersvoorspelling_scherm():

    def weersomstandigheden_pred():
        """Haalt huidige weersomstandigheden van weather.com."""
        global weather_com_pred_hvh, weather_com_pred_r, weather_com_pred_d, dag1, dag2, dag3, dag4
        try:
            weather_com_pred_hvh = pywapi.get_weather_from_weather_com( 'NLXX0025', units = 'metric' )
            weather_com_pred_r = pywapi.get_weather_from_weather_com( 'NLXX0015', units = 'metric' )
            weather_com_pred_d = pywapi.get_weather_from_weather_com( 'NLXX0006', units = 'metric' )

            dag1 = weather_com_pred_hvh['forecasts'][1]['date']
            dag2 = weather_com_pred_hvh['forecasts'][2]['date']
            dag3 = weather_com_pred_hvh['forecasts'][3]['date']
            dag4 = weather_com_pred_hvh['forecasts'][4]['date']

        except:
            print("Kan weersvoorspelling niet ophalen.")

    weersomstandigheden_pred()

    root_wvs = Tk()
    root_wvs.title("Weersvoorspelling")
    #root_wvs.wm_state('zoomed')
    root_wvs.attributes("-fullscreen", True)
    root_wvs.configure(background='#F0F2F2')

    bottomframe_wvs = Frame(root_wvs, bg='#6399E6', width=1700, height=70)
    bottomframe_wvs.grid()
    bottomframe_wvs.pack_propagate(0)
    bottomframe_wvs.place(rely=0.92)

    weersvoorspelling_tekst = Frame(root_wvs, bg='#F0F2F2')
    weersvoorspelling_tekst.grid()
    weersvoorspelling_tekst.place(relx=0.05, rely=0.05)

    Label(weersvoorspelling_tekst, text='Weersvoorspelling', anchor = NW, bg='#F0F2F2', fg='#003399', font = ('Ariel',18, 'bold')).grid(row=1,column=0, ipadx=5, sticky=NSEW,)

    weersvoorspelling_frame = LabelFrame(root_wvs, width=650, height=220, text=dag1, fg='#003399', font = (13), bg='white')
    weersvoorspelling_frame.grid()
    weersvoorspelling_frame.grid_propagate(False)
    weersvoorspelling_frame.place(relx=0.05, rely=0.15)

    weersvoorspelling_frame2 = LabelFrame(root_wvs, width=650, height=220, text=dag2, fg='#003399', font = (13), bg='white')
    weersvoorspelling_frame2.grid()
    weersvoorspelling_frame2.grid_propagate(False)
    weersvoorspelling_frame2.place(relx=0.53, rely=0.15)

    weersvoorspelling_frame3 = LabelFrame(root_wvs, width=650, height=220, text=dag3, fg='#003399', font = (13), bg='white')
    weersvoorspelling_frame3.grid()
    weersvoorspelling_frame3.grid_propagate(False)
    weersvoorspelling_frame3.place(relx=0.05, rely=0.50)

    weersvoorspelling_frame4 = LabelFrame(root_wvs, width=650, height=220, text=dag4, fg='#003399', font = (13), bg='white')
    weersvoorspelling_frame4.grid()
    weersvoorspelling_frame4.grid_propagate(False)
    weersvoorspelling_frame4.place(relx=0.53, rely=0.50)

    def weersvoorspelling():
        global dag1, dag2, dag3, dag4

        def sluiten():
            root_wvs.destroy()

        scherm_sluiten_knop = Button(root_wvs, text='Terug', bg='#003399', fg='white',  command=sluiten)
        scherm_sluiten_knop.pack()
        scherm_sluiten_knop.place(width=150, height=50, relx=0.85, rely=0.93)

        try:
        #dag1
            Label(weersvoorspelling_frame, text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame, text='Min / Max temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text='Regenkans', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=0,ipadx=5, sticky=NSEW)

            #Hoek van Holland
            Label(weersvoorspelling_frame, text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][1]['low'] + "°C / " + weather_com_pred_hvh['forecasts'][1]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][1]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][1]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][1]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][1]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_hvh['forecasts'][1]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=1,ipadx=5, sticky=NSEW)

            #Rotterdam
            Label(weersvoorspelling_frame, text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][1]['low'] + "°C / " + weather_com_pred_r['forecasts'][1]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][1]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][1]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][1]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][1]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_r['forecasts'][1]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=2,ipadx=5, sticky=NSEW)

            #Dordrecht
            Label(weersvoorspelling_frame, text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][1]['low'] + "°C / " + weather_com_pred_d['forecasts'][1]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][1]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][1]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][1]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][1]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame, text=weather_com_pred_d['forecasts'][1]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=3,ipadx=5, sticky=NSEW)




        #dag2
            Label(weersvoorspelling_frame2, text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame2, text='Min / Max temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text='Regenkans', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=0,ipadx=5, sticky=NSEW)

            #Hoek van Holland
            Label(weersvoorspelling_frame2, text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame2, text=weather_com_pred_hvh['forecasts'][2]['low'] + "°C / " + weather_com_pred_hvh['forecasts'][2]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_hvh['forecasts'][2]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_hvh['forecasts'][2]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_hvh['forecasts'][2]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_hvh['forecasts'][2]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_hvh['forecasts'][2]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=1,ipadx=5, sticky=NSEW)

            #Rotterdam
            Label(weersvoorspelling_frame2, text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame2, text=weather_com_pred_r['forecasts'][2]['low'] + "°C / " + weather_com_pred_r['forecasts'][2]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_r['forecasts'][2]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_r['forecasts'][2]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_r['forecasts'][2]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_r['forecasts'][2]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_r['forecasts'][2]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=2,ipadx=5, sticky=NSEW)

            #Dordrecht
            Label(weersvoorspelling_frame2, text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame2, text=weather_com_pred_d['forecasts'][2]['low'] + "°C / " + weather_com_pred_d['forecasts'][2]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_d['forecasts'][2]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_d['forecasts'][2]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_d['forecasts'][2]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_d['forecasts'][2]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame2, text=weather_com_pred_d['forecasts'][2]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=3,ipadx=5, sticky=NSEW)


        #dag3
            Label(weersvoorspelling_frame3, text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame3, text='Min / Max temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text='Regenkans', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=0,ipadx=5, sticky=NSEW)

            #Hoek van Holland
            Label(weersvoorspelling_frame3, text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame3, text=weather_com_pred_hvh['forecasts'][3]['low'] + "°C / " + weather_com_pred_hvh['forecasts'][3]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_hvh['forecasts'][3]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_hvh['forecasts'][3]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_hvh['forecasts'][3]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_hvh['forecasts'][3]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_hvh['forecasts'][3]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=1,ipadx=5, sticky=NSEW)

            #Rotterdam
            Label(weersvoorspelling_frame3, text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame3, text=weather_com_pred_r['forecasts'][3]['low'] + "°C / " + weather_com_pred_r['forecasts'][3]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_r['forecasts'][3]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_r['forecasts'][3]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_r['forecasts'][3]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_r['forecasts'][3]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_r['forecasts'][3]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=2,ipadx=5, sticky=NSEW)

            #Dordrecht
            Label(weersvoorspelling_frame3, text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame3, text=weather_com_pred_d['forecasts'][3]['low'] + "°C / " + weather_com_pred_d['forecasts'][3]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_d['forecasts'][3]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_d['forecasts'][3]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_d['forecasts'][3]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_d['forecasts'][3]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame3, text=weather_com_pred_d['forecasts'][3]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=3,ipadx=5, sticky=NSEW)


        #dag4
            Label(weersvoorspelling_frame4, text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame4, text='Min / Max temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text='Regenkans', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=0,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=0,ipadx=5, sticky=NSEW)

            #Hoek van Holland
            Label(weersvoorspelling_frame4, text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame4, text=weather_com_pred_hvh['forecasts'][4]['low'] + "°C / " + weather_com_pred_hvh['forecasts'][4]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_hvh['forecasts'][4]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_hvh['forecasts'][4]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_hvh['forecasts'][4]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_hvh['forecasts'][4]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=1,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_hvh['forecasts'][4]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=1,ipadx=5, sticky=NSEW)

            #Rotterdam
            Label(weersvoorspelling_frame4, text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame4, text=weather_com_pred_r['forecasts'][4]['low'] + "°C / " + weather_com_pred_r['forecasts'][4]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_r['forecasts'][4]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_r['forecasts'][4]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_r['forecasts'][4]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_r['forecasts'][4]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=2,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_r['forecasts'][4]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=2,ipadx=5, sticky=NSEW)

            #Dordrecht
            Label(weersvoorspelling_frame4, text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3,ipadx=5, sticky=NSEW,)
            Label(weersvoorspelling_frame4, text=weather_com_pred_d['forecasts'][4]['low'] + "°C / " + weather_com_pred_d['forecasts'][4]['high'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_d['forecasts'][4]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_d['forecasts'][4]['day']['chance_precip'] + "%", anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_d['forecasts'][4]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_d['forecasts'][4]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=6,column=3,ipadx=5, sticky=NSEW)
            Label(weersvoorspelling_frame4, text=weather_com_pred_d['forecasts'][4]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=7,column=3,ipadx=5, sticky=NSEW)

        except:
            print("Kan tabel niet aanmaken")






    weersvoorspelling()

    mainloop()