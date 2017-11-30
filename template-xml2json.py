# -*- coding: UTF-8 -*-
# For python3 earlier python may garble Japanese text
# Skelton for reading xml file and writing to json file
# First line needs to hold the field names.
# you need to do "pip3 install xmltodict" 

import sys
import os
from io import open

import json
import xmltodict


if len(sys.argv)<2:
	print ("\nusage: "+sys.argv[0]+" <INPUTFILE>.csv")
	print ("       the output will be saved in <INPUTFILE>.json\n")
	sys.exit(1)

fxml = open(str(sys.argv[1]), "r",encoding="utf-8")
fjson =open((str(sys.argv[1]).lower()).replace(".xml",".json"), "w",encoding="utf-8")

xmlsource = fxml.read()

# json.dump(dict,fjson) # use this if you don't care to put linefeed occasionally for readability

# use below if you want to put linefeed once in a while.
dict = xmltodict.parse(xmlsource)
jsontext=json.dumps(dict)
jsontext=jsontext.replace("}, {","},\n{")
fjson.write(jsontext)


	

