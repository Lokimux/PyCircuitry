from machine import Pin, I2C
from time import sleep
import math

# MPU6050 Registers and Addresses
MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

# Initialize I2C
i2c = I2C(0, scl=Pin(25), sda=Pin(26))  # Update with your SDA/SCL pins

# Wake up MPU6050
i2c.writeto_mem(MPU6050_ADDR, PWR_MGMT_1, b'\x00')

def read_raw_data(addr):
    # Read two bytes of data from the given register
    high = i2c.readfrom_mem(MPU6050_ADDR, addr, 1)
    low = i2c.readfrom_mem(MPU6050_ADDR, addr + 1, 1)
    value = (high[0] << 8) | low[0]
    # Convert to signed
    if value > 32768:
        value -= 65536
    return value

while True:
    # Read Accelerometer values
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_XOUT_H + 2)
    acc_z = read_raw_data(ACCEL_XOUT_H + 4)

    # Read Gyroscope values
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_XOUT_H + 2)
    gyro_z = read_raw_data(GYRO_XOUT_H + 4)

    # Convert raw data to g's for acceleration and degrees/sec for gyro
    acc_x_g = acc_x / 16384.0
    acc_y_g = acc_y / 16384.0
    acc_z_g = acc_z / 16384.0

    gyro_x_dps = gyro_x / 131.0
    gyro_y_dps = gyro_y / 131.0
    gyro_z_dps = gyro_z / 131.0

    print(f"Accel (g): X={acc_x_g:.2f}, Y={acc_y_g:.2f}, Z={acc_z_g:.2f}")
    print(f"Gyro (°/s): X={gyro_x_dps:.2f}, Y={gyro_y_dps:.2f}, Z={gyro_z_dps:.2f}")
    print("")

    sleep(1)
