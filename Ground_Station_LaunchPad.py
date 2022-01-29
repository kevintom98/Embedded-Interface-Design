'''
Ground station script using tkinter and matplotlib.
Author        : Kevin Tom
Date          : 1 - Jun -2019
User group    : International Cansat Competition - AAS, NASA
Developed for : Launchpad SJCE - Cansat Group
'''


import matplotlib.pyplot as plt
#import tkinter as tk
import matplotlib.animation as animation
#import time
#from tkinter import ttk
#import sys
import serial
import keyboard


print("modules start")
print(keyboard.__file__)
print(serial.__file__)
print("modules end")
try:
    ser = serial.Serial('COM11', baudrate=9600)
    ser.flushInput()

    while True:
        # check if bytes received
        numBytes = ser.inWaiting()
        if(numBytes > 0):
            serBytes = ser.readline()
            print(serBytes)

            file = open('people.csv', 'ab')
            file.write(serBytes)
            file.close()
    # close serial port
    ser.close

except:
    #print("Unexpected error:", sys.exc_info()[0])
    #print("Unexpected error:", sys.exc_info()[1])
    print("error")
#Adding Subplots
fig = plt.figure()
ax1 = fig.add_subplot(4,2,1)
ax2 = fig.add_subplot(4,2,2)
ax3 = fig.add_subplot(4,2,3)
ax4 = fig.add_subplot(4,2,4)
ax5 = fig.add_subplot(4,2,5)
ax6 = fig.add_subplot(4,2,6)
ax7 = fig.add_subplot(4,2,7)
ax8 = fig.add_subplot(4,2,8)

#Reading CSV and splitting data by newline
def animate(i):
    pullData = open("people.csv","r").read()
    dataArray = pullData.split('\n')
    aar = []
    #bar = []
    #car = []
    #dar = []
    ear = []
    far = []
    gar = []
    #har = []
    #iar = []
    #jar = []
    kar = []
    #lar = []
    mar = []
    nar = []
    oar = []
    #par = []
    xar = []
    q=0
    for eachLine in dataArray:
        if len(eachLine)>1:
            q=q+1
            a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = eachLine.split(',')
            xar.append(int(q))
            aar.append(int(d))
            ear.append(int(e))
            far.append(float(f))
            gar.append(float(g))
            kar.append(int(k))
            mar.append(float(m))
            nar.append(float(n))
            oar.append(int(o))
    ax1.clear()
    ax1.plot(xar,aar)
    ax1.set_ylabel('Altitude')

    ax2.clear()
    ax2.set_ylabel('Pressure')
    ax2.plot(xar,ear)

    ax3.clear()
    ax3.set_ylabel('Temprature')
    ax3.plot(xar,far)

    ax4.clear()
    ax4.plot(xar,gar)
    ax4.set_ylabel('Voltage')

    ax5.clear()
    ax5.plot(xar,kar)
    ax5.set_ylabel('GPS Altitude')

    ax6.clear()
    ax6.plot(xar,mar)
    ax6.set_ylabel('Pitch')

    ax7.clear()
    ax7.plot(xar,nar)
    ax7.set_ylabel('Roll')

    ax8.clear()
    ax8.plot(xar,oar)
    ax8.set_ylabel('RPM of blades')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
