import sqlite3
import datetime
import os

# Database setup and connection
def get_db_connection():
    """Create a connection to the SQLite database."""
    # Ensure the directory exists
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect('data/timestamps.db')
    return conn

def setup_database():
    """Create the timestamps table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS timestamp_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def log_current_timestamp():
    """Insert the current timestamp into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get current timestamp
    current_time = datetime.datetime.now()
    
    # Insert current timestamp
    cursor.execute('INSERT INTO timestamp_logs (timestamp) VALUES (?)', 
                   (current_time.strftime('%Y-%m-%d %H:%M:%S'),))
    
    conn.commit()
    conn.close()

def fetch_all_timestamps():
    """Retrieve and print all saved timestamps."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Fetch all timestamps
    cursor.execute('SELECT * FROM timestamp_logs')
    timestamps = cursor.fetchall()
    
    print("Saved Timestamps:")
    for record in timestamps:
        print(f"ID: {record[0]}, Timestamp: {record[1]}")
    
    conn.close()

def main():
    # Setup the database
    setup_database()
    
    # Log current timestamp
    log_current_timestamp()
    
    # Fetch and print all timestamps
    fetch_all_timestamps()

if __name__ == '__main__':
    main()
