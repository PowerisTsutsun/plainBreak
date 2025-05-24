# plainBreak - Non Hashed password cracking 🔓
A Python-based password cracking toolkit featuring dictionary and brute-force attacks for educational and ethical security testing.

---

## 🚀 Features
- **Dictionary Attack**: Tests passwords against a provided wordlist (e.g., `rockyou.txt` in `/data`).
- **Brute Force Attack**: Exhaustive search for all possible password combinations up to a set length.
- **Login Simulation**: Test login attempts with cracked passwords from `users.db`.
- **GUI Support**: Basic GUI (`gui/app.py`) for easier interaction.
- **Test Suite**: Contains tests for the cracking methods in `/tests`.

---

## 🗂️ Project Structure
```
plainBreak/
├── data/
│ ├── rockyou.txt
│ └── users.db
├── docs/
│ ├── analysis.txt
│ └── project_report.pdf
├── gui/
│ └── app.py
├── results/
│ ├── cracked_log.txt
│ ├── presentation.pptx
│ └── project_report.pdf
├── scripts/
│ ├── brute_force.py
│ ├── create_db.py
│ ├── dictionary_attack.py
│ ├── login_simulator.py
│ ├── utils.py
├── src/
│ └── Images of the project
├── tests/
│ └── test_crack_methods.py
└── requirements.txt

```
---

## 🛠️ Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/PowerisTsutsun/plainBreak.git
   cd plainBreak
   
# Dictionary Attack
 - python scripts/dictionary_attack.py

# Brute Force Attack
 - python scripts/brute_force.py
   
# Create Sample Users Database
 - python scripts/create_db.py
   
# Simulate Logins with Cracked Passwords
 - python scripts/login_simulator.py

# Launch GUI
 - python gui/app.py

