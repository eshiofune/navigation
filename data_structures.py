import sys

from helpers import distance, match_node


class Node:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __eq__(self, node):
        '''
        Defines the equivalence of two nodes as the equality of their names.
        '''
        return self.name == node.name

    def __str__(self):
        return self.name


class Map:
    '''
    Data structure that represents a map as a special kind of graph
    '''

    _edges = []
    
    def add_edges(self, edges):
        self._edges = edges

    def get_nodes(self):
        '''
        Returns all the nodes in the map
        '''
        nodes = []

        for edge in self._edges:
            if edge[0] not in nodes:
                nodes.append(edge[0])
            if edge[1] not in nodes:
                nodes.append(edge[1])
        
        return nodes

    def get_distance(self, node1, node2):
        '''
        Returns the distance between two nodes
        '''
        return distance(node1.position, node2.position)

    def get_neighbours(self, node):
        '''
        Returns the neighbours of a node, that is, all the nodes
        that share an edge with the specified node
        '''
        neighbours = []

        for edge in self._edges:
            if node in edge:
                neighbours.append(
                    edge[0] if edge[1] == node else edge[1]
                )

        return neighbours

    def _is_in_between(self, first, second, middle):
        '''
        Returns True if middle is in-between the first and second
        nodes in position, otherwise False
        '''
        res = False
        
        if first.position[0] < second.position[0]:
            res = middle.position[0] >= first.position[0] and middle.position[0] <= second.position[0]
        elif first.position[0] > second.position[0]:
            res = middle.position[0] <= first.position[0] and middle.position[0] >= second.position[0]
        else:
            res = middle.position[0] == first.position[0]

        if first.position[1] < second.position[1]:
            res = middle.position[1] >= first.position[1] and middle.position[1] <= second.position[1]
        elif first.position[1] > second.position[1]:
            res = middle.position[1] <= first.position[1] and middle.position[1] >= second.position[1]
        else:
            res = middle.position[1] == first.position[1]

        return res
    
    def get_node(self, name):
        '''
        Returns the node with this name
        '''
        if type(name) == Node:
            return name
        elif type(name) == str:
            return match_node(self.get_nodes(), name)
        
        raise TypeError("name must be a string")
    
    def get_shortest_path(self, start_node, destination):
        '''
        Returns a collection of all the nodes that lie on the shortest path
        between the start_node and the destination
        '''
        start_node, destination = self.get_node(start_node), self.get_node(destination)

        current_node = start_node
        path = [current_node]

        while current_node != destination:
            min_distance = self.get_distance(current_node, destination)

            for neighbour in self.get_neighbours(current_node):
                if self._is_in_between(current_node, destination, neighbour):
                    if self.get_distance(neighbour, destination) < min_distance:
                        current_node = neighbour
            
            if len(path) > 0 and current_node == path[-1]:
                # No route to destination from the current node. Backtrack to last node on path
                path = path[:-1]

                if len(path) == 0:
                    # No route to destination from start_node
                    break
                else:
                    current_node = path[-1]
            else:
                path.append(current_node)

        return path