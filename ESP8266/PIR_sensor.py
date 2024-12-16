from machine import Pin
from time import sleep

# Define the pins
pir_pin = 5  # D1 on NodeMCU
led_pin = 2  # D4 on NodeMCU (built-in LED)

# Set up the pins
pir = Pin(pir_pin, Pin.IN)
led = Pin(led_pin, Pin.OUT)

print("PIR sensor is initializing...")
sleep(2)  # Give time for PIR sensor to stabilize
print("PIR sensor ready.")

try:
    while True:
        if pir.value():  # Motion detected
            print("Motion detected!")
            for _ in range(10):  # Blink the LED rapidly
                led.on()
                sleep(0.05)  # 50 ms on
                led.off()
                sleep(0.05)  # 50 ms off
        else:
            led.off()  # Ensure LED is off when no motion
except KeyboardInterrupt:
    print("Program stopped.")
