import ipaddress
import socket
from ipaddress import ip_address

sock = socket.socket()
sock.setblocking(1)
try:
    ip = ipaddress.ip_address(input("К какому ip подключаться?"))
except ValueError:
    ip = "127.0.0.1"
try:
    port = int(input("К какому порту подключаться"))
except ValueError:
    port = 9090
sock.connect((ip, port))
print("Соединение установлено")
while True:
    line = input()
    sock.send(line.encode())
    print("Данные отправлены")
    if line == "exit":
        print("Соединение разорвано")
        break
    data = sock.recv(1024)
    print("Данные получены:")
    print(data.decode())
sock.close()
