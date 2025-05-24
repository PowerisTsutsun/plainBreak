import unittest
import sys
import os

# Insert the root directory (plainBreak/) into sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.create_db import create_users_db
from scripts.dictionary_attack import dictionary_attack
from scripts.brute_force import brute_force_attack

class TestCrackMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_users_db()  # Ensure the database is initialized

    def test_dictionary_attack(self):
        cracked = dictionary_attack("data/users.db", "data/rockyou.txt")
        cracked_usernames = [user for user, _ in cracked]
        self.assertIn("admin", cracked_usernames)
        self.assertIn("user1", cracked_usernames)

    def test_brute_force_attack(self):
        cracked = brute_force_attack("data/users.db", max_length=4)
        cracked_usernames = [user for user, _ in cracked]
        self.assertIn("admin", cracked_usernames)
        self.assertIn("user1", cracked_usernames)

if __name__ == "__main__":
    unittest.main()
