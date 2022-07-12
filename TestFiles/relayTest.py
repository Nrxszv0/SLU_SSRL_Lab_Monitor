import RPi.GPIO as GPIO
import time

in1 = 23
in2 = 22
in3 = 27
in4 = 17

relays = [in1,in2,in3,in4]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

while True:
    for r in range(4):
        GPIO.output(relays[r],1)
        print("relay " + str(r) + ": on")
        time.sleep(1)
        GPIO.output(relays[r],0)
        print("relay " + str(r) + ": off")
        time.sleep(1)

