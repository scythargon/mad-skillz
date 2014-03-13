#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

file_ind = 0
byte_ind = 0
f2 = 0
with open(os.argv[1], "rb") as f:
    byte = f.read(1)
    while byte != "":
        if not byte_ind % 1000000:
        	if f2:
        		f2.close()
        	f2 = open(os.argv[1]+'_'+str(file_ind), "rb")
        	file_ind += 1
        byte_ind += 1
    		f2.write(b)
        	byte = f.read(1)
	f.close()