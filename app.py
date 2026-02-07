from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = get_db_connection()
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                     (name, email))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
