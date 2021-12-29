"""
File Name   : paho_mqtt_subscribe_test.py

Author      : Kevin Tom
              Teaching Assistant - Fall 2021
              Embedded Interface Design - ECEN 5783
              University of Colorado Boulder

Email       : keto9919@colorado.edu

Paltform    : Raspberry Pi 3 Model B+,  16-Bit Quad Core
              ARMv8 CPU - With WLAN and Bluetooth 4.2 & BLE

IDE Used    : Thonny Python IDE

Date        : 23 December 2021

Version     : 1.0
            
Description : This python program subcribe to a topic in the specified broker
              and prints the value received from the broker. The program also
              prints connection code which will help determine how the client
              gets connected. The follwing code will be returned,

                    0x00  -  Connection Accepted
                    0x01  -  Connection Refused, unacceptable protocol version
                    0x02  -  Connection Refused, identifier rejected
                    0x03  -  Connection Refused, Server unavailable
                    0x04  -  Connection Refused, bad user name or password
                    0x05  -  Connection Refused, not authorized
                    6-255 - Reserved for future use
                    
              
Reference   : MQTT Setup Guide slides by Prof. Benjamin Spriggs
              Paho MQTT Documentation : https://pypi.org/project/paho-mqtt/
              MQTT Connection :
              https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html#_Toc398718035

"""

#Importing the MQTT client library
import paho.mqtt.client as mqtt

#Imporiting time library
import time



"""
Name        : on_connect(rc)

Description : This function prints the connection code with which the
              subscriber got connected to broker. This function also 
              subscribes to the topic 'apt_boulder/temp1'. Connection
              codes are mentioned in the file description.
              
Paramters   : rc - Connection code returned after connection

Returns     : None

"""
def on_connect(rc):
    print("Connected with connection code:"+str(rc))
    client.subscribe("apt_boulder/temp1")




"""
Name        : on_message(message)

Description : This function prints the message received from the
              broker as soon as it is recieved. The messages are
              recieved from 'apt_boulder/temp1' topic.
              
Paramters   : Message - Message from topic subcribed.

Returns     : None

"""
def on_message(message):
    print("Message: " ,str(message.payload.decode("utf-8")))



#Test borker to which this program will be connecting
mqttBroker1 ="mqtt.eclipseprojects.io"

#Giving the program a client ID, this ID will be used to connect to the broker
client = mqtt.Client("keto_client")


client.on_connect = on_connect
client.on_message = on_message

#connecting to MQTT broker with specified client ID
client.connect(mqttBroker1)

#infinite loop
client.loop_forever()