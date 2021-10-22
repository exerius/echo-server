import ipaddress
import socket
from ipaddress import ip_address 


def recv(connection): # функция получения сообщения
    head = int(connection.recv(1024).decode())
    data = connection.recv(head)
    return data.decode()


def send(connection, message): # функция отправки сообщения
    message = message.encode()

    header = str(len(message)).encode()
    connection.send(header)
    connection.send(message)


def respond(idd, message): # функция ответа на какое-то сообщение
    #send(sock, "!!!re!!!")
    #send(sock, idd)
    send(sock, str(message+"|"+str(idd)))


sock = socket.socket() # создаем сокет
sock.setblocking(1)
try:
    ip = ipaddress.ip_address(input("К какому ip подключаться?")) # ввод ip
except ValueError:
    ip = "127.0.0.1"
try:
    port = int(input("К какому порту подключаться")) # ввод порта
except ValueError:
    port = 9090
sock.connect((ip, port)) # подключение к порту
print("Соединение установлено")
while True:
    line = input("Введите сообщение") # отправка сообщения
    if line[:3] == "re:": # отправка ответа (в начале нужно написать re:+номер сообщения)
        respond(line[3], line[4:])
    else:
        send(sock, line) #отправка сообщения
        print("Данные отправлены")
        if line == "exit":
            print("Соединение разорвано")
            break
    data = recv(sock)
    print("Данные получены:")
    print(data) # получение ответа
sock.close()
