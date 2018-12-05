#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:51:36 2018

@author: zouhao

Function:
    Array2D class;
"""
import random
from myarray import Array

class Array2D:
    def __init__(self, numRows, numCols):
        self.theRows=Array(numRows)
        
        for i in range(numRows):
            self.theRows[i]=Array(numCols)
            
    def clone(self):
        newa2d=Array2D(self.numRows(), self.numCols())
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                newa2d.theRows[row][col]=self.theRows[row][col]
        return newa2d
    
    def print(self):
        for i in range(self.numRows()):
            self.theRows[i].print()
            print()
            
    def numRows(self):
        return len(self.theRows)
    
    def numCols(self):
        return len(self.theRows[0])
    
    def clear(self, value):
        for row in range(self.numRows()):
            self.theRows[row].clear(value)
            
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple)==2, 'Invalid number of array subscripts.'
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and \
               col >= 0 and col < self.numCols(), \
               "Array subscript out of range."
        the1dArray = self.theRows[row]
        return the1dArray[col]
    
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple)==2, 'Invalid number of array subscripts.'
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and \
               col >= 0 and col < self.numCols(), \
               'Array subscript out of range.'
        the1dArray = self.theRows[row]
        the1dArray[col] = value
        
def main():
    a = Array2D(10, 5)
    for r in range(a.numRows()):
        for c in range(a.numCols()):
            a[r, c] = random.random()
            
    a.print()
    
if __name__=='__main__':
    main()
