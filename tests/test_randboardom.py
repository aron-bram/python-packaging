"""Run this filefrom root folder."""

import os, sys

# __init__ doesn't seem to work
sys.path.insert(0, os.path.abspath("."))
print(sys.path)

from src.ranboardom.script import board 

b = board(3, 3)

def test_matrix_size():
    assert b.size == 9

def test_matrix_rows():
    assert b.shape[0] == 3

def test_matrix_cols():
    assert b.shape[1] == 3
