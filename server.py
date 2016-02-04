import graph

# Reads and creates a graph from a file
def read_city_graph(filename):
    EdGraph = UndirectedGraph()
    """
    Goes through each line of the file
    and creates a vertice or an edge
    """
    with open(filename,"r",) as file:
        for line in file:
            line = line.split(",")
            if line[0] == "V":
                EdGraph.add_vertex(line[1])
            elif line[0] == "E":
                EdGraph.add_edge(line[1],line[2])
    return(EdGraph)
