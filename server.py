import socket


def connect(port):
	try:
		sock.bind(("", port))
		print(f"Подключился к порту {port}")
	except OSError:
		connect(port+1)

with open("log.txt", "a") as file:
	file.write("Сервер запущен\n")
sock = socket.socket()
try:
	port = int(input("К какому порту подключаться"))
except ValueError:
	port = 9090
connect(port)
sock.listen(0)
with open("log.txt", "a") as file:
	file.write("Начато прослушивание порта\n")
conn, addr = sock.accept()
with open("log.txt", "a") as file:
	file.write("Клиент подключен\n")
msg = ''

while True:
	data = conn.recv(1024)
	with open("log.txt", "a") as file:
		file.write("Приняты данные от клиента\n")
	decoded = data.decode()
	if decoded == 'exit':
		with open("log.txt", "a") as file:
			file.write("Соединение разорвано\n")
		conn, addr = sock.accept()
		continue_listening = input("Продолжить прослушивание порта?")
		if continue_listening == "no":
			conn.close()
			break
	else:
		msg += data.decode()
		conn.send(data)
		with open("log.txt", "a") as file:
			file.write("Клиенту отправлены данные\n")
with open("log.txt", "a") as file:
	file.write("Сервер остановлен")