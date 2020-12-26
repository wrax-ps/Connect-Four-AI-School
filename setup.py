from os import system
import time

system('python setup.py')

print('This program is going to install the packages that the game is going to make the game')
time.sleep(3)

system('pip install numpy==1.19.4')
system('pip install pygame')

print('Check for errors in the packages. If there is no errors then you can shut this window')
time.sleep(120)