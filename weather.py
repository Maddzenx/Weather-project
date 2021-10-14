import hour_program
import nearby_citites
import ozone_level

#runs the three program after each other
def main():
    hour_program.hour.start()
    nearby_citites.nearby.start()
    ozone_level.ozone.start()
    
main()
