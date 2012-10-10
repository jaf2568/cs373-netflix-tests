#!/usr/bin/env python
"""
To run the program
    % python RunNetflix.py < RunNetflix.in > RunNetflix.out
    % chmod ugo+x RunCollatz.py
    % RunNetflix.py < RunNetflix.in > RunNetflix.out

To document the program
    % pydoc -w Netflix
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
