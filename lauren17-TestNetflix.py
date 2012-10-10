#!/usr/bin/env python

import StringIO
import unittest
from Netflix import *

class TestNetflix (unittest.TestCase) :



    def test_netflix_read_1(self):
        r = ""      #StringIO.StringIO("")
        a = [0,0,0,False]
        b = a[:]
        error = netflix_read(r,a)
        self.assert_(error == False)
        self.assert_(a == b)

    def test_netflix_read_2(self):
        r = "82793\n"       #StringIO.StringIO("82793\n")
        a = [1,42,0,False]
        b = [1,82793, 0, False]
        success = netflix_read(r,a)
        self.assert_(success == True )
        self.assert_(a == b)

    def test_netflix_read_3(self):
        r = "2:\n"      #StringIO.StringIO("2:\n82793\n")
        a = [1,42,0,False]
        b = [2,42, 0, True]
        success = netflix_read(r,a)
        self.assert_(success == True )
        self.assert_(a == b)

    def test_movie_avg_cache_read_1(self):
        error = False
        try:
            movie_avg_cache_read()
        except:
            error = True
        finally:
            self.assert_(error == False)

    def test_movie_avg_cache_read_2(self):
        error = False
        value = False
        try:
            value = movie_avg_cache_read()
        except:
            error = True
        finally:
            self.assert_(error == False)
            self.assert_(value == True)

 
    def test_movie_avg_cache_read_3(self):
        error = False
        value = False
        
        try:
            value = movie_avg_cache_read()
        except:
            error = True
        finally:
            self.assert_(error == False)
            self.assert_(value == True)
            self.assert_(movieAvgRatings[0] == 0)
 
    def test_user_avg_cache_read_1(self):
        error = False
        try:
            user_avg_cache_read()
        except:
            error = True
        finally:
            self.assert_(error == False)

    def test_user_avg_cache_read_2(self):
        error = False
        value = False
        try:
            value = user_avg_cache_read()
        except:
            error = True
        finally:
            self.assert_(error == False)
            self.assert_(value == True)

 
    def test_user_avg_cache_read_3(self):
        error = False
        value = False
        
        try:
            value = user_avg_cache_read()
        except:
            error = True
        finally:
            self.assert_(error == False)
            self.assert_(value == True)
            self.assert_(userAvgRatings[0] == 0)

    def test_movie_avg_model_1(self):
        movieId = 0
        userId = 0
        res = movie_avg_model([movieId, userId, 0, False])
        self.assert_(res == 0)
         
    def test_movie_avg_model_2(self):
        movieId = 2043
        userId = 0
        res = movie_avg_model([movieId, userId, 0, False])
        self.assert_(res != 0)
        self.assert_(round(res,3) == 3.778)  

    def test_movie_avg_model_3(self):
        movieId = 10851
        userId = 0
        res = movie_avg_model([movieId, userId, 0, False])
        self.assert_(res != 0)
        self.assert_(round(res,3) == 3.854)

    def test_user_avg_model_1(self):
        movieId = 0
        userId = 0
        res = movie_avg_model([movieId, userId, 0, False])
        self.assert_(res == 0)
        
 
    def test_user_avg_model_2(self):
        movieId = 0
        userId = 7
        res = user_avg_model([movieId, userId, 0, False])
        self.assert_(round(res,3) > 0)  


    def test_user_avg_model_3(self):
        movieId = 0
        userId = 2649429
        res = user_avg_model([movieId, userId, 0, False])
        self.assert_(round(res,3) > 0)
 
    def test_netflix_eval_1 (self):
        a = [0,0,0,False]
        b = a[:]
        
        netflix_eval(a)
        self.assert_(a[0] == 0)

    def test_netflix_eval_2 (self):
        a = [2043,7,0,False]
        b = a[:]
        
        netflix_eval(a)
        self.assert_(a[2] >= 1)
        self.assert_(a[2] <= 5)
 

    def test_netflix_eval_3 (self):
        a = [2043,2649429,0,False]
        b = a[:]
        
        netflix_eval(a)
        self.assert_(a[2] >= 1)
        self.assert_(a[2] <= 5)

    def test_netflix_print_1 (self):
        w = StringIO.StringIO()
        ratings = ["1","2","3","4"]

        netflix_print(w,ratings)
        self.assert_(w.getvalue() == "1\n2\n3\n4\n")

    def test_netflix_print_2 (self):
        w = StringIO.StringIO()
        ratings = ["1:","4"]

        netflix_print(w,ratings)
        self.assert_(w.getvalue() == "1:\n4\n")

    def test_netflix_print_3 (self):
        w = StringIO.StringIO()
        ratings = ["1:","","4"]

        netflix_print(w,ratings)
        self.assert_(w.getvalue() == "1:\n4\n")

    def test_predict_1 (self):
        r = "1:"
        a = [0,0,0,False]
        rating = predict(r,a) 

        self.assert_(rating == "1:")

    def test_predict_2 (self):
        r = "2\n"
        a = [0,0,0,False]
        rating = predict(r,a) 

        self.assert_(rating != "0")

    def test_predict_3 (self):
        r = "3\n"
        a = [0,0,0,False]
        rating = predict(r,a) 

        self.assert_(rating != "0")

    def test_netflix_solve_1 (self):
        r = StringIO.StringIO("1:\n")
        w = StringIO.StringIO()
        a = [0,0,0,False]
        netflix_solve(r,w) 

        self.assert_(w.getvalue() == "1:\n")

    def test_netflix_solve_2 (self):
        r = StringIO.StringIO("0:\n2\n")
        w = StringIO.StringIO()
        a = [0,0,0,False]
        netflix_solve(r,w)
        
        self.assert_(w.getvalue() != "0:\n0\n")

    def test_netflix_solve_3 (self):
        r = StringIO.StringIO("\n")
        w = StringIO.StringIO()
        a = [0,0,0,False]
        netflix_solve(r,w)

        self.assert_(w.getvalue() == "\n")





        
print "TestNetflix.py"
movie_avg_cache_read()
user_avg_cache_read()
unittest.main()
print "Done."
