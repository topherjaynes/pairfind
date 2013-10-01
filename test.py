#!/usr/bin/env python
# encoding: utf-8
"""
test.py

Created by Christopher Jaynes on 2013-09-30.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import unittest
import sys
from io import StringIO
from solution import print_dictionary_of_artist, find_unique_pairings


class TestPairsSolution(unittest.TestCase):
    def setUp(self):
        #self.held, sys.stdout = sys.stdout, StringIO()
        self.tdictionary={"Jay-z, Taylor Swift ": 2, "Garth Brooks,Mackelmore":1}
        self.pairs_list=["Jay-z","Chris Jaynes", "The Beatles"]
    def tearDown(self):
        pass
        #self.output.close()
        #sys.stdout = self.saved_stdout
    def test_DictionaryPrint(self):
        pass
        # poor form as tested with return, captuing stfout easier in python3

    def test_TestSort(self):
        assert find_unique_pairings(self.pairs_list,2) == [('Jay-z', 'Chris Jaynes'), ('Jay-z', 'The Beatles'), ('Chris Jaynes', 'The Beatles')]
    
    
if __name__ == '__main__':
        unittest.main()