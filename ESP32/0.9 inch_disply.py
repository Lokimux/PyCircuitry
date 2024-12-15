from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Initialize I2C interface
i2c = I2C(0, scl=Pin(26), sda=Pin(25))  # Adjust pins if needed

# Define OLED dimensions
oled_width = 128
oled_height = 64

# Initialize the OLED display
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# Clear the display
oled.fill(0)

# Display "Hi" in the center
text = "Hi"
char_width = 8  # Default font character width
char_height = 8  # Default font character height

# Calculate position to center the text
x_pos = (oled_width - (len(text) * char_width)) // 2
y_pos = (oled_height - char_height) // 2

oled.text(text, x_pos, y_pos)

# Show the content on the display
oled.show()
