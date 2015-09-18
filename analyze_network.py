import os as os
import sys as sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import operator
import pickle
#from convert_txt_to_csv import converttxt
#import pymysql
#from database_network import write_to_database


def analyzenetwork(networkname, centrality):
	"""this function calculates and graphs the network by different centrality measurements, including betweenness and closeness, for selected network"""

	"""
	Note: this project originally stores all data to a local MySQL database via pymysql. However, this disables researchers other than myself from replicating the analysis. Therefore, in this version, I stopped using database as the method to store and manage data. Following codes are for reference only.
	"""

	#networkname = str(networkname)
	#networkbriefname = str(networkname)[0:3]

	#db = pymysql.connect(host='localhost', user='root', passwd='xxxxxx', db='Final')
	#c = db.cursor()

	#query = """SELECT * FROM network WHERE layer = '%s'""" % networkbriefname #get selected network (contrained by the "layer" name) from the databate
	#c.execute(query)
	#data = c.fetchall()
	##print data
	


	# retrive relational data stored in the /Data directory
	filename = str(networkname) + ".txt"

	path = os.getcwd()   #get current working directory
	filepath = path + "/Data/" + filename

	f = open(filepath, 'r')   #open the file with network data

	
	# adding data to graph "g" by iterate through the opened file
	g = nx.DiGraph() 
	g.clear()
	
	for i in iter(f):
		line = i.split()
		sender = line[0]
		receiver = line[1]
		g.add_edge(sender, receiver)
		#print (sender, receiver)
	#print(networkname, 'has:', g.nodes())

	f.close()


	# creating directories for pictures and outputs if does not exist
	pics = 'Pics/'
	outputs = 'Outputs'

	if not os.path.exists(pics):
		os.makedirs(pics)
	if not os.path.exists(outputs):
		os.makedirs(outputs)


	# centrality calculation and visualization
	if str(centrality) == "eigenvector": 
		# calculating centrality
		eigenvector = nx.eigenvector_centrality(g)
		# create a file with nodes sorted by their eigenvector centrality, and save it under the Outputs directory
		sorted_eigenvector = sorted(eigenvector.items(), key=operator.itemgetter(1), reverse=True)
		#print sorted_eigenvector, type(sorted_eigenvector)
		centrality_value_file = path + "/Outputs/" + str(networkname) + '_eigenvector' + '.txt'
		f_centrality = open(centrality_value_file, 'w')
		for item in sorted_eigenvector:
			#print item, type(item)
			#print item[0], item[1], type(item[0]), type(item[1])
			f_centrality.write(item[0])
			f_centrality.write(',')
			f_centrality.write(str(item[1]))
			f_centrality.write("\n")
		f_centrality.close()
		#print f_centrality

		# visualize the network and save it as a .png file under the Pics dictory
		e = eigenvector
		#lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, with_labels=True, node_color='blue', nodelist=e.keys(), node_size=[v * 1000 for v in e.values()], font_size=7)

		filename = "Pics/" + str(networkname) + "_" + str(centrality) + '.png'
		plt.savefig(filename)

		#return(eigenvector)

	elif str(centrality) == "closeness": 
		# calculating centrality
		closeness = nx.closeness_centrality(g)
		# create a file with nodes sorted by their closeness centrality, and save it under the Outputs directory
		sorted_closeness = sorted(closeness.items(), key=operator.itemgetter(1), reverse=True)
		#print sorted_closeness, type(sorted_closeness)
		centrality_value_file = path + "/Outputs/" + str(networkname) + '_closeness' + '.txt'
		f_centrality = open(centrality_value_file, 'w')
		for item in sorted_closeness:
			#print item, type(item)
			#print item[0], item[1], type(item[0]), type(item[1])
			f_centrality.write(item[0])
			f_centrality.write(',')
			f_centrality.write(str(item[1]))
			f_centrality.write("\n")
		f_centrality.close()
		#print f_centrality

		# visualize the network and save it as a .png file under the Pics dictory
		c = closeness
		#lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, with_labels=True, node_color='blue', nodelist=c.keys(), node_size=[v * 1000 for v in c.values()], font_size=7)

		filename = "Pics/" + str(networkname) + "_" + str(centrality) + '.png'
		plt.savefig(filename)


		#return(closeness)

	elif str(centrality) == "betweenness": 
		# calculating centrality
		betweenness = nx.betweenness_centrality(g)
		
		# create a file with nodes sorted by their betweenness centrality, and save it under the Outputs directory
		sorted_betweenness = sorted(betweenness.items(), key=operator.itemgetter(1), reverse=True)
		#print sorted_betweenness, type(sorted_betweenness)
		centrality_value_file = path + "/Outputs/" + str(networkname) + '_betweenness' + '.txt'
		f_centrality = open(centrality_value_file, 'w')
		for item in sorted_betweenness:
			#print item, type(item)
			#print item[0], item[1], type(item[0]), type(item[1])
			f_centrality.write(item[0])
			f_centrality.write(',')
			f_centrality.write(str(item[1]))
			f_centrality.write("\n")
		f_centrality.close()
		#print f_centrality


		
		# visualize the network and save it as a .png file under the Pics dictory
		b = betweenness
		#lyt = nx.layout.spring_layout(g) # making sure the node positions are the same
		nx.draw(g, with_labels=True, node_color='blue', nodelist=b.keys(), node_size=[v * 6000 for v in b.values()], font_size=7)
		filename = "Pics/" + str(networkname) + "_" + str(centrality) + '.png'
		plt.savefig(filename)
	
		#return(betweenness)



if __name__ == "__main__":
	analyzenetwork(sys.argv[1], sys.argv[2])

