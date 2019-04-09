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
    def bf_traverse(self, starting_vertex_id):
        search_queue = Queue()
        visited = set()
        # Put the starting vertex in the Queue
        search_queue.enqueue(starting_vertex_id)
        # While the Queue is not empty...
        while search_queue.size() > 0:
            # Dequeue the first node from the Queue
            v = search_queue.dequeue()
            # If note hasn't been visited, add it to visited
            if v not in visited:
                print(v)
                visited.add(v)
                # Put children into Queue
                for neighbor in self.vertices[v]:
                    search_queue.enqueue(neighbor)

    # Depth First Traversal
    def df_traverse(self, starting_vertex_id):
        search_stack = Stack()
        visited = set()
        # Put the starting vertex in the Stack
        search_stack.push(starting_vertex_id)
        # While the stack is not empty...
        while search_stack.size() > 0:
            # Pop the top node from the Stack
            v = search_stack.pop()
            # If that node has not been visted, add it to visited
            if v not in visited:
                print(v)
                visited.add(v)
                # Put children into Stack
                for neighbor in self.vertices[v]:
                    search_stack.push(neighbor)

    # Recursive Depth First Traversal
    def dft_recursive(self, starting_vertex_id, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex_id)

        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    # Breadth First Search
    def bf_search(self, starting_vertex_id, target_id):
        search_queue = Queue()
        searched = set()
        # Put the starting vertex in the Queue
        search_queue.enqueue([starting_vertex_id])
        # While the Queue is not empty...
        while search_queue.size() > 0:
            # Dequeue the first node from the Queue
            path = search_queue.dequeue()
            print('path', path)
            v = path[-1]
            # If node hasn't been searched, add it to searched
            if v not in searched:
                # check if node value == target
                if v == target_id:
                    return path

                searched.add(v)
                # Put children into Queue
                for neighbor in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    search_queue.enqueue(new_path)
        return None

    # Breadth First Search
    def df_search(self, starting_vertex_id, target_id):
        search_stack = Stack()
        searched = set()
        # Put the starting vertex in the Stack
        search_stack.push([starting_vertex_id])
        # While the stack is not empty...
        while search_stack.size() > 0:
            # Pop the top node from the Stack
            print('search_stack', search_stack.stack)
            path = search_stack.pop()
            print('path', path)
            v = path[-1]
            # If node hasn't been searched, add it to searched
            if v not in searched:
                # check if node value == target
                if v == target_id:
                    return path

                searched.add(v)
                # Put children onto Stack
                for neighbor in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    search_stack.push(new_path)
        return None


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
# print(g.bf_search(1, 4))
print(g.df_search(1, 4))
print(g.df_search(1, 6))
