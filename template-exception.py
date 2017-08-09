# -*- coding: UTF-8 -*-
import sys

def test(first,second):
	print ("try %d divided by %d = " % (first,second),end='')
	try:
		result = int(first)/int(second)
		print(result)
	except Exception as e:
		print("!!! Exception : ",e)
		sys.exit(1)		
	return


test(10,2)
test(5,0)
test(20,5)
