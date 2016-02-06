from graph import  UndirectedGraph, Graph

# Reads and creates a graph from a file
def read_city_graph(filename):
    #set the three variables we are gonna output
    EdGraph = UndirectedGraph()
    roadNames = []
    locations = {}
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
                EdGraph.add_edge(line[1],line[2])
                roadNames.append([int(line[1]),int(line[2]), line[3].strip()])
    return(EdGraph,roadNames,locations)
#The variable association bellow is purely for readability
v = read_city_graph('edmonton-roads-2.0.1.txt')
EdGraph = v[0]
roadNames = v[1]
locations = v[2]
