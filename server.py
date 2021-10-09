import socket  # импорт библиотеки сокетов

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создание сокета
self_ip = "127.0.0.1"  # свой ip
self_port = 9090  # свой порт
addrs = []  # массив с адресами клиентов
sock.bind((self_ip, self_port))
while True:
	data, addr = sock.recvfrom(1024)  # получаем сообщение
	if addr not in addrs:  # если столкнулись с адресом впервые, добавляем его в список
		addrs.append(addr)
	decoded = data.decode()  # расшифровка сообщения
	if decoded != "first_try_connection":
		for i in addrs:  # отсылаем присланное сообщение всем известным клиентам
			tosend = ("client, with ip= "+str(addr[0])+"port= "+str(addr[1])+"said:  "+decoded).encode()
			sock.sendto(tosend, i)

