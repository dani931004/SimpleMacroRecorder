import pyautogui as pa
from time import sleep
from pynput import keyboard



# Record number of positions where mouse is clicked or scrolled
def record():
    print('Starting after 3 sec...')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Recording...')
    from mouse_recorder import play_recorder
    # Record mouse clicks and scrolls
    play = play_recorder()
    print('Record stopped...')
    print('Recording done...')
    return 'Finished!'

# Play recorded positions
def play():
    speed = input('Please enter the speed between clicks in sec...')
    print('Waiting 3 sec...')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Playing...')
    # open the mouse log file and take all x,y and buttons from it
    with open('mouse_log.txt', 'r') as f:
        a = f.readlines()
        for line in a:
            if 'Button' in line:
                l = line.split(',')
                dx = l[0]
                dy = l[1]
                b = l[2].replace('Button.','').replace('\n','')
                buttons = b
                pa.click(x=int(dx), y=int(dy), button=buttons)
                sleep(float(speed))
                print('Click')
            elif 'scrollh' in line:
                ll = line.split(',')
                s = ll[3].replace('\n','')
                sx = ll[0]
                sy = ll[1]
                pa.scroll(s,x=int(sx),y=int(sy))
                sleep(float(speed))
                print('Scroll')
    return 'Complete!'


record()
# play()