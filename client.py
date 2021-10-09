import socket  # импорт библиотеки сокетов
from threading import Thread  # импорт потока для многопоточности


def listenig():  # функция прослушки сервера
    while True:
        try:
            data = sock.recv(1024)
        except:
            continue
        else:
            print(data.decode())
    sock.close()


def sending():  # функция отправки сообщений на сервер
    while True:
        line = input()
        sock.sendto(line.encode(), server_addr)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создание сокета
server_addr = (input("Введите ip сервера"), int(input("Введите порт сервера")))
sock.sendto(b"first_try_connection", server_addr)
thread1 = Thread(target=listenig)  # один поток слушает
thread2 = Thread(target=sending)  # а другой -- пишет
thread1.start()
thread2.start()