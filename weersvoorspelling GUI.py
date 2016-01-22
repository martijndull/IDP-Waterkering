from tkinter import *
import pywapi

weather_com_pred_hvh = pywapi.get_weather_from_weather_com( 'NLXX0025', units = 'metric' )
weather_com_pred_r = pywapi.get_weather_from_weather_com( 'NLXX0015', units = 'metric' )
weather_com_pred_d = pywapi.get_weather_from_weather_com( 'NLXX0006', units = 'metric' )


class WindowClass1():
    def __init__(self):
        root = Tk()
        root.title("Weersvoorspelling")
        root.wm_state('zoomed')

        def weersvoorspelling():

            Label(text='Datum', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=4, sticky=NSEW,)
            Label(text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
            Label(text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW)
            Label(text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW)
            Label(text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW)
            Label(text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)
            Label(text='Minimum temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0, sticky=NSEW)

            #datum
            Label(text=weather_com_pred_hvh['forecasts'][1]['date'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=5, sticky=NSEW)

            #Hoek van Holland
            Label(text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW,)
            Label(text=weather_com_pred_hvh['forecasts'][1]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][1]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][1]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][1]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][1]['low'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1, sticky=NSEW)

            #Rotterdam
            Label(text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=2, sticky=NSEW,)
            Label(text=weather_com_pred_r['forecasts'][1]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][1]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][1]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][1]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][1]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2, sticky=NSEW)

            #Dordrecht
            Label(text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=3, sticky=NSEW,)
            Label(text=weather_com_pred_d['forecasts'][1]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][1]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][1]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][1]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][1]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3, sticky=NSEW)

        weersvoorspelling()
        mainloop()

WindowClass1()


class WindowClass2():
    def __init__(self):
        root = Tk()
        root.title("Weersvoorspelling")
        root.wm_state('zoomed')

        def weersvoorspelling():

            Label(text='Datum', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=4, sticky=NSEW,)
            Label(text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
            Label(text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW)
            Label(text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW)
            Label(text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW)
            Label(text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)
            Label(text='Minimum temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0, sticky=NSEW)

            #datum
            Label(text=weather_com_pred_hvh['forecasts'][2]['date'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=5, sticky=NSEW)

            #Hoek van Holland
            Label(text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW,)
            Label(text=weather_com_pred_hvh['forecasts'][2]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][2]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][2]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][2]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][2]['low'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1, sticky=NSEW)

            #Rotterdam
            Label(text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=2, sticky=NSEW,)
            Label(text=weather_com_pred_r['forecasts'][2]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][2]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][2]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][2]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][2]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2, sticky=NSEW)

            #Dordrecht
            Label(text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=3, sticky=NSEW,)
            Label(text=weather_com_pred_d['forecasts'][2]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][2]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][2]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][2]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][2]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3, sticky=NSEW)

        weersvoorspelling()
        mainloop()

WindowClass2()


class WindowClass3():
    def __init__(self):
        root = Tk()
        root.title("Weersvoorspelling")
        root.wm_state('zoomed')

        def weersvoorspelling():

            Label(text='Datum', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=4, sticky=NSEW,)
            Label(text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
            Label(text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW)
            Label(text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW)
            Label(text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW)
            Label(text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)
            Label(text='Minimum temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0, sticky=NSEW)

            #datum
            Label(text=weather_com_pred_hvh['forecasts'][3]['date'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=5, sticky=NSEW)

            #Hoek van Holland
            Label(text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW,)
            Label(text=weather_com_pred_hvh['forecasts'][3]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][3]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][3]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][3]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][3]['low'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1, sticky=NSEW)

            #Rotterdam
            Label(text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=2, sticky=NSEW,)
            Label(text=weather_com_pred_r['forecasts'][3]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][3]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][3]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][3]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][3]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2, sticky=NSEW)

            #Dordrecht
            Label(text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=3, sticky=NSEW,)
            Label(text=weather_com_pred_d['forecasts'][3]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][3]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][3]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][3]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][3]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3, sticky=NSEW)

        weersvoorspelling()
        mainloop()

WindowClass3()


class WindowClass4():
    def __init__(self):
        root = Tk()
        root.title("Weersvoorspelling")
        root.wm_state('zoomed')

        def weersvoorspelling():

            Label(text='Datum', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=4, sticky=NSEW,)
            Label(text='Locatie', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=0, sticky=NSEW,)
            Label(text='Verwachte omstandigheden', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=0, sticky=NSEW)
            Label(text='Luchtvochtigheid', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=0, sticky=NSEW)
            Label(text='Windkracht', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=0, sticky=NSEW)
            Label(text='Richting', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=0, sticky=NSEW)
            Label(text='Minimum temperatuur', anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=0, sticky=NSEW)

            #datum
            Label(text=weather_com_pred_hvh['forecasts'][4]['date'], anchor = NW, bg = 'white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=5, sticky=NSEW)

            #Hoek van Holland
            Label(text="Hoek van Holland", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=1, sticky=NSEW,)
            Label(text=weather_com_pred_hvh['forecasts'][4]['day']['text'], anchor = NW, bg ='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][4]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][4]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][4]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=1, sticky=NSEW)
            Label(text=weather_com_pred_hvh['forecasts'][4]['low'] + "°C",  anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=1, sticky=NSEW)

            #Rotterdam
            Label(text="Rotterdam", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=2, sticky=NSEW,)
            Label(text=weather_com_pred_r['forecasts'][4]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][4]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][4]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][4]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=2, sticky=NSEW)
            Label(text=weather_com_pred_r['forecasts'][4]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=2, sticky=NSEW)

            #Dordrecht
            Label(text="Dordrecht", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=0,column=3, sticky=NSEW,)
            Label(text=weather_com_pred_d['forecasts'][4]['day']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=1,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][4]['day']['humidity'] + "%", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=2,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][4]['day']['wind']['speed'] + str("km/h"), anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=3,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][4]['day']['wind']['text'], anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=4,column=3, sticky=NSEW)
            Label(text=weather_com_pred_d['forecasts'][4]['low'] + "°C", anchor = NW, bg='white', fg='#003399', font = ('Ariel',10, 'bold')).grid(row=5,column=3, sticky=NSEW)

        weersvoorspelling()
        mainloop()

WindowClass4()
