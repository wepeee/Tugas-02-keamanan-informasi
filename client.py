import requests
from des_utils import encrypt_message, decrypt_message

# Ganti URL setelah ngrok dijalankan
SERVER_URL = "https://abcd-1234.ngrok-free.app/send"

while True:
    message = input("You: ")
    cipher = encrypt_message(message)
    payload = {"cipher": cipher}
    response = requests.post(SERVER_URL, json=payload)
    data = response.json()
    
    reply_enc = data.get("reply")
    print("\n[Encrypted reply]:", reply_enc)
    print("[Decrypted reply]:", decrypt_message(reply_enc))
