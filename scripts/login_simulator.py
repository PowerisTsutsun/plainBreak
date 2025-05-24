import sqlite3

def simulate_login(username, password):
    conn = sqlite3.connect("data/users.db")
    c = conn.cursor()

    # WARNING: This is intentionally insecure (no hashing or input sanitization)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    c.execute(query, (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        print(f"[+] Login successful: Welcome {username}")
        return True
    else:
        print("[-] Login failed: Invalid username or password")
        return False

if __name__ == "__main__":
    print("=== Simulated Login System ===")
    user = input("Username: ")
    pw = input("Password: ")
    simulate_login(user, pw)
