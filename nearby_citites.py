import requests

class nearby:

    # gets the data of the nearby citites within a rectangle
    def by_rectangle():
        
        coordBounds = input('Enter the longitube and latutide bounds in the format [lon-left,lat-bottom,lon-right,lat-top,zoom] where zoom is between 0-16 for instance 12,32,15,37,10. No deciamls.": ')
       
        url = 'http://api.openweathermap.org/data/2.5/box/city?bbox={}&appid=638635f506f79928ef51d1f7dfd4a3a8&units=metric'.format(coordBounds)
        res = requests.get(url) 
        data = res.json()
        nearby.show_data(data)


    # gets the data of the nearby citites within a circle
    def by_circle():

        latitude = input('Enter latitude: ')
        longitude = 0


        # try-except to handle if input is a float or not
        try: 
            float(latitude)
            longitude = input('Enter longitute: ')
            try:
                float(longitude)
                url = 'http://api.openweathermap.org/data/2.5/find?lat={}&lon={}&cnt=3&appid=638635f506f79928ef51d1f7dfd4a3a8&units=metric'.format(latitude, longitude)
                res = requests.get(url) 
                data = res.json()
                nearby.show_data(data)
            except ValueError:
                print('Invalid input. Run the program and enter a number instead')
                
        except ValueError:
            print('Invalid input. Run the program and enter a number instead')


    # prints the data
    def show_data(data):

        name0 = data['list'][0]['name']
        name1 = data['list'][1]['name']
        name2 = data['list'][2]['name']

        print('\nSome citites within the area is:\n1.{} '.format(name0) + '\n2.{}'.format(name1) + '\n3.{}'.format(name2)) 


    #starting point of the program
    #asks for the users input
    def start():
        answer = input('Enter how if you want nearby citites within a "rectangle" or a "circle": ')

        if answer == 'rectangle' or answer == 'rectangle ' or answer == 'Rectangle'or answer == 'Rectangle ':
            nearby.by_rectangle()

        elif answer =='circle' or answer =='circle ' or answer =='Circle' or answer =='Circle ':
            nearby.by_circle()

        else: 
            print('Sorry, I did not get that. Run the program and try again :)')
            


nearby.start()
