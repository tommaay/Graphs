"""
Simple graph implementation
"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    # Breadth First Traversal
    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()
        # Put the starting vertex in the Queue
        q.enqueue(starting_vertex_id)
        # While the Queue is not empty...
        while q.size() > 0:
            # Dequeue the first node from the Queue
            v = q.dequeue()
            # If note hasn't been visited, add it to visited
            if v not in visited:
                print(v)
                visited.add(v)
                # Put children into Queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    # Depth First Traversal
    def dft(self, starting_vertex_id):
        s = Stack()
        visited = set()
        # Put the starting vertex in the Stack
        s.push(starting_vertex_id)
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the top node from the Stack
            v = s.pop()
            # If that node has not been visted, add it to visited
            if v not in visited:
                print(v)
                visited.add(v)
                # Put children into Stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    # Recursive Depth First Traversal
    def dft_recursive(self, starting_vertex_id, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex_id)

        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_directed_edge(1, 2)
g.add_directed_edge(1, 3)
g.add_directed_edge(2, 3)
g.add_directed_edge(3, 4)
print(g.vertices)
print(g.dft(1))
