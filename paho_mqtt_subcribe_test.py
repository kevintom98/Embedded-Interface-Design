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
              gets coinnected. The follwing code
              
Reference   : MQTT Setup Guide slides by Prof. Benjamin Spriggs
              Paho MQTT Documentation : https://pypi.org/project/paho-mqtt/

"""
import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,flags,rc):
    print("Connected with connection code:"+str(rc))
    client.subscribe("apt_boulder/temp1")

def on_message(client, userdata, message):
    print("Message: " ,str(message.payload.decode("utf-8")))

mqttBroker1 ="mqtt.eclipseprojects.io"

client = mqtt.Client("keto_client")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttBroker1)
client.loop_forever()

#client.connect(mqttBroker) 

#client.loop_start()

#client.subscribe("TEMPERATURE_CUB")
#client.on_message=on_message 

#time.sleep(30)
#client.loop_stop()