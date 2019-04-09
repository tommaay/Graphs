import random


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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i}")
        # Create Friendships
        # Generate all possible friendship combinations
        possibleFriendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        # Shuffle the possible friendships
        random.shuffle(possibleFriendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: numUsers * avgFriendships // 2
        # Need to divide by 2 since each addFriendship() creates 2 friendships
        for i in range(numUsers * avgFriendships // 2):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

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
            v = path[-1]
            # If node hasn't been searched, add it to searched
            if v not in searched:
                # check if node value == target
                if v == target_id:
                    return path

                searched.add(v)
                # Put children into Queue
                for neighbor in self.friendships[v]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    search_queue.enqueue(new_path)
        return None

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        # Loop through the friends list
        for i in range(1, len(self.friendships)+1):
            # Set path from userId to i if there is one or None if there isn't
            visited[i] = self.bf_search(userID, i)
        # Return the social paths excluding None
        return {k: v for k, v in visited.items() if v != None}


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
