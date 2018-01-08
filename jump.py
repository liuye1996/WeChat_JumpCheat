import os
import PIL
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import  time

need_update = True

def get_screen_image():
    os.system('adb shell screencap -p /storage/emulated/0/.1py/screen.png')
    os.system('adb pull /storage/emulated/0/.1py/screen.png')
    return numpy.array(PIL.Image.open('screen.png'))

def jump_to_next(point1,point2):
    x1,y1 = point1;x2,y2 = point2
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance*1.95)))

def on_calck(event,coor=[]):
    global  need_update
    coor.append((event.xdata,event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(),coor.pop())
    need_update = True

def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,

figure = plt.figure()
axes_image = plt.imshow(get_screen_image(),animated=True)
figure.canvas.mpl_connect('button_press_event',on_calck)
ani = FuncAnimation(figure,update_screen,interval=50,blit=True)
plt.show()