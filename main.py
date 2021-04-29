import pyautogui as pa
from time import sleep
import mouse_recorder as mr

# Record number of positions where mouse is moved
def record():
    positions = []
    print('Starting after 3 sec...')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Recording...')
    # Record mouse movements
    mode = 'on_move'
    mr.play_listener(mode)
    print('Record stopped...')
    with open ('mouse_log.txt', 'r') as f:
        line = f.readlines()
        for line in line:
            positions.append(line)
    # Take mouse position
    # while count < recorded_positions:
    #     sleep(0.08)
    #     count += 1
    #     position = pa.position()
    #     # Save mouse position
    #     positions.append(position)
    print('Recording done...')
    return positions

# Play recorded positions
def play(count,positions):
    print('Waiting 3 sec...')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Playing...')
    # Getting length of list
    i = 0
    # Iterating using while loop
    while i < count:
        # Play the recorded mouse movements
        pa.moveTo(positions[i])
        i += 1
        # Move mouse to saved position 
    return 'Complete!'


# play(100,record(100))

def play_mouse():
    print('Playing...')
    x = []
    y = []
    # open log file and take x and y from it and append them to lists
    with open('mouse_log.txt', 'r') as f:
        print('Opening file...')
        line = f.readlines()
        for line in line:
            l = line.split('|')
            y.append(l[1].strip('\n'))
            x.append(l[0])
        print('Closing file...')
    # # play all x,y points
    move = [pa.moveTo(int(x[i]),int(y[i])) for i in range(len(x))]
    # for i in range(len(x)):
    #     pa.moveTo(int(x[i]),int(y[i]))
    return print('Playing Complete!')


# mode = 'on_move'
# mr.play_listener(mode)
play_mouse()