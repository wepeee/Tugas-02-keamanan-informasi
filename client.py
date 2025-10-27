import requests
from des_utils import encrypt_message, decrypt_message

# Ganti URL ini dengan URL HTTPS dari ngrok kamu (harus pakai /send di akhir)
SERVER_URL = "https://abcd-1234.ngrok-free.app/send"

print("=== DES HTTP Client ===")
print("Pastikan server_http.py dan ngrok http 5000 sudah berjalan!\n")

while True:
    try:
        # Input pesan dari user
        message = input("You: ").strip()
        if not message:
            continue

        # Enkripsi pesan sebelum dikirim
        cipher = encrypt_message(message)
        payload = {"cipher": cipher}

        # Kirim ke server lewat HTTP POST JSON
        response = requests.post(SERVER_URL, json=payload, timeout=15)

        # Cek apakah server berhasil merespons
        if response.status_code != 200:
            print(f"⚠️ Server error {response.status_code}: {response.text}")
            continue

        # Coba parse response JSON dari server
        try:
            data = response.json()
        except Exception as e:
            print("⚠️ Gagal parsing JSON dari server:", e)
            print("Response mentah:", response.text)
            continue

        # Ambil balasan terenkripsi
        reply_enc = data.get("reply", "")
        if not reply_enc:
            print("⚠️ Balasan dari server kosong!")
            continue

        # Dekripsi balasan
        reply_dec = decrypt_message(reply_enc)

        # Tampilkan hasil
        print("\n[Encrypted reply]:", reply_enc)
        print("[Decrypted reply]:", reply_dec, "\n")

    except KeyboardInterrupt:
        print("\n❌ Program dihentikan oleh user.")
        break
    except requests.exceptions.RequestException as e:
        print("⚠️ Error koneksi:", e)
