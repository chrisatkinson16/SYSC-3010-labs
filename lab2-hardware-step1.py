from sense_emu import SenseHat
import time 
s = SenseHat()
s.low_light = True

s.show_letter("C")

count = 1

while True:
    events = s.stick.get_events()
    for event in events:
        if event.action == "pressed":
            count = count + 1
            if count%2 == 0:
                s.show_letter("C")
            else:
                s.show_letter("A")
                
s.stick.direction_any = do_thing
