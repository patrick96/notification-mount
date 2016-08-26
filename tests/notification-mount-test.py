#!/usr/bin/env python2

import unittest

class FooTests(unittest.TestCase):

    def testFoo(self):
        self.assertTrue(True)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
