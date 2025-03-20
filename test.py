import unittest
from tkinter import Tk, StringVar
from app import on_click 

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.entry_var = StringVar()

    def test_addition(self):
        self.entry_var.set("2+3")
        on_click("=", self.entry_var)
        self.assertEqual(self.entry_var.get(), "5")

    def test_subtraction(self):
        self.entry_var.set("10-4")
        on_click("=", self.entry_var)
        self.assertEqual(self.entry_var.get(), "6")

    def test_multiplication(self):
        self.entry_var.set("6*3")
        on_click("=", self.entry_var)
        self.assertEqual(self.entry_var.get(), "18")

    def test_division(self):
        self.entry_var.set("12/4")
        on_click("=", self.entry_var)
        self.assertEqual(self.entry_var.get(), "3.0")

    def test_clear(self):
        self.entry_var.set("123")
        on_click("C", self.entry_var)
        self.assertEqual(self.entry_var.get(), "")

if __name__ == "__main__":
    unittest.main()
