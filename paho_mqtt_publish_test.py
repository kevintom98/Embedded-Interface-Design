"""
File Name   : paho_mqtt_publish_test.py

Author      : Kevin Tom
              Teaching Assistant - Fall 2021
              Embedded Interface Design - ECEN 5783
              University of Colorado Boulder

Email       : keto9919@colorado.edu

Paltform    : Raspberry Pi 3 Model B+,  16-Bit Quad Core
              ARMv8 CPU - With WLAN and Bluetooth 4.2 & BLE

IDE Used    : Thonny Python IDE

Date        : 23 December 2021

Version     : 1.2
            
Description : This python program is a skeleton program which publishes a random number
              to a topic called 'apt_boulder/temp1' in sample MQTT broker 'mqtt.eclipse
              projects.io'. After publishing the published value is printed, then the p
              rogram goes to sleep for 2 secnds (This might vary a little). The program
              publishes data to topic every 2 seconds.
              
Reference   : MQTT Setup Guide slides by Prof. Benjamin Spriggs
              Paho MQTT Documentation : https://pypi.org/project/paho-mqtt/

"""

#Importing the MQTT client library
import paho.mqtt.client as mqtt

#Importing random library 
from random import uniform

#Imporiting time library
import time

#Test borker to which this program will be connecting
mqttBroker1 ="mqtt.eclipseprojects.io" 

#Giving the program a client ID, this ID will be used to connect to the broker
client = mqtt.Client("Temperature_Inside_1")

#connecting to MQTT broker with specified client ID
client.connect(mqttBroker1) 

#infinite loop
while True:
    #Generate a random number between 20.0 and 25.0
    randNumber = uniform(20.0, 25.0)
    
    #publishing the generated random number to topic
    client.publish("apt_boulder/temp1", randNumber)
    
    #printing generated random number
    print("Just published " + str(randNumber) + " to topic apt_boulder/temp1")
    
    #Program going to sleep for 2 seconds
    time.sleep(2)