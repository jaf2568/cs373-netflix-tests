#!/usr/bin/env python

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""


# --------
# imports 
# --------

import unittest
import StringIO
from Netflix import netflix_readCache, netflix_eval, netflix_predict, netflix_print, netflix_solve 
# ------------
# TestNetflix
# ------------
class TestNetflix (unittest.TestCase):

    # ------------------
    # netflix_readMovies
    # ------------------
    def test_netflix_readCache_1(self):
        f = StringIO.StringIO("1 4.356\n14 1.112\n56 3\n10023 4.56\n")
        m = [0] * 10030
        netflix_readCache(f, m)
        self.assert_(m[1] == 4.356)
        self.assert_(m[14] == 1.112)
        self.assert_(m[56] == 3)
        self.assert_(m[10023] == 4.56)
        self.assert_(m[10024] == 0)

    def test_netflix_readCache_2(self):
        f = StringIO.StringIO("")
        m = [0] * 10000
        netflix_readCache(f, m)
        for mov in m:
            self.assert_(mov == 0)

    def test_netflix_readCache_3(self):
        f = StringIO.StringIO("50 2.1\n6075 5\n963 3.9\n")
        m = [0] * 6080
        netflix_readCache(f, m)
        self.assert_(m[50] == 2.1)
        self.assert_(m[6075] == 5)
        self.assert_(m[963] == 3.9)

    def test_netflix_readCache_4(self):
        f = StringIO.StringIO("1 5\n10 4.8929\n1000 2.678\n1000000 3.999")
        c = [0] * 1000010
        netflix_readCache(f, c)
        self.assert_(c[1] == 5)
        self.assert_(c[10] == 4.8929)
        self.assert_(c[1000] == 2.678)
        self.assert_(c[1000000] == 3.999)

    def test_netflix_readCache_5(self):
        f = StringIO.StringIO("235 4.23\n15 1.111\n9000 3.06")
        c = [0] * 10000
        netflix_readCache(f, c)
        self.assert_(c[235] == 4.23)
        self.assert_(c[15] == 1.111)
        self.assert_(c[9000] == 3.06)

    # ------------
    # netflix_eval
    # ------------
    def test_netflix_eval_1(self):
        f = StringIO.StringIO("1:\n1\n2\n2:\n1\n2\n")
        m = [0, 2.5, 1.9]
        c = [0, 4.8, 3.3]
        ans = {}
        b = netflix_eval(f, m, c, ans, [])
        self.assert_(b == False)
        for key in ans:
            for i in range(len(ans[key])):
                ans[key][i] = "%.2f" % ans[key][i]
        self.assert_(ans[1] == ["4.22", "2.90"])
        self.assert_(ans[2] == ["4.07", "2.25"])

    def test_netflix_eval_2(self):
        f = StringIO.StringIO("")
        m = [0]
        c = [0]
        ans = {}
        b = netflix_eval(f, m, c, ans, [])
        self.assert_(b == False)
        self.assert_(ans == {})

    def test_netflix_eval_3(self):
        f = StringIO.StringIO("1:\n1\n2\n3\n3:\n3\n2\n4:\n2\n3\n1\n")
        m = [0, 4.5, 3.3, 5, 2.6]
        c = [0, 3, 4.99, 2.78]
        ans = {}
        b = netflix_eval(f, m, c, ans, [])
        self.assert_(b == False)
        for key in ans:
            for i in range(len(ans[key])):
                ans[key][i] = "%.2f" % ans[key][i]
        self.assert_(ans[1] == ["4.12", "4.87", "4.07"])
        self.assert_(ans[3] == ["4.45", "4.99"])
        self.assert_(ans[4] == ["4.39", "2.69", "2.80"])

    # ---------------
    # netflix_predict
    # ---------------
    def test_netflix_predict_1(self):
        m = 5.0
        c = 1.0
        ans = netflix_predict(m, c)
        self.assert_(ans == 2.0)

    def test_netflix_predict_2(self):
        m = 1.0
        c = 3.0
        ans = netflix_predict(m, c)
        self.assert_(ans == 1.50)

    def test_netflix_predict_3(self):
        m = 3.0
        c = 3.0
        ans = netflix_predict(m, c)
        self.assert_(ans == 3)
              
    # -------------
    # netflix_print
    # -------------
    def test_netflix_print_1(self):
        w = StringIO.StringIO()
        ans = {1: [1,2,3],
               2: [4,5],
               6: [2] }
        netflix_print(w, ans, [1,2,6])
        self.assert_(w.getvalue() == "1:\n1\n2\n3\n2:\n4\n5\n6:\n2\n")

    def test_netflix_print_2(self):
        w = StringIO.StringIO()
        ans = {}
        netflix_print(w, ans, [])
        self.assert_(w.getvalue() == "")

    def test_netflix_print_3(self):
        w = StringIO.StringIO()
        ans = {1: [1,2,3],
               2: [4,5],
               6: [2] }
        netflix_print(w, ans, [6,2,1])
        self.assert_(w.getvalue() == "6:\n2\n2:\n4\n5\n1:\n1\n2\n3\n")

    # -------------
    # netflix_solve
    # -------------
    def test_netflix_solve_1(self):
        r = StringIO.StringIO("1:\n30878\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "1:\n3.69158015625\n")

    def test_netflix_solve_2(self):
        r = StringIO.StringIO("10:\n1531863\n1952305\n10000:\n200206\n523108\n")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "10:\n3.16766407736\n3.29503177546\n10000:\n4.03026889535\n3.92066810055\n")
    
    def test_netflix_solve_3(self):
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        netflix_solve(r, w)
        self.assert_(w.getvalue() == "")

# -----
# main
# -----

print "TestNetflix.py"
unittest.main()
print "Done."
