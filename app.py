from flask import Flask, render_template, request
from crypto import encrypt_ml, decrypt_ml

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        password = request.form.get("password", "")
        action = request.form.get("action")

        if action == "encrypt":
            result = encrypt_ml(text, password)
        elif action == "decrypt":
            result = decrypt_ml(text, password)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()