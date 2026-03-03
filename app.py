from flask import Flask, request, jsonify
from hash_utils import sha256_bytes
from crypto_utils import encrypt_data, decrypt_data, generate_key

app = Flask(__name__)
key = generate_key()

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = file.read()

    file_hash = sha256_bytes(data)
    encrypted = encrypt_data(data, key)

    return jsonify({
        "hash": file_hash,
        "message": "File encrypted and hashed successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)