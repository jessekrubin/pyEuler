#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

cash = {}

def divList(x):
    leeest = []
    for i in range(1, int(x/2)+1 ):
        if x % i == 0:
            leeest.append(i)
    return leeest

def numDivs(x):
    n = 0
    for i in range(int((1 + x)/2),0, -1):
        # print(i)
        if x % i == 0:
            n += 1
    return n


curTriangleNum = 1
maxDivs = 1
notDoneYet = True
# for i in range(10):
i = 1
while(notDoneYet):
    i += 1
    curTriangleNum = curTriangleNum + i
    if 
    listODivs = divList(curTriangleNum)
    # lengthList = numDivs(curTriangleNum)
    

    
    if (maxDivs < lengthList):
        maxDivs = lengthList
        print("\n***")
        print("NEW MAX")
        print("index: {}".format(i))
        print("cur: {}".format(curTriangleNum))
        # print("divs: {}".format((listODivs)))
        # print("lenlist: {}".format(len(listODivs)))
        print("# div: {}".format(lengthList))
        
        if(maxDivs > 500):
            notDoneYet = False

    # if (numbDivs % 100 == 0):
    #     print("\n***")
    #     print("index: {}".format(i))
    #     print("cur: {}".format(curTriangleNum))
    #     print("divs: {}".format(numbDivs))
    #     print("# div: {}".format(numbDivs))
