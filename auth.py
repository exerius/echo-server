import socket
import hashlib

sock = socket.socket()
sock.bind(("", 9091))
sock.listen(0)
users = {}

with open("users.txt", "r") as file:
    for i in file:
        line = i.split(":")
        users.update({line[0]:[line[1], line[2]]})
while True:
    conn, addr = sock.accept()
    if addr[0] in users:
        conn.send("Введите пароль".encode())
        password = hashlib.md5(conn.recv(1024)).hexdigest()
        if password == users[addr[0]][1]:
            conn.send("Привет, ".encode()+users[addr[0]][0].encode())
        else:
            conn.send("Пароль неверен".encode())
    else:
        conn.send("Как вас зовут?".encode())
        name = conn.recv(1024).decode()
        conn.send("Введите пароль".encode())
        password = hashlib.md5(conn.recv(1024)).hexdigest()
        line = ":".join([addr[0], name, password])
        with open("users.txt", "a") as file:
            file.write(line)
