from flask import Flask
import os
import time
from datetime import datetime
from pytz import timezone
import psutil
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Prashant Kumar"
    username = getpass.getuser()
    server_time = datetime.now().astimezone(timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

    top_output = "\n".join([f"{p.info['name']} - {p.info['cpu_percent']}%" for p in psutil.process_iter(attrs=['name', 'cpu_percent'])])

    return f"""
    <h1>System Info</h1>
    <p><strong>Full Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre><strong>Top Output:</strong></pre><pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
