import socket
from des_utils import encrypt_message, decrypt_message

PORT = 12345

s = socket.socket()
s.bind(('0.0.0.0', PORT))
s.listen(1)
print(f"Server listening on port {PORT}...")

conn, addr = s.accept()
print("Connected from:", addr)

while True:
    data = conn.recv(2048).decode()
    if not data:
        break
    print("\n[Encrypted]:", data)
    print("[Decrypted]:", decrypt_message(data))
    msg = input("Your reply: ")
    conn.send(encrypt_message(msg).encode())

conn.close()
