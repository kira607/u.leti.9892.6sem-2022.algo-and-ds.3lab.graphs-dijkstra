import os
from typing import Tuple

import graphviz

from .vertex import Vertex
from ._infinity import inf


class Graph:
    def __init__(self, *names: str) -> None:
        self._vertices = {}
        for name in names:
            self.add_vertex(name)

    @property
    def vertices(self):
        return tuple(self._vertices)

    def add_vertex(self, name: str) -> Vertex:
        existing = self._vertices.get(name)
        if existing:
            return existing
        vertex = Vertex(name)
        self._vertices[name] = vertex
        return vertex

    def find_minimal_path(self, v1: str, v2: str) -> Tuple[str]:
        v1 = self._vertices[v1]
        v2 = self._vertices[v2]

        shortest_paths, shortest_paths_values = self._get_dijkstra(v1)

        path = []
        node = v2
        
        while node != v1:
            path.append(node)
            node = shortest_paths[node]

        path.append(v1)

        path = tuple(reversed(tuple(map(lambda x: getattr(x, 'name'), path))))
        value = shortest_paths_values[v2]
        
        return path, value

    def _get_dijkstra(self, root_vertex: Vertex):
        to_visit = list(self._vertices.values())

        shortest_paths_values = {v: inf for v in to_visit}
        shortest_paths_values[root_vertex] = 0
        shortest_paths = {}

        while to_visit:
            min_vertex = min(to_visit, key=lambda vertex: shortest_paths_values[vertex])
            for neighbor, edge_value in min_vertex.neighbors:
                vertex_value = shortest_paths_values[min_vertex] + edge_value
                if vertex_value < shortest_paths_values[neighbor]:
                    shortest_paths_values[neighbor] = vertex_value
                    shortest_paths[neighbor] = min_vertex
            to_visit.remove(min_vertex)
        
        return shortest_paths, shortest_paths_values

    def get_dot_string(self) -> str:
        s = 'digraph {\n'
        for v in self._vertices.values():
            s += v.get_dot_string()
        s += '}'
        return s


def load_graph(path: str):
    graph = Graph()
    with open(path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = [s.strip() for s in line.split(';')]
        source_vertex_name, target_vertex_name, source_target_value, target_source_value = line
        if source_target_value != 'N/A':
            source_target_value = int(source_target_value)
            source_vertex = graph.add_vertex(source_vertex_name)
            target_vertex = graph.add_vertex(target_vertex_name)
            source_vertex.add_neighbor(target_vertex, source_target_value)
        if target_source_value != 'N/A':
            target_source_value = int(target_source_value)
            source_vertex = graph.add_vertex(source_vertex_name)
            target_vertex = graph.add_vertex(target_vertex_name)
            target_vertex.add_neighbor(source_vertex, target_source_value)
    return graph


def export_graph(graph: Graph, path: str, name: str = 'graph') -> None:
    file_path = os.path.join(path, f'{name}.dot')
    graphviz.Source(graph.get_dot_string()).render(file_path)