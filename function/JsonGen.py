#-*- coding: utf-8 -*-

## Common Modules
import sys
import operator
import time
## Regex Modules
import re
## File I/O Modules
import csv

from string import digits
import copy
import json

## Encoding UTF-8 Setting
reload(sys)
sys.setdefaultencoding('UTF8')

#if False:
if True:
	ids_file = open("./ids.txt", 'r')
	mjs_file = open("./mjs.txt", 'r')
	mat_file = open("./mat.txt", 'r')
	
	ids = []
	mjs = []
	mat = []
	for chunk in iter(lambda: ids_file.readline(), ''):
		ids.append(chunk.replace("\n","").replace("u\'", "").replace("\'",""))
	for chunk in iter(lambda: mjs_file.readline(), ''):
		mjs.append(chunk.replace("\n","").replace("u\'", "").replace("\'",""))
	for chunk in iter(lambda: mat_file.readline(), ''):
		mat.append( [round(float(f),5) for f in chunk.replace("\n","").split(",")] )

	## UI Write

	NodesOverall = ids
	LinksOverall_20 = []
	LinksOverall_25 = []
	LinksOverall_30 = []

	NodesPartA = []
	LinksPart_A_15 = []

	NodesPartB = []
	LinksPart_B_15 = []

	NodesPartC = []
	LinksPart_C_15 = []

	NodesPartD = []
	LinksPart_D_15 = []

	Type_A = ["BIZ", "MAT", "ECO", "IIE"]
	Type_B = ["CSI", "KOR"]
	Type_C = ["CSI", "LIS"]
	Type_D = ["CSI", "LIS", "KOR"]

		## UI. MAT ECO BIZ EEE IIE 15%

	print "start"
	for i in range(0, len(ids)):
		##print mjs[i]
		if mjs[i] in Type_A:
			print "!!!!"
			NodesPartA.append(ids[i])
		if mjs[i] in Type_B:
			NodesPartB.append(ids[i])
		if mjs[i] in Type_C:
			NodesPartC.append(ids[i])
		if mjs[i] in Type_D:
			NodesPartD.append(ids[i])

	print NodesPartC
	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			"""
			if mat[i][j] >= 0.20:
				LinksOverall_20.append( [ids[i], ids[j], float(mat[i][j])] ) 
			if mat[i][j] >= 0.25:
				LinksOverall_25.append( [ids[i], ids[j], float(mat[i][j])] ) 
			if mat[i][j] >= 0.30:
				LinksOverall_30.append( [ids[i], ids[j], float(mat[i][j])] ) 
			"""
			if (mjs[i] in Type_A) and (mjs[j] in Type_A):
				if mat[i][j] >= 0.15:
					LinksPart_A_15.append( [ids[i], ids[j], float(mat[i][j])] ) 
			if (mjs[i] in Type_B) and (mjs[j] in Type_B):
				if mat[i][j] >= 0.15:
					LinksPart_B_15.append( [ids[i], ids[j], float(mat[i][j])] ) 
			if (mjs[i] in Type_C) and (mjs[j] in Type_C):
				if mat[i][j] >= 0.15:
					LinksPart_C_15.append( [ids[i], ids[j], float(mat[i][j])] ) 
			if (mjs[i] in Type_D) and (mjs[j] in Type_D):
				if mat[i][j] >= 0.15:
					LinksPart_D_15.append( [ids[i], ids[j], float(mat[i][j])] ) 

	## UI. MAT ECO BIZ EEE IIE 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_A_15
	json_dic["nodes"] = NodesPartA
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('./data_typeA15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)



	"""
	## UI. KOR SCI 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_B_15
	json_dic["nodes"] = NodesPartB
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('./data_typeB15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. KOR SCI 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_C_15
	json_dic["nodes"] = NodesPartC
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('./data_typeC15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. KOR SCI 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_D_15
	json_dic["nodes"] = NodesPartD
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('./data_typeD15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)
	## UI. Overall Network Analysis 20%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksOverall_20
	json_dic["nodes"] = NodesOverall
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('./data_overall20.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. Overall Network Analysis 25%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksOverall_25
	json_dic["nodes"] = NodesOverall
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('./data_overall25.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. Overall Network Analysis 30%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksOverall_30
	json_dic["nodes"] = NodesOverall
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('./data_overall30.json', 'w') as outfile:
	    json.dump(json_dic, outfile)


	"""

