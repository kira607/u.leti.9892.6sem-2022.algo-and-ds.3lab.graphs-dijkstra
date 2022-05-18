from typing import Tuple

class Vertex:
    def __init__(self, name: str) -> None:
        self.name = name
        self._neighbors = {}

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} \'{self.name}\'>'

    def __str__(self) -> str:
        return repr(self)

    def __eq__(self, other: 'Vertex') -> bool:
        return hash(self) == hash(other)

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def neighbors(self) -> Tuple[Tuple['Vertex', int]]:
        return tuple(self._neighbors.items())

    def add_neighbor(self, neighbor: 'Vertex', weight: int) -> None:
        if not isinstance(neighbor, Vertex):
            raise TypeError(neighbor)
        self._neighbors[neighbor] = weight

    def get_dot_string(self) -> str:
        s = ''
        for v, w in self._neighbors.items():
            s += f'"{self.name}" -> "{v.name}" [label="{w}"]\n'
        return s
