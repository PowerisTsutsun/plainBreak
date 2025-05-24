import sqlite3

def create_users_db():
    conn = sqlite3.connect("data/users.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("CREATE TABLE users (username TEXT, password TEXT)")
    
    # Add sample users with plaintext passwords
    users = [
        ('admin', '123456'),
        ('user1', 'password'),
        ('guest', 'letmein'),
        ('test', 'qwerty'),
        ('demo', 'abc123')
    ]
    
    c.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)
    conn.commit()
    conn.close()
    print("[+] users.db created successfully with sample data.")

if __name__ == "__main__":
    create_users_db()
