
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


def cal4():
	ids_file = open("./ids.txt", 'r')
	mjs_file = open("./mjs.txt", 'r')
	mat_file = open("./mat.txt", 'r')
	std_file = open("./mjs_standards.txt", 'r')
	
	ids = []
	mjs = []
	mat = []
	std = []
	for chunk in iter(lambda: ids_file.readline(), ''):
		ids.append(chunk.replace("\n",""))
	for chunk in iter(lambda: mjs_file.readline(), ''):
		mjs.append(chunk.replace("\n","").replace("u","").replace("\'", ""))
	for chunk in iter(lambda: mat_file.readline(), ''):
		mat.append( [round(float(f),5) for f in chunk.replace("\n","").split(",")] )
	for chunk in iter(lambda: std_file.readline(), ''):
		std.append( chunk.replace("\n","") )
	print "read"
	print std
	out = open("./majorConnec.txt", 'w')

	for i in range(0, len(std)):
		for j in range(i+1, len(std)):
			current = [std[i], std[j]]
			data = []
			print ",".join(current)
			for x in range(0, len(ids)):
				for y in range(x+1, len(ids)):
					if (str(mjs[x]) in current) and (str(mjs[y]) in current) and (str(mjs[x]) != str(mjs[y])):
						data.append(mat[x][y])

			print repr( sum(data) ) + "," + repr( len(data) )
			out.write( ",".join(current) + "," + repr( sum(data) ) + "," + repr( len(data) ) +"\n") 


		#out.write(repr(k) + "," + ",".join(str(x) for x in ratios) + "\n")
		#out2.write(repr(k) + "," + ",".join(str(x) for x in coeffs) + "\n")


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
	cal4()

if __name__ == "__main__":
    main()		