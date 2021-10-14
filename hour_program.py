import requests 

# returns the weather forecast in the upcoming 12 hour with 3-hour intervals
class hour:

    # gets data by cityname
    def by_cityname():

        city = input('Enter a city: ')
        url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid=638635f506f79928ef51d1f7dfd4a3a8&units=metric'.format(city)
        res = requests.get(url) # imports the data
        data = res.json() # to json format
        hour.show_data(data)

    # gets data by latitude and longitude values
    def by_coordinates():

        latitude = input('Enter latitude: ')
        longitude = 0


        # try-except to handle if input is a float or not
        try: 
            float(latitude)
            longitude = input('Enter longitute: ')
            try:
                float(longitude)
                url = 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid=638635f506f79928ef51d1f7dfd4a3a8&units=metric'.format(latitude,longitude)
                res = requests.get(url) 
                data = res.json() 
                hour.show_data(data)
            except ValueError:
                print('Invalid input. Run the program and enter a number instead')
                
                
        except ValueError:
            print('Invalid input. Run the program and enter a number instead')
            

    # prints the data
    def show_data(data):

        date0 = data['list'][0]['dt_txt']
        date1 = data['list'][1]['dt_txt']
        date2 = data['list'][2]['dt_txt']
        date3 = data['list'][3]['dt_txt']
        date4 = data['list'][4]['dt_txt']

        temp0 = data['list'][0]['main']['temp']
        temp1 = data['list'][1]['main']['temp']
        temp2 = data['list'][2]['main']['temp']
        temp3 = data['list'][3]['main']['temp']
        temp4 = data['list'][4]['main']['temp']

        city = data['city']['name']

        print('\n{} 12-hour weather forecast:\n'.format(city)) 
        print('Current ({}) '.format(date0)+ 'the temperature will be {} degree celcius'.format(temp0))
        print('In 3 hours ({}) '.format(date1) + 'the temperature will be {} degree celcius'.format(temp1)) 
        print('In 6 hours ({}) '.format(date2) + 'the temperature will be {} degree celcius'.format(temp2))
        print('In 9 hours ({}) '.format(date3) + 'the temperature will be {} degree celcius'.format(temp3))
        print('In 12 hours ({}) '.format(date4) + 'the temperature will be {} degree celcius\n'.format(temp4))

    #starting point of the program
    #asks for the users input
    def start():

        print('Hi! How do you want to get data?')
        print('Enter "name" to get data by cityname or "coord" to get data by coordinates')
        answer = input('Write your answer here: ')

   
        if answer == 'name':
            hour.by_cityname()

        elif answer == 'coord':
            hour.by_coordinates()

        else:
            print('Sorry, invalid input. Run the program and try again :)')
           

hour.start()
