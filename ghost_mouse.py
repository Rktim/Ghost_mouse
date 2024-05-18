#HOW TO CREATE A GHOST MOUSE


import pyautogui as pyg
import random
import time

while True:
    x=random.randint(550,780)
    y=random.randint(250,580)

    pyg.moveTo(x,y,0.6)
    time.sleep(1)
    

