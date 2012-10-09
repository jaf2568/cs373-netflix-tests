#!/usr/bin/env python
"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""
# -------
# imports
# -------
import sys
from Netflix import netflix_solve


# -----
# main
# ----
netflix_solve(sys.stdin, sys.stdout)
