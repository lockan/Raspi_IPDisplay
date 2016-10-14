from __future__ import print_function
import time
import socket
import Adafruit_CharLCD as LCD

# TUNEABLES
GATEWAY = "192.168.1.254"
DISPLAYTIME = 10

# LCD OBJECT
lcd = LCD.Adafruit_CharLCDPlate()

# Creates a socket to GATEWAY and returns local network IP address
def GetDeviceIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((GATEWAY, 0))  # connecting to a UDP address doesn't send packets
    ip = s.getsockname()[0]
    return ip

# Displays the IP of the device for 10 seconds, then turns the LCD display off. 
def DisplayIP(ip):
    lcd.enable_display(True)
    lcd.set_backlight(1)
    lcd.clear()
    lcd.message(ip)
    time.sleep(DISPLAYTIME)
    lcd.clear()
    lcd.enable_display(False)
    lcd.set_backlight(0)

if __name__ == "__main__":
    ip = GetDeviceIP()
    DisplayIP(ip)
    exit(0)
