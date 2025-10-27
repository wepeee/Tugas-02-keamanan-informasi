import socket
from des_utils import encrypt_message, decrypt_message

# Ganti setelah ngrok dijalankan
HOST = '4.tcp.ngrok.io'
PORT = 14732

s = socket.socket()
s.connect((HOST, PORT))
print("Connected to server!")

while True:
    msg = input("You: ")
    s.send(encrypt_message(msg).encode())
    data = s.recv(2048).decode()
    print("\n[Encrypted]:", data)
    print("[Decrypted]:", decrypt_message(data))
