# test_transaction.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from transaction import Transaction  # 👈 Import the class from your file

class TestTransaction(unittest.TestCase):
    
    def test_initialization(self):
        t = Transaction("TX001", 1000.0)
        self.assertEqual(t.number, "TX001")
        self.assertEqual(t.funds, 1000.0)
        self.assertEqual(t.status, "active")

    def test_str_output(self):
        t = Transaction("TX002", 500, "pending")
        expected = "Transaction(TX002, 500, pending)"
        self.assertEqual(str(t), expected)

    def test_repr_output(self):
        t = Transaction("TX003", 750.5, "completed")
        expected = "Transaction(TX003, 750.5, completed)"
        self.assertEqual(repr(t), expected)

if __name__ == "__main__":
    unittest.main()
