import sqlite3
from scripts.utils import log_cracked_passwords, timer


@timer
def dictionary_attack(db_path, wordlist_path):
    print("[*] Starting dictionary attack...")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT username, password FROM users")
    users = c.fetchall()

    with open(wordlist_path, 'r', encoding='latin-1') as f:
        words = f.read().splitlines()

    cracked = []
    for username, real_pw in users:
        for guess in words:
            if guess == real_pw:
                print(f"[+] Password found for {username}: {guess}")
                cracked.append((username, guess))
                break
        else:
            print(f"[-] No match for {username}")

    conn.close()
    log_cracked_passwords(cracked)
    print("[*] Dictionary attack complete.")
    return cracked

if __name__ == "__main__":
    db_path = "data/users.db"
    wordlist_path = "data/rockyou.txt"
    dictionary_attack(db_path, wordlist_path)