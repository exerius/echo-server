#Сервер авторизации И иденттификации
import socket
import hashlib

sock = socket.socket()
sock.bind(("", 9091))
sock.listen(0)
users = {}

with open("users.txt", "r") as file:#читаем список пользователей из файла. Предполагается, что файл (хотя бы пустой) был создан заранее при "установке" программы
    for i in file:
        line = i.split(":")
        users.update({line[0]:[line[1], line[2]]})
while True:
    conn, addr = sock.accept()
    if addr[0] in users: #если мы уже знаем этот ip
        conn.send("Введите пароль".encode()) # просим пароль
        password = hashlib.md5(conn.recv(1024)).hexdigest() # пароль хранятся в виде хэшей, поэтому полученный пароль тож4е хэшиируем
        if password == users[addr[0]][1]:
            conn.send("Привет, ".encode()+users[addr[0]][0].encode()) # приветствуем
        else:
            conn.send("Пароль неверен".encode())
    else:
        conn.send("Как вас зовут?".encode()) #если ip встречается в 1-ый раз
        name = conn.recv(1024).decode() # узнаем имя
        conn.send("Введите пароль".encode()) # узнаем пароль
        password = hashlib.md5(conn.recv(1024)).hexdigest() #хэшируем пароль
        line = ":".join([addr[0], name, password])
        with open("users.txt", "a") as file:
            file.write(line)
