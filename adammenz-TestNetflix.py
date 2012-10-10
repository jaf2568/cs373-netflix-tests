#!/usr/bin/env python

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.py.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import generateRating, getAverageRatingForMovie, getAverageRatingForUser, RMSE, lookUpRatings, netflix_solve

# -----------
# TestNetflix
# -----------

f = open('cache/avgRating.cache')
avgRating = float(f.read())

class TestNetflix (unittest.TestCase) :
    # ----
    # generateRating
    # ----

    def test_generateRating_1 (self) :
        v = generateRating(193940, '7295')
        self.assert_(abs(v - 3.89764802008) < 1e-6)
    
    def test_generateRating_2 (self) :
        v = generateRating(193940, '11173')
	self.assert_(abs(v - 4.52821808617) , 1e-6)
 
    def test_generateRating_3 (self) :
        v = generateRating(193940, '1802')
        self.assert_(abs(v - 4.43568293531), 1e-6)

    # ----
    # getAverageRatingForMovie
    # ----

    def test_getAverageRatingForMovie_1 (self) :
        v = getAverageRatingForMovie('7295')
        self.assert_(v == 2.751937984496124)

    def test_getAverageRatingForMovie_2 (self) :
        v = getAverageRatingForMovie('11173')
        self.assert_(v == 3.3825080505903768)

    def test_getAverageRatingForMovie_3 (self) :
        v = getAverageRatingForMovie('1802')
        self.assert_(v == 3.2899728997289972)

    # ----
    # getAverageRatingForUser
    # ----

    def test_getAverageRatingForUser_1 (self) :
        v = getAverageRatingForUser(1169722)
        self.assert_(v == 4.1851851851851851)

    def test_getAverageRatingForUser_2 (self) :
        v = getAverageRatingForUser(1169723)
        self.assert_(v == 3.1578947368421053)

    def test_getAverageRatingForUser_3 (self) :
        v = getAverageRatingForUser(193940)
        self.assert_(v == 4.75)

    # ----
    # RMSE
    # ----

    def test_RMSE_1 (self) :
        errors = [.4, .6, .8, -.3]
        v = RMSE(errors)
        self.assert_(v - 0.5590169943749475 < 1e-6)

    def test_RMSE_2 (self) :
        errors = [.1, .1, .1, .3]
        v = RMSE(errors)
        self.assert_(v - 0.17320508075688773 < 1e-6)

    def test_RMSE_3 (self) :
        errors = [.2, .4, .6]
        v = RMSE(errors)
        self.assert_(v - 0.432049 < 1e-6)

    # ----
    # lookUpRatings
    # ----

    def test_lookup_1 (self) :
        v = lookUpRatings(5320, 1264176)
        self.assert_(v == 3)

    def test_lookup_2 (self) :
        v = lookUpRatings(2769, 1916745)
        self.assert_(v == 4)

    def test_lookup_3 (self) :
        v = lookUpRatings(3427, 2523090)
        self.assert_(v == 5)

    # ----
    # solve
    # ----
  
    def test_solve_1 (self):
      r = StringIO.StringIO("1:\n30878\n14756\n1000:\n98259\n")
      w = StringIO.StringIO()
      netflix_solve(r, w)
      self.assert_(w.getvalue() == "1:\n3.77887034808\n3.7891665353\n1000:\n3.43667731865\n")
    
    def test_solve_2 (self):
      r = StringIO.StringIO("10:\n1952305\n1001:\n67976\n10009:\n701514\n")
      w = StringIO.StringIO()
      netflix_solve(r, w)
      self.assert_(w.getvalue() == "10:\n2.98577358649\n1001:\n3.43706266681\n10009:\n2.61416192075\n")

    def test_solve_3 (self):
      r = StringIO.StringIO("10034:\n2107088\n69088\n10035:\n1651047\n")
      w = StringIO.StringIO()
      netflix_solve(r, w)
      self.assert_(w.getvalue() == "10034:\n1.71205495192\n2.40949449673\n10035:\n2.69705066121\n")

# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
