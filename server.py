from graph import  UndirectedGraph, Graph
import math

#calculates the distance between two points
def cost_distance(u,v):
    dist = math.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)
    return dist

# Reads and creates a graph from a file
def read_city_graph(filename):
    #set the three variables we are gonna output
    EdGraph = UndirectedGraph()
    roadNames = []
    locations = {}
    weights = {}
    """
    Goes through each line of the file
    and creates a vertice or an edge
    """
    with open(filename,"r",) as file:
        for line in file:
            line = line.split(",")

            if line[0] == "V":
                EdGraph.add_vertex(int(line[1]))
                #appends the information we need about the vertice
                locations[int(line[1])] = [int(float(line[2])*100000),int(float(line[3])*100000)]
            elif line[0] == "E":
                EdGraph.add_edge(int(line[1]),int(line[2]))
                roadNames.append([int(line[1]),int(line[2]), line[3].strip()])
                weights[(int(line[1]),int(line[2]))] = cost_distance(locations[int(line[1])],locations[int(line[2])])
    return(EdGraph,roadNames,locations,weights)
#the following functions gets the closest vertices to the start and end of the given input
def closestVertices(locations, startx, starty, endx, endy):
    startLoc = [startx,starty]
    endLoc = [endx, endy]
    startVert = 0
    endVert = 0
    for x in locations:
        pstartVert = cost_distance(locations[x], startLoc)
        pendVert = cost_distance(locations[x], endLoc)

#The variable association below is purely for readability
v = read_city_graph('edmonton-roads-2.0.1.txt')
EdGraph = v[0]
roadNames = v[1]
locations = v[2]
weights = v[3]
print(weights)