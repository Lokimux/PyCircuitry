from machine import Pin
from time import sleep
import dht

# Define the DHT11 sensor pin
dht_pin = Pin(14)  # Replace with the GPIO pin you're using
sensor = dht.DHT11(dht_pin)

while True:
    try:
        # Trigger the sensor to read data
        sensor.measure()
        temp = sensor.temperature()  # Read temperature
        hum = sensor.humidity()  # Read humidity
        
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {hum}%")
        
    except OSError as e:
        print("Failed to read from DHT sensor:", e)
    
    # Wait for 2 seconds before reading again
    sleep(2)
