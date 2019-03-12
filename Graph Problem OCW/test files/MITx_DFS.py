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

def getTotalPathLength(path):
    if path==None:
        return 0
    pathlength=0
    for i in range(len(path)-1):

        pathlength=pathlength+getTotalEdgeWeight(path[i],path[i+1])
    return pathlength

def getOutPathLength(path):
    if path==None:
        return 0
    pathlength=0
    for i in range(len(path)-1):

        pathlength=pathlength+getOutEdgeWeight(path[i],path[i+1])
    return pathlength

def getTotalEdgeWeight(node1,node2):
    
    for edge in graph.edges[node1]:
        if edge[0]==node2:
            return int(edge[1][0])
        
def getOutEdgeWeight(node1,node2):
    
    for edge in graph.edges[node1]:
        if edge[0]==node2:
            return int(edge[1][1])
    

def DFS(graph, start, end, path, shortest,shortest_path_length,shortest_out_dist,\
        pathlength,maxOutdistance,toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph under the given constraint
       of maximum outdoor distance"""
       
    
    path = path + [start]
    totalpathlength=getTotalPathLength(path)
    outerpathlength=getOutPathLength(path)
    
    
    if toPrint:
        pass 
        
    if start == end and outerpathlength<=maxOutdistance and (totalpathlength <= shortest_path_length):
        print('A Shorter Path found',path,[totalpathlength],[outerpathlength])
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            
            
            
            if shortest== None or totalpathlength <= shortest_path_length:
              if totalpathlength <shortest_path_length and outerpathlength<=maxOutdistance  :
                newPath = DFS(graph, node, end, path, shortest, shortest_path_length,\
                              shortest_out_dist,pathlength, maxOutdistance, toPrint)
                
                if newPath != None:
                    
                      shortest = newPath
                      shortest_path_length=getTotalPathLength(shortest)
                      shortest_out_dist=getOutPathLength(shortest)
                      

       
    return shortest
    
def shortestPath(graph, start, end, maxOutdistance, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, sys.maxsize, sys.maxsize, 0, maxOutdistance, toPrint)

def testSP(source, destination,maxOutdistance):
    g = load_map('mit_map.txt')
    
    sp = shortestPath(g, Node(source), Node(destination), maxOutdistance,toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from {} to {} for the given constraint'.format(source,destination))


testSP('2','9',0)
