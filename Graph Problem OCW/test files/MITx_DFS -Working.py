# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:25:25 2018

@author: Piyush
"""
import sys
from graph import Digraph, Node, WeightedEdge
def load_map(map_filename):
   
    graph=Digraph()
    print("Loading map from file...")
    f = open(map_filename, 'r')
    for line in f:
        line_data = line.rstrip('\n').split(' ')
        
        node1=Node(str(line_data[0]))
        node2=Node(str(line_data[1]))
        if node1 not in graph.nodes:
            graph.add_node(node1)
        if node2 not in graph.nodes:
            graph.add_node(node2)
        edge=WeightedEdge(node1,node2,line_data[2],line_data[3])
        graph.add_edge(edge)
    
    return graph

graph=load_map('mit_map.txt')
print(graph)

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def getPathLength(path):
    if path==None:
        return 0
    pathlength=0
    for i in range(len(path)-1):

        pathlength=pathlength+getEdgeWeight(path[i],path[i+1])
    return pathlength

def getEdgeWeight(node1,node2):
    
    for edge in graph.edges[node1]:
        if edge[0]==node2:
            return int(edge[1][0])
    

def DFS(graph, start, end, path, shortest,shortest_path_length,\
        pathlength,toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
       
    
    path = path + [start]
    pathlength=getPathLength(path)
    
    
    if toPrint:
        print('Current DFS path and its length is:', printPath(path),[pathlength])
        #print('current shortest path length is: ',[shortest_path_length])
    if start == end and pathlength <= shortest_path_length :
        print('A Shorter Path found')
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            
            #print('checking path validity: ',pathlength <= shortest_path_length)
            if shortest== None or pathlength <= shortest_path_length:
                newPath = DFS(graph, node, end, path, shortest, shortest_path_length,\
                              pathlength, toPrint)
                
                if newPath != None:
                    
                      shortest = newPath
                      shortest_path_length=getPathLength(shortest)
                      print('current shortest is' , shortest, [shortest_path_length])
                    
        elif toPrint:
            print('Already visited', node)

       
    return shortest
    
def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [],None,sys.maxsize,0,toPrint)

def testSP(source, destination):
    g = load_map('mit_map.txt')
    
    sp = shortestPath(g, Node(source), Node(destination),toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


testSP('1','5')
