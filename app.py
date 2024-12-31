from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def home():
    # Get current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Define the target New Year 2025 time (January 1st, 2025 at midnight)
    new_year = datetime(2025, 1, 1, 0, 0, 0)
    
    # Calculate the countdown time difference
    time_left = new_year - datetime.now()
    
    # Extract hours, minutes, seconds for countdown
    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds % 3600) // 60
    seconds_left = time_left.seconds % 60
    
    return render_template('index.html', current_time=current_time, 
                           days_left=days_left, hours_left=hours_left, 
                           minutes_left=minutes_left, seconds_left=seconds_left)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
