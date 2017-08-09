# -*- coding: UTF-8 -*-
# For python3 earlier python may garble Japanese text
# Skelton for reading lines from file and processing line by line
import sys
import os
import json
from io import open

def doprocess(line):

	f.write('[%5d] %s\n' % (count, line.strip()))

	return

if len(sys.argv)<2:
	print ("\nusage: "+sys.argv[0]+" <INPUTFILE>")
	print ("       the output will be saved in out_<INPUTFILE>\n")
	sys.exit(1)

f = open(str(sys.argv[1]), "r",encoding="utf-8")
lines = f.readlines()
f.close()
count=0
f = open("out-"+str(sys.argv[1]), "w",encoding="utf-8")

for l in lines:
	if not (count%1000):		
		print("\n[%6d]" % (count),end='')
	else:
		if not (count%10): 
			sys.stdout.write('.')
			sys.stdout.flush()
			
	count+=1
	doprocess(l)
	
	
print("\n[%6d]" % count)

	

