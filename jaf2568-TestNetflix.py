#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import sqre_diff, netflix_print,actual_rate, computeRmse, getCatch, customers_Rating, movies_Rating, customers_ID, getAveRatingCostumer, predict, netflix_solve

# -----------
# TestCollatz
# -----------

class TestNetflix (unittest.TestCase) :
    # ---------
    # sqre_diff
    # ---------

    def test_sqre_diff_1 (self) :
        v = sqre_diff (0, 0)
        self.assert_(v == 0)

    def test_sqre_diff_2 (self) :
        v = sqre_diff (2, 1)
        self.assert_(v == 1)

    def test_sqre_diff_3 (self) :
        v = sqre_diff (5, 3)
        self.assert_(v == 4)
    
    # -------------
    # netflix_print
    # -------------
    def test_netflix_print_1 (self) :
        w = StringIO.StringIO()
        netflix_print(w, "1")
        self.assert_(w.getvalue() == "1\n")
    
    def test_netflix_print_2 (self) :
        w = StringIO.StringIO()
        netflix_print(w, 4)
        self.assert_(w.getvalue() == "4\n")

    def test_netflix_print_3 (self) :
        w = StringIO.StringIO()
        netflix_print(w, "123412:")
        self.assert_(w.getvalue() == "123412:\n")

    # -----------
    # actual_rate
    # -----------
    def test_actual_rate_1 (self) :
        r = StringIO.StringIO("1:\n3")
        b = actual_rate(r)
        self.assert_(b == [3])

    def test_actual_rate_2 (self) :
        r = StringIO.StringIO("1:\n3\n2:\n3.4\n3:\n3.4\n4:\n4.3")
        b = actual_rate(r)
        self.assert_(b == [3,3.4,3.4,4.3])


    def test_actual_rate_3 (self) :
        r = StringIO.StringIO("1:\n3\n2:\n3.4")
        b = actual_rate(r)
        self.assert_(b == [3,3.4])

    # -----------
    # computeRsme
    # -----------
    def test_computeRsme_1 (self) :
        r = StringIO.StringIO("1:\n1")
        b = computeRmse(r,[1])
        self.assert_(b==0.0)

    def test_computeRsme_2 (self) :
        r = StringIO.StringIO("1:\n1")
        b = computeRmse(r,[2])
        self.assert_(b==1.0)
    
    def test_computeRsme_3 (self) :
        r = StringIO.StringIO("1:\n2\n2:\n1\n3:\n4")
        b = computeRmse(r,[1,2,3])
        self.assert_(b== 1.0)
     
    # --------
    # getCatch
    # --------
    def test_getCatch_1 (self) :
        r = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5\n5 5")
        getCatch(r)
        mRating = movies_Rating 
        cRating = customers_Rating
        cId = customers_ID
        self.assert_(cId[0] == '1')
        self.assert_(cId[1] == '2')
        self.assert_(cId[2] == '3')
        self.assert_(cId[3] == '5')
        self.assert_(cId[4] == '4')
        self.assert_(cRating[0] == '3.4')
        self.assert_(cRating[1] == '4.4')
        self.assert_(cRating[2] == '2.4')
        self.assert_(cRating[3] == '1.2')
        self.assert_(cRating[4] == '2.2')
        self.assert_(mRating[1] == '3.5')
        self.assert_(mRating[2] == '2.5')
        self.assert_(mRating[5] == '5')  

    # --------------------
    # getAveRatingCostumer
    # --------------------
    def test_getAveRatingCostumer_1 (self) :
        r = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(r)
        b = getAveRatingCostumer('2')
        self.assert_(b == 4.4)

    def test_getAveRatingCostumer_2 (self) :
        r = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(r)
        b = getAveRatingCostumer('1')
        self.assert_(b == 3.4)

    def test_getAveRatingCostumer_3 (self) :
        r = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(r)
        b = getAveRatingCostumer('6')
        self.assert_(b == 0.0)

    # -------
    # predict
    # -------
    def test_predict_1 (self) :
        r = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(r)
        b = predict('2', '1')
        self.assert_(b == 3.95)

    def test_predict_2 (self) :
        r = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(r)
        b = predict('1', '1')
        self.assert_(b == 3.45)

    def test_predict_3 (self) :
        r = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5\n5 5")
        getCatch(r)
        b = predict('5', '5')
        self.assert_(b == 3.1)

    # -------------
    # netflix_solve
    # -------------
    def test_netflix_solve_1 (self) :
        re = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(re)
        r = StringIO.StringIO("1:\n1\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "1:\n3.45\n")

    def test_netflix_solve_2 (self) :
        re = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(re)
        r = StringIO.StringIO("1:\n1\n2\n5\n2:\n3\n2")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "1:\n3.45\n3.95\n2.35\n2:\n2.45\n3.45\n")

    def test_netflix_solve_3 (self) :
        re = StringIO.StringIO("COSTUMERS_RATE\n1 3.4\n2 4.4\n3 2.4\n5 1.2\n4 2.2\nMOVIE_RATES\n2 2.5\n1 3.5")
        getCatch(re)
        r = StringIO.StringIO("1:\n2:")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "1:\n2:\n")


# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
