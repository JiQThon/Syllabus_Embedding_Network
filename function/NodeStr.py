
#-*- coding: utf-8 -*-

## Common Modules
import sys
import operator
import time
import getopt

## Regex Modules
import re
## File I/O Modules
import csv
from string import digits
import copy
import json
import math
import networkx
## Encoding UTF-8 Setting
reload(sys)
sys.setdefaultencoding('UTF8')


def cal5_nodeStr():
	ids_file = open("./ids.txt", 'r')
	mjs_file = open("./mjs.txt", 'r')
	mat_file = open("./mat.txt", 'r')
	
	ids = []
	mjs = []
	mat = []
	for chunk in iter(lambda: ids_file.readline(), ''):
		ids.append(chunk.replace("\n",""))
	for chunk in iter(lambda: mjs_file.readline(), ''):
		mjs.append(chunk.replace("\n",""))
	for chunk in iter(lambda: mat_file.readline(), ''):
		mat.append( [round(float(f),5) for f in chunk.replace("\n","").split(",")] )
	print "read"


	## Control Lambda
	for k in [x / 10.0 for x in range(0, 505, 50)]: ## 0, 505
		out = open("./nodeStrs"+str(int(k))+".txt", 'w')
		for i in range(0, len(mat)):
			for j in range(0, len(mat)):
				if mat[i][j] < k/100:
					mat[i][j] = 0
		data = []
		for i in range(0, len(mat)):
			data.append(sum(mat[i]) - 1)
		out.write("\n".join(str(x) for x in data) + "\n")


def main(argv=None):
	if argv is None:
		argv = sys.argv
    # parse command line options
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
	except getopt.error, msg:
 		print msg
		print "for help use --help"
		sys.exit(2)

	# process options
	"""
	## give documentation
	for o, a in opts:
	    if o in ("-h", "--help"):
	        print __doc__
	        sys.exit(0)
	"""

	# process arguments
	cal5_nodeStr()

if __name__ == "__main__":
    main()		