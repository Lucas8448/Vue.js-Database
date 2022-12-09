from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import sqlite3

# create database if not exists
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(userId INTEGER PRIMARY KEY)''')
c.execute('''CREATE TABLE IF NOT EXISTS rooms(roomId INTEGER PRIMARY KEY, hearts INTEGER, smiley INTEGER, upvote INTEGER, downvote INTEGER, previous1 TEXT, previous2 TEXT, previous3 TEXT, previous4 TEXT)''')
# create fake data
for i in range(0, 5):
    c.execute("SELECT * FROM rooms WHERE roomId = ?", (i,))
    if c.fetchone() is None:
        c.execute("INSERT INTO rooms VALUES (?, 0, 0, 0, 0, 'Lucas', 'Sandra', 'John Filip', 'Ping')", (i,))
conn.commit()
conn.close()

DEBUG = True
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

@app.route('/rooms/', methods=['GET'])
@cross_origin()
def rooms():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    data = c.fetchall()
    conn.close()
    return jsonify(data)


@app.route('/rooms/<int:roomId>', methods=['GET'])
@cross_origin()
def room(roomId):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM rooms WHERE roomId = ?", (roomId,))
    data = c.fetchone()
    conn.close()
    return jsonify(data)

@app.route('/login')
@cross_origin()
def login():
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run()