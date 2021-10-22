#Клиент для сервера авторизации и идентификации
import socket


sock = socket.socket()
sock.setblocking(1)
sock.connect((input("Введите ip"), int(input("Введите номер порта"))))
while True:
    data = sock.recv(1024).decode()
    print(data)
    line = input()
    sock.send(line.encode())
