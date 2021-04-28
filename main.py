import pyautogui as pa
import time

positions = []
# Record mouse movements
# Take mouse position
print('take position')
position = pa.position()
print('Position is:',position)
# Save mouse position
positions.append(position)
print('sleep 5 sec...')
time.sleep(5)

# Play the recorded mouse movements
print('moving mouse')
pa.moveTo(position)
# Move mouse to saved position 
