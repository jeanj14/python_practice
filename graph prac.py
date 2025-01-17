# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:55:13 2024

@author: ALBERTJUNIOR
"""
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:", self.graph_dict)
        
    def get_paths(self, start, end, path=[]):
        path+= [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    path.append(p)

if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"), 
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")]
    
    route_graph = Graph(routes)

    start = "Mumbai" 
    end = "Mumbai"
    
    print(f"Paths between {start} and {end}", route_graph.get_paths(start, end))