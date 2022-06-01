import socket
import network
from time import sleep
from machine import PWM, Pin

buzzer = PWM(Pin(5),freq = 2000, duty = 500)
buzzer.deinit()
sw = Pin(22,Pin.IN)

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.config(essid='ESP-AP') # set the ESSID of the access point
ap.config(max_clients=1) # set how many clients can connect to the network
ap.active(True)
def listen():
    value = 0
    try:
        c, addr = s.accept()
        value = c.recv(1024).decode()
        sleep(1)
        print('Got connection from', addr)
        message = ('Information received')
        c.send(message.encode())
        c.close()
        if value == "1":
            print("connected")
        elif value == "":
            print("empty")
    except OSError:
        print("disconnected")
#             listen()
        
def beep():
    buzzer.init()
s = socket.socket()
print('Socket succesfully created')
port = 1234
s.bind(('',port))
print('Socket binded to port', port)
s.listen(1)
print('Socket is listening')

for i in range(0,10):
    ap.active(True)
    listen()
    sleep(20)
    ap.active(False)
    listen()
    print("Test",i+1)
    sleep(5)   