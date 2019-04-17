from data import EDGES
from data_structures import Map

unilag_map = Map()

unilag_map.add_edges(EDGES)

if __name__ == "__main__":
    source = raw_input("Where are you now? (Press Enter to exit) ")
    
    while source != "":
        destination = raw_input("Where are you going? ")
        
        path = unilag_map.get_shortest_path(source, destination)

        print()
        for node in path[:-1]:
            print(str(node) + " -> ")
        print(str(path[-1]) + "\n")

        source = raw_input("Where are you now? (Press Enter to exit) ")
