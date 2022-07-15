from machine import Pin
import onewire, ds18x20
import time
import socket
import network
import machine
import _thread
#powered by 阿政啊阿政
ds_pin = Pin(13)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
a = Pin(15, Pin.OUT)
b = Pin(17, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(16, Pin.OUT)
a.value(0)
b.value(0)
c.value(0)
d.value(0)
i = 0
delay_time_ms = 3
delay_time_msm = 12
recv_data_str = " "
send_data = " "
global client_socket
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('123456789', '987654321')
        i = 1
        while not wlan.isconnected():
            print("正在链接...{}".format(i))
            i += 1
            time.sleep(1)
    print('network config:', wlan.ifconfig())
def start_tcp():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_server_socket.bind(("", 8000))
    tcp_server_socket.listen(128)
    global client_socket 
    client_socket, clientAddr = tcp_server_socket.accept()
    print('客户端：', clientAddr)
    return tcp_server_socket
def read_ds_sensor():
    roms = ds_sensor.scan()
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        if isinstance(temp, float):
            temp = round(temp, 2)
            return temp
def do_ks():
    for i in range(83):
        a.value(1)
        b.value(0)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)    
        a.value(0)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)    
        a.value(0)
        b.value(0)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_ms)    
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_ms)

def do_kn():
    for i in range(83):
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_ms)    
        a.value(0)
        b.value(0)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_ms)    
        a.value(0)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)    
        a.value(1)
        b.value(0)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_ms)
def do_ms():
    for i in range(21):
        a.value(1)
        b.value(0)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_msm)    
        a.value(0)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_msm)   
        a.value(0)
        b.value(0)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_msm)
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_msm)
def do_mn():
    for i in range(21):
        a.value(0)
        b.value(0)
        c.value(0)
        d.value(1)
        time.sleep_ms(delay_time_msm)
        a.value(0)
        b.value(0)
        c.value(1)
        d.value(0)
        time.sleep_ms(delay_time_msm)  
        a.value(0)
        b.value(1)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_msm)   
        a.value(1)
        b.value(0)
        c.value(0)
        d.value(0)
        time.sleep_ms(delay_time_msm)        
def do_stop():
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)
    time.sleep_ms(delay_time_msm)
def tcpsenda():
    while True:
        print(read_ds_sensor())
        send_data = str(read_ds_sensor())
        client_socket.send(send_data.encode("utf-8"))
        time.sleep(5)
def do_recv():
    while True:
        recv_data, sender_info = client_socket.recvfrom(128)
        global recv_data_str
        recv_data_str = recv_data.decode("utf-8")
        try:
            print(recv_data_str)
        except Exception as ret:
            print("error:", ret)
        if recv_data_str == "ON":
            led.value(1)
            recv_data_str=" "
        elif recv_data_str == "OF":
            led.value(0)
            recv_data_str=" "
        elif recv_data_str == "SO":
            led.value(1)
            time.sleep_ms(100)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(100)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(100)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(500)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(500)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(500)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(100)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(100)
            led.value(0)
            time.sleep_ms(100)
            led.value(1)
            time.sleep_ms(100)
            led.value(0)
            time.sleep_ms(1000)

        elif recv_data_str == "KS": 
            do_ks()
            recv_data_str=" "
        elif recv_data_str == "KN":
            do_kn()
            recv_data_str=" "
        elif recv_data_str == "MS":
            do_ms()
            recv_data_str=" "
        elif recv_data_str == "MN":
            do_mn()
            recv_data_str=" "
def main():
    do_connect()
    tcp_socket = start_tcp()
    global led
    led = machine.Pin(2, machine.Pin.OUT)  
    _thread.start_new_thread(tcpsenda,())
    time.sleep_ms(2)
    while True:
        do_recv()
        pass
if __name__ == "__main__":
    main()