import sqlite3
import datetime
import os

# Ensure the directory exists
os.makedirs('data', exist_ok=True)

# Database connection
conn = sqlite3.connect('data/timestamps.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS timestamp_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Get current timestamp
current_time = datetime.datetime.now()

# Insert current timestamp
cursor.execute('INSERT INTO timestamp_logs (timestamp) VALUES (?)', 
               (current_time.strftime('%Y-%m-%d %H:%M:%S'),))

# Commit changes
conn.commit()

# Fetch and print all timestamps
cursor.execute('SELECT * FROM timestamp_logs')
timestamps = cursor.fetchall()

print("Saved Timestamps:")
for record in timestamps:
    print(f"ID: {record[0]}, Timestamp: {record[1]}")

# Close connection
conn.close()