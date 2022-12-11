from flask import Flask, jsonify, session
from flask_cors import CORS, cross_origin
import sqlite3

# create database if not exists
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(userId INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS rooms(roomId INTEGER PRIMARY KEY, hearts INTEGER, smiley INTEGER, upvote INTEGER, downvote INTEGER, previous1 TEXT, previous2 TEXT, previous3 TEXT, previous4 TEXT, previous5 TEXT)''')
# create fake data
for i in range(0, 5):
    c.execute("SELECT * FROM rooms WHERE roomId = ?", (i,))
    if c.fetchone() is None:
        c.execute("INSERT INTO rooms VALUES (?, 0, 0, 0, 0, 'Lucas', 'Sandra', 'John Filip', 'Ping', 'Default')", (i,))
conn.commit()
conn.close()

DEBUG = True
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

@app.route('/rooms/<roomId>')
@cross_origin()
def rooms(roomId):
    with sqlite3.connect ('database.db') as conn:
        c = conn.cursor()
        c.execute("SELECT roomId FROM rooms")
        rooms = c.fetchall()
        c.execute("SELECT * FROM rooms WHERE roomId = ?", (roomId,))
        room = c.fetchone()
        return jsonify({'rooms': rooms, 'room': room})
    
@app.route('/react/<roomId>/<name>/<num>')
@cross_origin()
def react(roomId, name, num):
    with sqlite3.connect ('database.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM rooms WHERE roomId = ?", (roomId,))
        room = c.fetchone()
        if num == '1':
            c.execute("UPDATE rooms SET hearts = ? WHERE roomId = ?", (room[1] + 1, roomId))
        elif num == '2':
            c.execute("UPDATE rooms SET smiley = ? WHERE roomId = ?", (room[2] + 1, roomId))
        elif num == '3':
            c.execute("UPDATE rooms SET upvote = ? WHERE roomId = ?", (room[3] + 1, roomId))
        elif num == '4':
            c.execute("UPDATE rooms SET downvote = ? WHERE roomId = ?", (room[4] + 1, roomId))
        elif num == '5':
            c.execute("UPDATE rooms SET previous1 = ? WHERE roomId = ?", (room[5], roomId))
            c.execute("UPDATE rooms SET previous2 = ? WHERE roomId = ?", (room[6], roomId))
            c.execute("UPDATE rooms SET previous3 = ? WHERE roomId = ?", (room[7], roomId))
            c.execute("UPDATE rooms SET previous4 = ? WHERE roomId = ?", (room[8], roomId))
            c.execute("UPDATE rooms SET previous5 = ? WHERE roomId = ?", (name, roomId))

if __name__ == '__main__':
    app.run()