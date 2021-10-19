import socket


def recv(connection):
	head = int(connection.recv(1024).decode())
	data = connection.recv(head)
	return data


def send(connection, message):
	message = message.encode()
	header = str(len(message)).encode()
	connection.send(header)
	connection.send(message)


def connect(port):
	try:
		sock.bind(("", port))
		print(f"Подключился к порту {port}")
	except OSError:
		connect(port+1)


def respond(id, message):
		send(sock, r"!!!re!!!")
		send(sock, str(id).encode())
		quote = recv(sock)
		send(sock, str("responded to \"" + quote + "\"" + ":" + message).encode())


def respond_recieved(data):
	message, idd = data.split("|")
	respond_to = messages[int(idd)]
	to_send =  str("responed to \""+respond_to+"\":\n"+message)
	print(to_send)
	send(conn, to_send)
	with open("log.txt", "a") as file:
		file.write("Клиенту отправлены данные\n")


with open("log.txt", "a") as file:
	file.write("Сервер запущен\n")
messages = []
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
	data = recv(conn)
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
	elif "|" in decoded:
		respond_recieved(decoded)
	else:
		messages.append(decoded)
		msg += data.decode()
		send(conn, data.decode())
		with open("log.txt", "a") as file:
			file.write("Клиенту отправлены данные\n")
with open("log.txt", "a") as file:
	file.write("Сервер остановлен")