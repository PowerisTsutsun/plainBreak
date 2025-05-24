import sqlite3
import itertools
import string
from scripts.utils import log_cracked_passwords, timer


@timer
def brute_force_attack(db_path, max_length=4):
    print("[*] Starting brute-force attack...")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT username, password FROM users")
    users = c.fetchall()

    chars = string.ascii_lowercase + string.digits
    cracked = []
    for username, real_pw in users:
        found = False
        for length in range(1, max_length + 1):
            for attempt in itertools.product(chars, repeat=length):
                guess = ''.join(attempt)
                if guess == real_pw:
                    print(f"[+] Password found for {username}: {guess}")
                    cracked.append((username, guess))
                    found = True
                    break
            if found:
                break
        else:
            print(f"[-] No match for {username}")

    conn.close()
    log_cracked_passwords(cracked)
    print("[*] Brute-force attack complete.")
    return cracked

if __name__ == "__main__":
    db_path = "data/users.db"
    brute_force_attack(db_path, max_length=4)
