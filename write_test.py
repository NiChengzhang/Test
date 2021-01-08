# coding=utf-8
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import copy
import numpy as np
import time
from class_network_1 import inf_network




from FUN_MULTI_NETWORK_SPREAD import MULTI_NETWORK_SPREAD #MULTI_NETWORK_SPREAD(MULTI_NETWORK, N_LAYERS, inf_index, BETA)
from FUN_CAL_INFLUENCE import CAL_INFLUENCE #CAL_INFLUENCE(MULTI_NETWORK, N_NODES, N_EDGES, N_LAYERS, RADIUS)
from FUN_CAL_EDGE import CAL_EDGE #CAL_EDGE(MULTI_NETWORK, N_NODES, N_EDGES, N_LAYERS)
from FUN_RANK import RANK #RANK(N_NODES, data)

#更改path可以改变生成网络的目录,请在源文件的目录下先新建文件夹(假设是doc_name).
#然后此时path = './doc_name/'
#detail.txt包含网络的节点数,边的数量(和随机生成的网络有关), 网络层数的信息
#x.nt则记录每一层节点的不同节点间的权重
# def GENERATE_MUL_NETWORK(N_NODES, N_EDGES, N_LAYERS, path):
# 	read = open(path + 'detail.txt', 'w')
# 	read.write("#NODES #EDGES #LAYERS" + '\n')
# 	read.write("{0:^5d} {1:^5d} {2:^5d}".format(N_NODES, N_EDGES, N_LAYERS) + '\n')
# 	read.close()
	
# 	MULTI_NETWORK = list()
# 	ori_network = inf_network(N_NODES, N_EDGES)
# 	MULTI_NETWORK.append(ori_network)
# 	for i in range(N_LAYERS - 1):
# 		#两种方法
# 		#1 新生成节点数量相同，边不同的网络
# 		MULTI_NETWORK.append(inf_network(N_NODES, N_EDGES))
# 		#2 生成和初始网络数量相同，边相同，只有权重不同的网络
# 		# MULTI_NETWORK.append(copy.deepcopy(ori_network).change_weight())
# 	for i in range(N_LAYERS):
# 		MULTI_NETWORK[i].layer = i

# 	for NETWORK in MULTI_NETWORK:	
# 		read = open(path + '{}.nt'.format(NETWORK.layer), 'wb')
# 		nx.write_multiline_adjlist(NETWORK.network, read, delimiter = ',')
# 		read.close()

# 	return True





def GENERATE_MUL_NETWORK(NETWORK_DICT, RANDOM_DICT, N_LAYERS, path):
	
	#这个功能可以暂时封存了,不要也罢
	
	

	MULTI_NETWORK = list()
	for value in NETWORK_DICT.values():
		MULTI_NETWORK.append(inf_network(False, None, value['name'], **value['arg']))


	for i in range(N_LAYERS):
		MULTI_NETWORK[i].layer = i

	for i in range(N_LAYERS):
		MULTI_NETWORK[i].change_weight(RANDOM_DICT[str(i + 1)]['fun'], **RANDOM_DICT[str(i + 1)]['arg'])


	for NETWORK in MULTI_NETWORK:	
		read = open(path + '{}.nt'.format(NETWORK.layer), 'wb')
		nx.write_multiline_adjlist(NETWORK.network, read, delimiter = ',')
		read.close()

	read = open(path + 'detail.txt', 'w')
	read.write("#NODES #LAYERS" + '\n')
	read.write("{0:^5d} {1:^5d}".format(MULTI_NETWORK[0].num_nodes, N_LAYERS) + '\n')
	read.close()

	return True




if __name__ == '__main__':

	def random_gen(mu = 0,sigma = 1):
		#生成符合分布的随机数
		val = random.gauss(mu, sigma)
		while( val <= 0 or val > 1):
			val = random.gauss(mu, sigma)
		return val


	NT_DICT = {'1': {'name':nx.barabasi_albert_graph, 'arg':{'n':100, 'm':5}}, 
	'2': {'name':nx.watts_strogatz_graph, 'arg':{'n':100, 'k':10, 'p':0.5}},
	'3': {'name':nx.barabasi_albert_graph, 'arg':{'n':100, 'm':7}}}

	NT_DICT_2 = {'1': {'name':nx.barabasi_albert_graph, 'arg':{'n':100, 'm':5}}, 
	'2': {'name':nx.watts_strogatz_graph, 'arg':{'n':100, 'k':10, 'p':0.5}},
	'3': {'name':nx.binomial_graph, 'arg':{'n':100, 'p':0.1}}}

	RANDOM_DICT_2 = {'1': {'fun':random.uniform, 'arg':{'a':0, 'b':1}}, 
	'2': {'fun':random.random, 'arg':{'a':0}},
	'3': {'fun':random_gen, 'arg':{'mu':0, 'sigma':1}}}					
	
	NT_DICT_FINAL = {'1': {'name':nx.barabasi_albert_graph, 'arg':{'n':1000, 'm':5}}, 
	'2': {'name':nx.watts_strogatz_graph, 'arg':{'n':5000, 'k':10, 'p':0.1}},
	'3': {'name':nx.binomial_graph, 'arg':{'n':5000, 'p':0.1}}}

	NT_DICT_12_28 = {'1': {'name':nx.barabasi_albert_graph, 'arg':{'n':1000, 'm':5}},
	'2': {'name':nx.barabasi_albert_graph, 'arg':{'n':1000, 'm':5}},
	'3': {'name':nx.barabasi_albert_graph, 'arg':{'n':1000, 'm':5}}}

	S500 = {'1': {'name':nx.barabasi_albert_graph, 'arg':{'n':500, 'm':7}}}		

	# N_NODES = 100#设置节点数
	# N_EDGES = 5#设置每个节点的连边数
	N_LAYERS = 3
	GENERATE_MUL_NETWORK(NT_DICT_12_28, RANDOM_DICT_2, N_LAYERS, "./12_28/")



