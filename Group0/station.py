from machine import Pin,PWM
import network
from time import sleep
import socket
buzzer = PWM(Pin(5),freq = 2000, duty=500)
buzzer.deinit()
sw = Pin(22,Pin.IN)
wlan = network.WLAN(network.STA_IF)
def beep():
        buzzer.init()
        sleep(0.5)
        buzzer.deinit()
        sleep(0.5)
    
def do_connect():
    wlan.active(True)
#     def handle_interrupt(pin):
#         sw.value(not sw.value())
#         if sw.value() == 1:
#             print("on")
#         else:
#             print("off")
#     sw.irq(trigger = Pin.IRQ_RISING, handler = handle_interrupt)
    if not wlan.isconnected():
        print('beeping')
        print('connecting to network...')
        beep()
        wlan.connect('ESP-AP', '')
        while not wlan.isconnected():
            beep()
            pass
    print('network config:', wlan.ifconfig())
    
def is_connected():
    return wlan.isconnected()
def client_listen(val):
    do_connect()
    #after connection is successful...
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = "192.168.4.1"
    PORT = 1234
    def send_message(msg):
        value = "1"
        c.send(bytes(msg, 'utf-8'))
    def connect_server():
        value= "0"
        try:
            c.connect((IP,PORT))
            sleep(1)
            send_message(value)
            print(c.recv(1024).decode())
            c.close()
        except OSError:
            print("Unable to receive connection")
    client_listen(val)
# To constantly check for wifi connection
# once the connection is lost the device will beep until connection has been established again
def main_func():
    do_connect()
    sleep(1)
    while is_connected():
        val = "1"
        print(val)
        client_listen(val)
        print('network config:', wlan.ifconfig())
        sleep(4)
        if is_connected():
            client_listen(val)
            pass
        else:
            main_func()
            val= "0"
            sleep(1)

main_func()