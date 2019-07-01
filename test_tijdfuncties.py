import unittest
import datetime

import tijdfuncties

class test_lijstnaartekst(unittest.TestCase):

# test lijstnaartekst
    def test_zin(self):
        self.assertEqual(tijdfuncties.lijstnaartekst(["appel","noot","peer","pit"]), "appel, noot, peer en pit")
    def test_zin_woord(self):
        self.assertEqual(tijdfuncties.lijstnaartekst(["appel"]), "appel")
    def test_zin_lege_list(self):
        self.assertEqual(tijdfuncties.lijstnaartekst([""]), "")

# test dateobjectnaartekst
    def test_datumobject(self):
        self.assertEqual(tijdfuncties.dateobjectnaartekst(datetime.datetime(2019, 7, 1)), "maandag 1 juli")
    def test_datumtekst(self):
        self.assertEqual(tijdfuncties.dateobjectnaartekst(datetime.datetime(2019, 7, 1, 12, 30)), "maandag 1 juli")

# test dateobjectnaarstring
    def test_object(self):
        self.assertEqual(tijdfuncties.dateobjectnaarstring(datetime.datetime(2019, 7, 1)), "2019-07-01")
    def test_object_tijd(self):
        self.assertEqual(tijdfuncties.dateobjectnaarstring(datetime.datetime(2019, 7, 1, 12, 30), True), "2019-07-01, 12:30:00")

# test stringnaardateobject
    def test_string(self):
         self.assertEqual(tijdfuncties.stringnaardateobject("2017-12-31"), datetime.datetime(2017, 12, 31, 0, 0))
    def test_foute_datum(self):
         self.assertEqual(tijdfuncties.stringnaardateobject("20-17-123-1"), None)
        
if __name__ == '__main__':
    unittest.main()