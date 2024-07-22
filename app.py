from flask import Flask, request, redirect, render_template, url_for, flash
import sqlite3
import string
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'url_shortener.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_id TEXT NOT NULL UNIQUE
            )
        ''')
        db.commit()

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    db = get_db()
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))
        
        short_id = generate_short_id()
        db.execute('INSERT INTO urls (original_url, short_id) VALUES (?, ?)', (url, short_id))
        db.commit()
        
        short_url = request.host_url + short_id
        flash(f'Shortened URL: {short_url}')
    
    urls = db.execute('SELECT original_url, short_id FROM urls').fetchall()
    return render_template('index.html', urls=urls)

@app.route('/<short_id>')
def redirect_to_url(short_id):
    db = get_db()
    result = db.execute('SELECT original_url FROM urls WHERE short_id = ?', (short_id,)).fetchone()
    
    if result is None:
        flash('Invalid URL')
        return redirect(url_for('index'))
    
    return redirect(result['original_url'])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
