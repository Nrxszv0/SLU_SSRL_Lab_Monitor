import RPi.GPIO as GPIO
import dht11
import time
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 4)
while True:
    result = instance.read()
    print("Temperature: %-3.1f C" % result.temperature)
    print(result.temperature)

    # print("Humidity: %-3.1f %%" % result.humidity)
    time.sleep(1)


# if result.is_valid():

# else:
    # print("Error: %d" % result.error_code)