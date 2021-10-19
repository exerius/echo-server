import ipaddress
import socket
from ipaddress import ip_address


def recv(connection):
    head = int(connection.recv(1024).decode())
    data = connection.recv(head)
    return data.decode()


def send(connection, message):
    message = message.encode()

    header = str(len(message)).encode()
    connection.send(header)
    connection.send(message)


def respond(idd, message):
    #send(sock, "!!!re!!!")
    #send(sock, idd)
    send(sock, str(message+"|"+str(idd)))


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
    line = input("Введите сообщение")
    if line[:3] == "re:":
        print("responded")
        print(line[3], line[4:])
        respond(line[3], line[4:])
    else:
        send(sock, line)
        print("Данные отправлены")
        if line == "exit":
            print("Соединение разорвано")
            break
    print("responded")
    data = recv(sock)
    print("Данные получены:")
    print(data)
sock.close()
