import time

def log_cracked_passwords(cracked, log_path="results/cracked_log.txt"):
    with open(log_path, 'w') as f:
        for username, password in cracked:
            f.write(f"{username}:{password}\n")
    print(f"[+] Cracked passwords logged to {log_path}")

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[i] Execution time: {end - start:.2f} seconds")
        return result
    return wrapper