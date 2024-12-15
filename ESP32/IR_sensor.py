from machine import Pin
from time import sleep

# Define the GPIO pin for the IR sensor
ir_sensor = Pin(14, Pin.IN)  # Replace GPIO4 with the pin you are using

while True:
    # Read the sensor state
    sensor_state = ir_sensor.value()
    
    if sensor_state == 0:
        print("Object detected!")
    else:
        print("No object detected.")
    
    sleep(1)  # Wait for 500 ms before reading again
