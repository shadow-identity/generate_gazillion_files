#!/bin/python
# -*- coding: utf-8 -*-
 
import os
import time
 
directory = '/home/nedr/mount/files/'
# Creates level0 * level1 files
level0 = 200
level1 = 10000

 
def number_format(num, places=0):
 
    places = max(0, places)
    tmp = "%.*f" % (places, num)
    point = tmp.find(".")
    integer = (point == -1) and tmp or tmp[:point]
    decimal = (point != -1) and tmp[point:] or ""
 
    count = commas = 0
    formatted = []
    for i in range(len(integer) - 1, 0, -1):
        count += 1
        formatted.append(integer[i])
        if count % 3 == 0:
            formatted.append(" ")
    formatted.append(integer[0])
    integer = "".join(formatted[::-1])
    return integer+decimal


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
 
    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)
 
if not os.path.exists(directory):
    os.makedirs(directory)
 
print 'making %s files, ~ %s mb' % (number_format(level0 * level1), level0 * level1 / 1000)
 
for j in xrange(level0):
    with Profiler() as p:
        for i in xrange(level1):
            with open(directory + str(j) + str(i), 'wb') as fout:
                fout.write(os.urandom(1024))
    print '-------------------------%s files written' % ((j + 1) * (i + 1))
 
print 'done. %s files, ~ %s mb' % (number_format(level0 * level1), level0 * level1 / 1000)