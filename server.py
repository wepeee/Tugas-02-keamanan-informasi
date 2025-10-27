from flask import Flask, request, jsonify
from des_utils import encrypt_message, decrypt_message

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def receive_message():
    data = request.get_json()
    encrypted_text = data.get("cipher")
    print("\n[Encrypted]:", encrypted_text)
    decrypted = decrypt_message(encrypted_text)
    print("[Decrypted]:", decrypted)
    
    # balasan terenkripsi
    reply_text = input("Balas pesan: ")
    reply_encrypted = encrypt_message(reply_text)
    return jsonify({"reply": reply_encrypted})

if __name__ == "__main__":
    app.run(port=5000)
