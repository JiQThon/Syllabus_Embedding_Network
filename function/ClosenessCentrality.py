
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
import math

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
		ids.append(chunk.replace("\n",""))
	for chunk in iter(lambda: mjs_file.readline(), ''):
		mjs.append(chunk.replace("\n",""))
	for chunk in iter(lambda: mat_file.readline(), ''):
		mat.append( [round(float(f),5) for f in chunk.replace("\n","").split(",")] )


	## 1. Calculate Node Strength ( using v )
	# The sum of weights attached to ties belonging to a node (Barrat et al., 2004)
	"""
	node_strength = [0]*len(ids)
	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			if i != j:
				node_strength[i] += mat[i][j]
	node_strength_output = open("./node_strength.txt", 'w')
	for i in range(0, len(node_strength)):
		node_strength_output.write(ids[i] + "," + mjs[i] + "," + repr(node_strength[i]) + "\n")
	print "strength finished"
	node_strength_output.close()
	"""
	##
	dmat = [[0 for _ in range(len(ids))] for _ in range(len(ids))]
	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			if i == j:
				dmat[i][j] == 0
			elif mat[i][j] < 0.00001:
				dmat[i][j] = float("inf")
			else:
				dmat[i][j] = round(1/math.sqrt(mat[i][j]),3)
				#dmat[i][j] = round((1/(mat[i][j]**2)), 3)
				dmat[i][j] = round(1/(mat[i][j]),3)
	print "setup finished"
	for k in range(0, len(ids)):
		print k
		for i in range(0, len(ids)):
			for j in range(0, len(ids)):
				if i == j:
					dmat[i][j] = 0
				elif dmat[i][j] > dmat[i][k] + dmat[k][j]:
					dmat[i][j] = dmat[i][k] + dmat[j][k]

	dist0_output = open("./dist_main.txt", 'w')
	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			dist0_output.write(repr(dmat[i][j]) + "\n")
	print "strength finished"
	dist0_output.close()


	node_closeness = [0]*len(ids)
	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			if i != j:
				node_closeness[i] += dmat[i][j]
	for i in range(0, len(ids)):
		node_closeness[i] = (len(ids)-1)/node_closeness[i]

	node_closeness_output = open("./node_closeness_main.txt", 'w')
	for i in range(0, len(ids)):
		node_closeness_output.write(ids[i] + ","+mjs[i]+"," + repr(node_closeness[i]) + "\n")
	print "closeness finished"
	node_closeness_output.close()


	"""








	## 1. Calculate Node Strength ( using v )
	# The sum of weights attached to ties belonging to a node (Barrat et al., 2004)
	node_strength = [0]*len(ids)
	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			if i != j:
				node_strength[i] += Mat[i][j]

	node_strength_output = open("./node_strength.txt", 'w')
	for i in range(0, len(node_strength)):
		node_strength_output.write(ids[i] + "," + repr(node_strength[i]) + "\n")
	print "strength finished"
	node_strength_output.close()

	## 2. Calculate Node Closeness Centralities ( using d = 1/v )
	# Redefined by using Dijkstra's distance algorithm (Newman, 2001)[11]
	shortest = copy.deepcopy(Dmat)
	for k in range(0, len(ids)):
		for i in range(0, len(ids)):
			for j in range(0, len(ids)):
				if i == j:
					shortest[i][j] = 0
				elif shortest[i][j] > shortest[i][k] + shortest[k][j]:
					shortest[i][j] = shortest[i][k] + shortest[j][k]

	node_closeness = [0]*len(ids)
	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			if i != j:
				node_closeness[i] += shortest[i][j]
	for i in range(0, len(ids)):
		node_closeness[i] = (len(ids)-1)/node_closeness[i]

	node_closeness_output = open("./node_closeness.txt", 'w')
	for i in range(0, len(node_strength)):
		node_closeness_output.write(ids[i] + "," + repr(node_closeness[i]) + "\n")
	print "closeness finished"
	node_closeness_output.close()

	## 3. Calculate Node Betweenness Centralities ( using d = 1/v )
	# Redefined by using Dijkstra's distance algorithm (Brandes, 2001)[12]
	# Distance Scaled Betweenness Centralities


	## 4. Calculate Global Clustering Coefficient
	# Redefined by using a triplet value (Opsahl and Panzarasa, 2009)[13]


	## 5. Calculate Local Clustering Coefficient
	# Redefined by using a triplet value (Barrat et al., 2004)[2]

	## 6. Component Analysis (Biggest Component Proportion)

	#networkx.connected_components(G)




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

	Type_A = ["BIZ", "MAT", "ECO", "IIE", "EEE"]
	Type_B = ["CSI", "KOR"]
	Type_C = ["CSI", "LIS"]
	Type_D = ["CSI", "LIS", "KOR"]

		## UI. MAT ECO BIZ EEE IIE 15%

	for id_ent in ids:
		if MajorMapping[str(id_ent).translate(None, digits)] in Type_A:
			NodesPartA.append(id_ent)
		if MajorMapping[str(id_ent).translate(None, digits)] in Type_B:
			NodesPartB.append(id_ent)
		if MajorMapping[str(id_ent).translate(None, digits)] in Type_C:
			NodesPartC.append(id_ent)
		if MajorMapping[str(id_ent).translate(None, digits)] in Type_D:
			NodesPartD.append(id_ent)

	for i in range(0, len(ids)):
		for j in range(0, len(ids)):
			if Mat[i][j] >= 0.20:
				LinksOverall_20.append( [ids[i], ids[j], float(Mat[i][j])] ) 
			if Mat[i][j] >= 0.25:
				LinksOverall_25.append( [ids[i], ids[j], float(Mat[i][j])] ) 
			if Mat[i][j] >= 0.30:
				LinksOverall_30.append( [ids[i], ids[j], float(Mat[i][j])] ) 
			
			mj_1 = MajorMapping[str(ids[i]).translate(None, digits)]
			mj_2 = MajorMapping[str(ids[j]).translate(None, digits)]

			if (mj_1 in Type_A) and (mj_2 in Type_A):
				if Mat[i][j] >= 0.15:
					LinksPart_A_15.append( [ids[i], ids[j], float(Mat[i][j])] ) 

			if (mj_1 in Type_B) and (mj_2 in Type_B):
				if Mat[i][j] >= 0.15:
					LinksPart_B_15.append( [ids[i], ids[j], float(Mat[i][j])] ) 

			if (mj_1 in Type_C) and (mj_2 in Type_C):
				if Mat[i][j] >= 0.15:
					LinksPart_C_15.append( [ids[i], ids[j], float(Mat[i][j])] ) 

			if (mj_1 in Type_D) and (mj_2 in Type_D):
				if Mat[i][j] >= 0.15:
					LinksPart_D_15.append( [ids[i], ids[j], float(Mat[i][j])] ) 

	## UI. Overall Network Analysis 20%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksOverall_20
	json_dic["nodes"] = NodesOverall
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('data_overall20.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. Overall Network Analysis 25%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksOverall_25
	json_dic["nodes"] = NodesOverall
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('data_overall25.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. Overall Network Analysis 30%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksOverall_30
	json_dic["nodes"] = NodesOverall
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('data_overall30.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. MAT ECO BIZ EEE IIE 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_A_15
	json_dic["nodes"] = NodesPartA
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('data_typeA15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. KOR SCI 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_B_15
	json_dic["nodes"] = NodesPartB
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('data_typeB15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. KOR SCI 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_C_15
	json_dic["nodes"] = NodesPartC
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('data_typeC15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	## UI. KOR SCI 15%
	json_dic = {}
	json_dic["graph"] = []
	json_dic["links"] = LinksPart_D_15
	json_dic["nodes"] = NodesPartD
	json_dic["directed"] = False
	json_dic["multigraph"] = False
	with open('data_typeD15.json', 'w') as outfile:
	    json.dump(json_dic, outfile)

	"""



