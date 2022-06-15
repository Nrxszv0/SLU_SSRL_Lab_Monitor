# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Modified from ^^
# By: Michael Crothers

import time
from datetime import datetime
import board
import adafruit_dht
import RPi.GPIO as GPIO
import math

import I2C_LCD_driver

from message import *


# Initialize the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.

# dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()

tempCMax = 30
tempCMin = 10
humiMax = 80
humiMin = 20

tempState = 0
humiState = 0
prevTempState = tempState
prevHumiState = humiState

# messageSentFlagTemp = False
# messageSentFlagHumi = False

tempLEDPin = 20
humiLEDPin = 21
errMessageLEDPin = 16
pasMessageLEDPin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(tempLEDPin,GPIO.OUT)
GPIO.setup(humiLEDPin,GPIO.OUT)
GPIO.setup(errMessageLEDPin,GPIO.OUT)
GPIO.setup(pasMessageLEDPin,GPIO.OUT)


GPIO.output(tempLEDPin,GPIO.LOW)
GPIO.output(humiLEDPin,GPIO.LOW)
GPIO.output(errMessageLEDPin,GPIO.LOW)
GPIO.output(pasMessageLEDPin,GPIO.LOW)



def sendMessages(subject, body):
    if __name__ =='__main__':                 
        email_alert("6366759462@txt.att.net", subject, body) # https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/ for other cell companies
        email_alert("lcrothers037@rsdmo.org", subject, body) 


while True:
    try:
    # Print the values to the serial port

      #for testing conditions
    # temperature_c = float(input("Enter Celcius: "))
    # temperature_f = temperature_c * (9 / 5) + 32
    # humidity = float(input("Enter Humidity: "))

        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity    

        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

        mylcd.lcd_clear()
        strTemp = "Temp:{:.1f}F {:.1f}C".format(temperature_f,temperature_c)
        strHumi = "Humidity: {}%".format(humidity)
        mylcd.lcd_display_string(strTemp, 1)
        mylcd.lcd_display_string(strHumi, 2)



        now = datetime.now()
        strDate = now.strftime("%m/%d/%Y %H:%M:%S")
        #add while loop to check if values are real and data was read
        if temperature_c > tempCMax:
            #if temperature greater than max turn on tempLED
            tempState = 1
            GPIO.output(tempLEDPin,GPIO.HIGH)
            strWarn = "Warning {} Time: {}".format(strTemp,strDate)
            print("Warning High Temperature")
            print(strWarn)
            if tempState != prevTempState:            
                #if temperature greater than max and a message was not just sent, send a message                
                try:                
                    sendMessages("Warning High Temperature", strWarn)
                    print("High Temp Message Sent")
                    prevTempState = tempState
                    GPIO.output(pasMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pasMessageLEDPin,GPIO.LOW)

                except:    
                    print("Message Error")
                    GPIO.output(errMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(errMessageLEDPin,GPIO.LOW)


        if temperature_c < tempCMin:
            #if temp less than min turn on tempLED
            tempState = -1
            GPIO.output(tempLEDPin,GPIO.HIGH)
            strWarn = "Warning {} Time: {}".format(strTemp,strDate)
            print("Warning Low Temperature")
            print(strWarn)
            if tempState != prevTempState:
                #if temp less than min and message was not just sent, send a message
                try:
                    sendMessages("Warning Low Temperature", strWarn)                       
                    print("Low Temp Message Sent")
                    prevTempState = tempState 
                    GPIO.output(pasMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pasMessageLEDPin,GPIO.LOW)                            
                except:
                    print("Message Error")
                    GPIO.output(errMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(errMessageLEDPin,GPIO.LOW)


        if humidity > humiMax:
            #if humidity greater than max turn on humiLED
            humiState = 1
            GPIO.output(humiLEDPin,GPIO.HIGH)
            strWarn = "Warning {} Time: {}".format(strHumi,strDate)
            print("Warning High Humidity")
            print(strWarn)
            if humiState != prevHumiState:
                #if humidity greater than max and a message was not just sent, send a message
                try:
                    sendMessages("Warning High Humidity", strWarn)  
                    print("High Humidity Message Sent")
                    prevHumiState = humiState
                    GPIO.output(pasMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pasMessageLEDPin,GPIO.LOW)    
                except:
                    print("Message Error")
                    GPIO.output(errMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(errMessageLEDPin,GPIO.LOW)
        if humidity < humiMin:
            #if humidity less than min turn on humiLED
            humiState = -1
            GPIO.output(humiLEDPin,GPIO.HIGH)
            strWarn = "Warning {} Time: {}".format(strHumi,strDate)
            print("Warning Low Humidity")
            print(strWarn)
            if humiState != prevHumiState:
                try:
                    sendMessages("Warning Low Humidity", strWarn)
                    print("Low Humidity Message Sent")
                    prevHumiState = humiState
                    GPIO.output(pasMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pasMessageLEDPin,GPIO.LOW) 
                except:
                    print("Message Error")
                    GPIO.output(errMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(errMessageLEDPin,GPIO.LOW)
                    
        if temperature_c <= tempCMax and temperature_c >= tempCMin:
            #if temp stabilizes send a text and turn off tempLED
            humiState = 0
            GPIO.output(tempLEDPin,GPIO.LOW)
            print("Temperature Stabilized")
            strTempStab = "Temperature Stabilized {} Time: {}".format(strTemp,strDate)
            if tempState != prevTempState:
                try:
                    sendMessages("Temperature Stabilized", strTempStab)
                    print("Temp Stablized Message Sent")
                    prevTempState = tempState
                    GPIO.output(pasMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pasMessageLEDPin,GPIO.LOW) 
                except:
                    print("Message Error")
                    GPIO.output(errMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(errMessageLEDPin,GPIO.LOW)                       
                           
        if humidity <= humiMax and humidity >= humiMin:
            #if humidity stabilizes send a text and turn off humiLED
            GPIO.output(humiLEDPin,GPIO.LOW)
            print("Humidity Stabilized")
            strHumiStab = "Humidity Stabilized {} Time: {}".format(strHumi,strDate)
            if humiState != prevHumiState:                
                try:
                    sendMessages("Humidity Stabilized", strHumiStab)
                    print("Humidity Stabilized Message Sent")  
                    prevHumiState = humiState
                    GPIO.output(pasMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pasMessageLEDPin,GPIO.LOW) 
                except:
                    print("Message Error")
                    GPIO.output(errMessageLEDPin,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(errMessageLEDPin,GPIO.LOW) 

    

         
            

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    # except Exception as error:
    #     mylcd.lcd_clear()
    #     mylcd.lcd_display_string("Error")
    #     dhtDevice.exit()
    #     GPIO.cleanup()
    #     raise error

    time.sleep(2.0)
lcd.clear()
GPIO.cleanup()



