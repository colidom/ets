#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mymodule

class TestMyModule(unittest.TestCase):
    
    def test_get_prime_numbers(self):
        self.assertEqual(mymodule.get_prime_numbers(10), [2, 3, 5, 7])
    
    def test_is_prime(self):
        self.assertTrue(mymodule.is_prime(5))
        self.assertFalse(mymodule.is_prime(6))
    
    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 7), 12)
        with self.assertRaises(TypeError):
            mymodule.sum(5, "Python")

if __name__ == "__main__":
    unittest.main()
