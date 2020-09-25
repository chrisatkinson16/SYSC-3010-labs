#temperature sensor using the sense hat

import random
from sense_emu import SenseHat

s = SenseHat()

print('press up for the temperature')

def temp(event):
    if event.action == 'pressed':
        print ('the current temp is', random.randint(-20, 30))
    
s.stick.direction_up = temp

    
