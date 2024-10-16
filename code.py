import os
import ipaddress
import microcontroller
import wifi
import socketpool
import time

print("Circuitpython program started")

try:
	print("made it into the try statement")


	print("Connecting to WiFi")

	#  connect to your SSID
	wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

	print("Connected to WiFi")

	pool = socketpool.SocketPool(wifi.radio)

	#  prints MAC address to REPL
	print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

	#  prints IP address to REPL
	print("My IP address is", wifi.radio.ipv4_address)

	#  pings Google
	ipv4 = ipaddress.ip_address("8.8.4.4")
	while(1):
		print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
		time.sleep(1)

except Exception as e:
    print("Error:\n", str(e))
    print("Resetting microcontroller in 10 seconds")
    time.sleep(10)
    microcontroller.reset() # this line doesn't work
