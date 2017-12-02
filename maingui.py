from tkinter import *
import pigpio
import DHT22
import RPi.GPIO as GPIO
import time
from time import sleep
import serial

def temp(): #code for temp/humidity
    pi=pigpio.pi()
    s=DHT22.sensor(pi,4)
    s.trigger()
    sleep(2)
    a=(s.humidity()/1.)
    b=(s.temperature()/1.)
    firstLabel=Label(leftFrame,text=a)
    firstLabel.grid(row=1,column=0,padx=10,pady=2)
    secondLabel=Label(leftFrame,text=b)
    secondLabel.grid(row=2,column=0,padx=10,pady=2)
    s.cancel()
    pi.stop()
    
def uls():  #code for distance estimation
    GPIO.setmode(GPIO.BCM)
    TRIG=23
    ECHO=24
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance=round(distance, 2)
    thirdLabel=Label(leftFrame,text=distance)
    thirdLabel.grid(row=1,column=1,padx=10,pady=2)
    GPIO.cleanup()

def radar():
    ser=serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=1)

    for i in range(6):
        arduinoData=ser.readline().decode('ascii')
        print (arduinoData)
    
    
root=Tk()
root.wm_title("ARMET")              #frame generation
root.config(background="#FFFFFF")
leftFrame=Frame(root,width=1000,height=3000,bg="#FFFFFF")
leftFrame.grid(row=0,column=0,padx=10,pady=2)

newButton=Button(leftFrame,text="T/H",command=temp)  #button generation
newButton.grid(row=0,column=0,padx=10,pady=2)

newButton1=Button(leftFrame,text="distance",command=uls)
newButton1.grid(row=0,column=1,padx=10,pady=2)

newButton2=Button(leftFrame,text="radar",command=radar)
newButton2.grid(row=3,column=0,padx=10,pady=2)

root.mainloop()

