import requests

# returns the current and forecast ozone level in the air in a given certain location
class ozone:

    def current_data():
        latitude = input('Enter latitude: ')
        longitude = 0

         # try-except to handle if input is a float or not
        try: 
            float(latitude)
            longitude = input('Enter longitute: ')
            try:
                float(longitude)
                url = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid=638635f506f79928ef51d1f7dfd4a3a8&units=metric'.format(latitude,longitude)
                res = requests.get(url) 
                current_data = res.json()
                ozone.show_cdata(current_data)
            except ValueError:
                print('Invalid input. Run the program and enter a number instead')          
        except ValueError:
            print('Invalid input. Run the program and enter a number instead')
            


    def forecast_data():

        latitude = input('Enter latitude: ')
        longitude = 0

        # try-except to handle if input is a float or not
        try: 
            float(latitude)
            longitude = input('Enter longitute: ')
            try:
                float(longitude)
                url = 'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={}&lon={}&appid=638635f506f79928ef51d1f7dfd4a3a8&units=metric'.format(latitude,longitude)
                res = requests.get(url) 
                forecast_data = res.json()
                ozone.show_fdata(forecast_data)
            except ValueError:
                print('Invalid input. Run the program and enter a number instead')
        except ValueError:
            print('Invalid input. Run the program and enter a number instead')


    def show_cdata(current_data):
        current_level = current_data['list'][0]['components']['o3']
        print('The current ozone level is {}'.format(current_level))


    def show_fdata(forecast_data):
        forecast_level = forecast_data['list'][0]['components']['o3']
        print('The forecast ozone level is {}'.format(forecast_level))

    #starting point of the program
    #asks for the users input
    def start():

        print('Enter "current" to get the current ozone level or "forecast" to get data the forecast ozone level: ')
        answer = input('Write your answer here: ')
   
        if answer == 'Current' or answer == 'current' or answer == 'Current ' or answer == 'current ':
            ozone.current_data()

        elif answer == 'Forecast' or answer == 'forecast' or answer == 'Forecast ' or answer == 'forecast ':
            ozone.forecast_data()

        else:
            print('Sorry, invalid input. Run the program and try again :)')


ozone.start()

 
           