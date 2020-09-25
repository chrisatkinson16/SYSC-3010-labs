from sense_emu import SenseHat
import time 
s = SenseHat()
s.low_light = True

red = (255, 0, 0)
nothing = (0, 0, 0)

def c():
    R = red
    N = nothing
    c = [
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, R, R, N, N, N,
    N, N, R, N, N, N, N, N,
    N, N, R, N, N, N, N, N,
    N, N, N, R, R, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    ]
    return c

def a():
    R = red
    N = nothing
    a = [
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, R, N, N, N, N,
    N, N, R, N, R, N, N, N,
    N, N, R, R, R, N, N, N,
    N, N, R, N, R, N, N, N,
    N, N, N, N, N, N, N, N,
    N, N, N, N, N, N, N, N,
    ]
    return a
    
def do_thing(event):
    letters = [c, a]
    count = 0
    if event.action == 'pressed':
        while True:
            s.set_pixels(letters[count%len(letters)]())
            time.sleep(0.75)
            count= count + 1
            
s.stick.direction_any = do_thing
