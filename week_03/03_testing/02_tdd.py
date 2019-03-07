'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''

import unittest
import code_for_02_tdd


class TestOpener(unittest.TestCase):

    def setUp(self):
        self.file = "/home/robert-jan/Documents/CodingNomads/python-onsite/week_03/03_testing/some_text"
        with open(self.file, "r") as fin:
            self.content = fin.read()[:100]

    #Failed on run 1, succes on run 2
    #Open a file and get the first 100 characters.
    def test_if_it_returns_the_first_100_chars(self):
        self.assertEqual(code_for_02_tdd.opener(self.file), self.content)


#Feels a bit stupid. Because in order to get to check whether the code does what I want, i'm also coding, gues that's
#not pure TDD.
