from flask import Flask, request, render_template_string, jsonify
import os
import pickle
import subprocess
import sqlite3

app = Flask(__name__)

# Security Issue 1: Hardcoded credentials
API_KEY = "sk_live_abc123xyz789"
DB_PASSWORD = "admin123"

@app.route('/')
def home():
    return 'Welcome to Security Demo'

# Security Issue 2: SQL Injection vulnerability
@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # VULNERABLE: Direct string concatenation in SQL
    sql = f"SELECT * FROM users WHERE username = '{query}'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)})

# Security Issue 3: Command Injection vulnerability
@app.route('/execute')
def execute():
    filename = request.args.get('file', 'test.txt')
    # VULNERABLE: Direct command execution
    result = subprocess.check_output(f'cat {filename}', shell=True)
    return result

# Security Issue 4: Unsafe deserialization
@app.route('/load')
def load_pickle():
    data = request.args.get('data', '')
    # VULNERABLE: pickle.loads with untrusted data
    try:
        obj = pickle.loads(data.encode())
        return jsonify({'loaded': str(obj)})
    except Exception as e:
        return jsonify({'error': str(e)})

# Security Issue 5: Template injection (if user input used in template)
@app.route('/template')
def template_inject():
    user_input = request.args.get('msg', 'Hello')
    # VULNERABLE: User input directly in template
    template = f"<h1>{user_input}</h1>"
    return render_template_string(template)

# Security Issue 6: Debug mode in production
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
