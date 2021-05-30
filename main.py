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
    from recorder import play_recorder
    # Record mouse clicks and scrolls
    play = play_recorder()
    print('Record stopped...')
    print('Recording done...')
    return 'Finished!'

# Play recorded positions
def play():
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
        case = '"'
        for line in a:
            if 'Button' in line:
                l = line.split(',')
                speed = l[3]
                sleep(float(speed))
                dx = l[0]
                dy = l[1]
                b = l[2].replace('Button.','').replace('\n','')
                buttons = b
                pa.click(x=int(dx), y=int(dy), button=buttons)
                print('Click')
            elif 'scrollh' in line:
                ll = line.split(',')
                speed = ll[4]
                sleep(float(speed))
                s = ll[3].replace('\n','')
                sx = ll[0]
                sy = ll[1]
                pa.scroll(s,x=int(sx),y=int(sy))
                print('Scroll')
            elif 'Press' in line:
                line = line.replace('Press:','').replace("'","").replace('\n','')
                if "shift_r" in line:
                    press = 'shiftright'
                    pa.press(press)
                    print('IF')
                    print('Press',press)
                elif '""' in line:
                    press = '"'
                    print('ELIF')
                    pa.press(press)
                    print('Press',press)
                elif 'ctrl_r' in line:
                    press = "ctrlright"
                    pa.press(press)
                    print('ELIF')
                    print('Press',press)
                elif 'alt_r' in line:
                    press = "altright"
                    pa.press(press)
                    print('ELIF')
                    print('Press',press)
                else:
                    press = line.replace('"',"").replace(' ','').replace('Key.','').replace('_','')
                    pa.press(press)
                    print('ELSE')
                    print('Press',press)
    return 'Complete!'


record()
# play()