# coding=utf-8

from lib.decorations import tictoc


def test_ftime_seconds():
    ti = 1.2345
    tf = 5.4321
    assert tictoc.ftime(ti, tf) == '4.198 s'


def test_ftime_milliseconds():
    ti = 1.2345*(10**(-3))
    tf = 5.4321*(10**(-3))
    assert tictoc.ftime(ti, tf) == '4.198 ms'


def test_ftime_microseconds():
    ti = 1.2345*(10**(-6))
    tf = 5.4321*(10**(-6))
    assert tictoc.ftime(ti, tf) == '4.198 μs'


def test_ftime_nanoseconds():
    ti = 1.2345*(10**(-9))
    tf = 5.4321*(10**(-9))
    assert tictoc.ftime(ti, tf) == '4.198 ns'
