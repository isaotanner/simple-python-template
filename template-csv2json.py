# -*- coding: UTF-8 -*-
# For python3 earlier python may garble Japanese text
# Skelton for reading csv file and writing to json file
# First line needs to hold the field names.

import sys
import os
import csv
import json
from io import open

if len(sys.argv)<2:
	print ("\nusage: "+sys.argv[0]+" <INPUTFILE>.csv")
	print ("       the output will be saved in <INPUTFILE>.json\n")
	sys.exit(1)

fcsv = open(str(sys.argv[1]), "r",encoding="utf-8")
fjson =open(str(sys.argv[1]).replace(".csv",".json"), "w",encoding="utf-8")

fieldname = fcsv.readline()
fieldnames = fieldname.split(",")

csvlists= csv.DictReader(fcsv,fieldnames)

count=0
for line in csvlists:
	if not (count%1000):		
		print("\n[%6d]" % (count),end='')
	else:
		if not (count%10): 
			sys.stdout.write('.')
			sys.stdout.flush()			
	count+=1
	json.dump(line,fjson)
	fjson.write("\n")
	
print("\n[%6d]" % count)

	

