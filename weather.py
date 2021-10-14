import hour_program
import nearby_citites
import ozone_level


#runs the three program after each other
def main():
    nearby_citites.nearby.start()
    hour_program.hour.start()
    ozone_level.ozone.start()
    
main()
