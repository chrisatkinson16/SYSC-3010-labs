from sense_hat import SenseHat
import time 
s = SenseHat()
s.low_light = True

s.show_letter("C")

count = 1

while True:
    events = s.stick.get_events()
    for event in events:
        if event.action == "pressed":
          if event.direction == "left":
            s.show_letter("C")
            time.sleep(5)
            s.show_letter("A")
          if event.direction == "right":
            s.clear()