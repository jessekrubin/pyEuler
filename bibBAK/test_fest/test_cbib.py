# coding=utf-8
from __future__ import division, print_function
import pyximport

pyximport.install()
# import pupy.cy_maths
from bib.amazon_prime import prime_gen as py_prime_gen
from bib.cy_amazon_prime import prime_gen as cy_prime_gen
from bib.decorations import tictoc




def primegens():
    """
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _py_prime_gen
        args: (1000,)
        time: 182.986 μs
        runs: 10
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _cy_prime_gen
        args: (1000,)
        time: 137.520 μs
        runs: 10
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _py_prime_gen
        args: (10000,)
        time: 2.062 ms
        runs: 10
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _cy_prime_gen
        args: (10000,)
        time: 1.747 ms
        runs: 10
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _py_prime_gen
        args: (100000,)
        time: 21.660 ms
        runs: 10
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _cy_prime_gen
        args: (100000,)
        time: 17.253 ms
        runs: 10
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _py_prime_gen
        args: (1000000,)
        time: 242.866 ms
        runs: 10
    __TICTOC__
        file: /Users/jesserubin/git/pyEuler/test_cybib.py
        funk: _cy_prime_gen
        args: (1000000,)
        time: 183.877 ms
        runs: 10
        @tictoc(runs=10)
        def _py_prime_gen(n):
            return list(py_prime_gen(n))

        @tictoc(runs=10)
    """

    @tictoc()
    def _py_prime_gen(n):
        return list(py_prime_gen(n))

    @tictoc()
    def _cy_prime_gen(n):
        return list(cy_prime_gen(n))

    for exp in range(4, 7):
        n = 10 ** exp
        py_primes = _py_prime_gen(n)
        cy_primes = _cy_prime_gen(n)


if __name__ == '__main__':
    primegens()  # test_n_time_reverse()
