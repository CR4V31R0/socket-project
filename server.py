import socket

HOST = "127.0.0.1"
PORT = 5000

# Criando socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print("Servidor iniciado...")
print("Aguardando conexão...")

conn, addr = server.accept()
print("Cliente conectado:", addr)

while True:
    data = conn.recv(1024)

    if not data:
        break

    mensagem = data.decode()
    print("Mensagem recebida:", mensagem)

    resposta = "Servidor recebeu: " + mensagem
    conn.send(resposta.encode())

conn.close()
server.close()