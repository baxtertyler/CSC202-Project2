# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3.5 5 +"), 8.5)
        self.assertAlmostEqual(postfix_eval("3 1 -"), 2)
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("3 5 <<"), 96)
        self.assertAlmostEqual(postfix_eval("3 5 >>"), 0)
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)
        self.assertAlmostEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)
        self.assertAlmostEqual(postfix_eval(" 5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("4 -")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("4 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("4 /")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("4 **")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("4 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
        try:
            postfix_eval("4 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("3 3 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("3 3 / 1 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")

    def test_postfix_eval_07(self):
        with self.assertRaises(ValueError):
            postfix_eval("1 0 /")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("6.5 + 3"), "6.5 3 +")
        self.assertEqual(infix_to_postfix("6.5"), "6.5")
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6 * 3"), "6 3 *")
        self.assertEqual(infix_to_postfix("6 / 3"), "6 3 /")
        self.assertEqual(infix_to_postfix("6 ** 3"), "6 3 **")
        self.assertEqual(infix_to_postfix("6 << 3"), "6 3 <<")
        self.assertEqual(infix_to_postfix("6 >> 3"), "6 3 >>")

        self.assertEqual(infix_to_postfix("6 << 3 >> 1"), "6 3 << 1 >>")
        self.assertEqual(infix_to_postfix("6 ** 3 << 1"), "6 3 1 << **")
        self.assertEqual(infix_to_postfix("2 << 6 ** 3 << 1"), "2 6 << 3 1 << **")
        self.assertEqual(infix_to_postfix("6 * 3 / 1"), "6 3 * 1 /")
        self.assertEqual(infix_to_postfix("6 - 3 + 1"), "6 3 - 1 +")

        self.assertEqual(infix_to_postfix("6 << 3 >> 1 << 2 >> 7"), "6 3 << 1 >> 2 << 7 >>")
        self.assertEqual(infix_to_postfix("6 / 3 * 1 / 2 * 7"), "6 3 / 1 * 2 / 7 *")
        self.assertEqual(infix_to_postfix("6 - 3 + 1 - 2 + 7"), "6 3 - 1 + 2 - 7 +")

        self.assertEqual(infix_to_postfix("5 + 5 - 2 / 2 ** 3"), "5 5 + 2 2 3 ** / -")

        self.assertEqual(infix_to_postfix("6 * 3 - 1"), "6 3 * 1 -")
        self.assertEqual(infix_to_postfix("6 * ( 3 - 1 )"), "6 3 1 - *")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3.5 / 2 1 - / 4 5 6"), "3.5 2 1 / - 4 5 / 6 - *")


if __name__ == "__main__":
    unittest.main()
