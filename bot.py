import pyautogui as pygu
import time
time.sleep(4)
#print(pygu.position())
x=990
y=1061
pygu.moveTo(x,y,1)
pygu.leftClick(x,y,1)hi

y1=237
pygu.dragTo(x1,y1)
pygu.leftClick(x1,y1,1)

for i in range(109):
    pygu.write("hi")
    
    pygu.press('enter')