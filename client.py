import requests
from des_utils import encrypt_message, decrypt_message

SERVER_URL = "https://groved-mark-unimpearled.ngrok-free.dev/send"

print("=== DES HTTP Client ===")

while True:
    try:
        message = input("You: ").strip()
        if not message:
            continue

        cipher = encrypt_message(message)
        payload = {"cipher": cipher}

        response = requests.post(SERVER_URL, json=payload, timeout=15)

        if response.status_code != 200:
            print(f"Server error {response.status_code}: {response.text}")
            continue

        try:
            data = response.json()
        except Exception as e:
            print("Gagal parsing JSON dari server:", e)
            print("Response mentah:", response.text)
            continue

        reply_enc = data.get("reply", "")
        if not reply_enc:
            print("Balasan dari server kosong!")
            continue

        reply_dec = decrypt_message(reply_enc)

        print("\n[Encrypted reply]:", reply_enc)
        print("[Decrypted reply]:", reply_dec, "\n")

    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user.")
        break
    except requests.exceptions.RequestException as e:
        print("Error koneksi:", e)
