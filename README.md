# Raspi_IPDisplay
A quick little program to display the Raspi's local network IP to an Adafruit LCD display. 

##Use case: 
I have an Adafruit 16x2 LCD display connected to the GPIO of my Raspi. I typically develop by connecting via SSH through putty.  
My Raspi doesn't have a static IP address. 
Setting this script to run at boot (by adding to /etc/rc.local) allows me to see the current IP address so I know where to connect. 

##Notes: 
- Uses the Adafruit GPIO and CharLCD libraries
- Should be run as root (or sudo) using Python2.7 (imports won't work in Python3)
- Due to Adafruit library depencies, you may also need to install Pytyon 3 on your Raspi
