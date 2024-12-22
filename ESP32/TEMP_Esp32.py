import time
import urequests
import dht
from machine import Pin
import network

# Pin Configuration
dht_pin = Pin(14)  # GPIO pin connected to DHT11 data pin
led_pin = Pin(27, Pin.OUT)  # GPIO pin connected to LED
sensor = dht.DHT11(dht_pin)

# Wi-Fi Configuration
SSID = "lokimux"  # Replace with your Wi-Fi SSID
PASSWORD = "11072004"  # Replace with your Wi-Fi password

# Telegram Bot Configuration
BOT_TOKEN = "bot_token"  # Replace with your Telegram bot token
CHAT_ID = "your_chat_id"  # Replace with your chat ID
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Function to connect to Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
        print("Trying to connect...")

    print("Connected to Wi-Fi!")
    print("Network config:", wlan.ifconfig())

# Function to send data to Telegram
def send_to_telegram(temperature, humidity):
    message = (
        "🌡️ Temperature & Humidity \n\n"
        "-----------------------------------\n"
        f"Temperature:  {temperature}°C\n"
        f"Humidity:     {humidity}%\n"
        "-----------------------------------\n"
        "📡📡📡Stay updated with your environment!"
    )
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
    }
    try:
        response = urequests.post(TELEGRAM_URL, json=data)
        response.close()
        print("Message sent to Telegram.")
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

# Main Function
def main():
    connect_to_wifi()  # Connect to Wi-Fi
    while True:
        try:
            # Read data from DHT11
            sensor.measure()
            temperature = sensor.temperature()
            humidity = sensor.humidity()

            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

            # Send data to Telegram
            send_to_telegram(temperature, humidity)

            # Blink LED if temperature >= 30
            if temperature >= 30:
                for _ in range(10):  # Blink 10 times very fast
                    led_pin.value(not led_pin.value())
                    time.sleep(0.1)
                led_pin.value(0)  # Turn off LED
            else:
                led_pin.value(0)  # Ensure LED is off when temperature < 30

            # Wait 5 minutes before the next reading
            time.sleep(30)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)  # Retry after 5 seconds if an error occurs

# Run the main function
main()
