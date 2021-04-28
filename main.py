import pyautogui as pa
from time import sleep

positions = []
count = 0

print('Starting after 3 sec...')
print('3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)
# Record mouse movements
# Take mouse position
while count < 50:
    sleep(0.08)
    print(count)
    count += 1
    position = pa.position()
    print('Position is:',position)
    # Save mouse position
    positions.append(position)

print('Waiting 3 sec...')
print('3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)




  
# Getting length of list
i = 0
# Iterating using while loop
while i < count:
    # Play the recorded mouse movements
    print('moving mouse...')
    pa.moveTo(positions[i])
    i += 1
    # Move mouse to saved position 

