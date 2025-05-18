import subprocess
import os

# Run app.py (Flask app) in a subprocess
flask_process = subprocess.Popen(['python', 'app.py'])

# Wait for both processes to finish (if you want to wait until both are done)
flask_process.wait()
