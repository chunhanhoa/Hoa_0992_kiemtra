from flask import Flask, render_template, request, json
from cipher.vigenere import VigenereCipher


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']  # Key should be a string
    Vigenere = VigenereCipher()

    encrypted_text = Vigenere.vigenere_encrypt(text, key)  # Use correct method name
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']  # Key should be a string
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)  # Use correct method name
    return f"text: {text}</br>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)