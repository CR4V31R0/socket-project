import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Conectado ao servidor!")

while True:
    mensagem = input("Digite uma mensagem (ou 'sair'): ")

    if mensagem.lower() == "sair":
        break

    client.send(mensagem.encode())

    resposta = client.recv(1024)
    print("Resposta do servidor:", resposta.decode())

client.close()