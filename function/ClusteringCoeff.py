
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


def cal3_compo(option):
	srt = option[0]
	end = option[1]

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

	out = open("./" + repr(srt) + "component.txt", 'w')
	out2 = open("./" + repr(srt) + "clusteringCoeffs.txt", 'w')

	## Control Lambda
	for k in [x / 10.0 for x in range(srt, end, 10)]: ## 0, 505
		print k
		G = networkx.Graph()
		G.add_nodes_from([0, len(ids)])
		for i in range(0, len(ids)):
			for j in range(i+1, len(ids)):
				if mat[i][j] >= k/100:
					G.add_edge(i,j)

		num = min(networkx.number_connected_components(G), 4)
		counts = [0]*4
		ratios = [0]*4
		for q in range(0, num):
			counts[q] = [len(c) for c in sorted(networkx.connected_components(G), key=len, reverse=True)][q]
			ratios[q] = float(counts[q]) / len(ids)

		largest = list([c for c in sorted(networkx.connected_components(G), key=len, reverse=True)][0])

		Number_Triangle = 0
		Number_Triads   = 0		
		AM_N = 0
		AM_D = 0

		GM_N = 0
		GM_D = 0

		MX_N = 0
		MX_D = 0

		MN_N = 0
		MN_D = 0

		lbd = k/100
		length = len(largest)
		for ind_a in range(0, length):
			print ind_a
			for ind_b in range(ind_a+1, length):
				for ind_c in range(ind_b+1, length):
					## Closed Trangle Case
					w1 = mat[largest[ind_a]][largest[ind_b]]
					w2 = mat[largest[ind_b]][largest[ind_c]]
					w3 = mat[largest[ind_c]][largest[ind_a]]
					if w1 >= lbd and w2 >= lbd and w3 >= lbd:
						AM_N += (w1+w2+w3)
						AM_D += (w1+w2+w3)
						GM_N += math.sqrt(w1*w2) + math.sqrt(w2*w3) + math.sqrt(w3*w1)
						GM_D += math.sqrt(w1*w2) + math.sqrt(w2*w3) + math.sqrt(w3*w1)
						MX_N += max(w1,w2) + max(w2,w3) + max(w3,w1)
						MX_D += max(w1,w2) + max(w2,w3) + max(w3,w1)
						MN_N += min(w1,w2) + min(w2,w3) + min(w3,w1)
						MN_D += min(w1,w2) + min(w2,w3) + min(w3,w1)
						Number_Triangle += 1
						Number_Triads   += 3		

					## AB not connected	
					elif w1 < lbd and w2 >= lbd and w3 >= lbd:
						AM_D += (w2+w3)/2
						GM_D += math.sqrt(w2*w3)
						MX_D += max(w2,w3)
						MN_D += min(w2,w3)
						Number_Triads   += 1	

					## BC not connected
					elif w1 >= lbd and w2 < lbd and w3 >= lbd:
						AM_D += (w1+w3)/2
						GM_D += math.sqrt(w1*w3)
						MX_D += max(w1,w3)
						MN_D += min(w1,w3)
						Number_Triads   += 1	

					## CA not connected	
					elif w1 >= lbd and w2 >= lbd and w3 < lbd:
						AM_D += (w1+w2)/2
						GM_D += math.sqrt(w1*w2)
						MX_D += max(w1,w2)
						MN_D += min(w1,w2)
						Number_Triads   += 1	

		coeffs = [AM_N/AM_D, GM_N/GM_D, MX_N/MX_D, MN_N / MN_D, Number_Triangle, Number_Triads]

		print k, " ::", ",".join(str(x) for x in ratios)
		del G
		out.write(repr(k) + "," + ",".join(str(x) for x in ratios) + "\n")
		out2.write(repr(k) + "," + ",".join(str(x) for x in coeffs) + "\n")


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
	start = 0
	end = 0
	if len(args) > 0:
		start		= int(args[0])
	if len(args) > 1:
		end     	= int(args[1])
	cal3_compo([start, end])

if __name__ == "__main__":
    main()		