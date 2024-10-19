from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name and Username
    full_name = "Shaik Mohammed Saad"  # Replace with your full name
    system_username = os.getenv("USER") or os.getenv("USERNAME")


    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Top command output
    top_output = subprocess.getoutput('top -bn1 | head -10')

    # HTML Response
    return f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {system_username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Top Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == 'main':
    app.run(host='0.0.0.0')