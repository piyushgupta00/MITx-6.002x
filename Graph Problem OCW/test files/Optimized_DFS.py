# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:25:25 2018

@author: Piyush
"""
#import sys
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

graph=load_map('test_mit_map.txt')
print(graph)

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def DFS(graph, start, end, path, shortest,toPrint = False,shortest_path_length=0):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    pathlength=0
    
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            
            for dest in graph.edges[start]:
                if dest[0]==node:
                    
                   #print('printing destination dist: ',dest[1][0])
                   #print('printing pathlength', pathlength)
                    pathlength=int(pathlength)+int(dest[1][0])
                
            
            if shortest == None or pathlength < shortest_path_length:
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
                    length=0
                    for i in range(len(shortest)-1):
                        node1=shortest[i]
                        node2=shortest[i+1]
                        for dest in graph.edges[node1]:
                          if dest[0]==node2:
                            pathlength=pathlength+int(dest[1][0])
                    shortest_path_length=length
        elif toPrint:
            print('Already visited', node)
            
    return shortest
    
def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, toPrint)

def testSP(source, destination):
    g = load_map('test_mit_map.txt')
    sp = shortestPath(g, Node(source), Node(destination),toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

#testSP('Chicago', 'Boston')
#
testSP('a','f')