from queue import PriorityQueue

# Creating Base Class


class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path[:]
            self.path.append(value)

        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def Get_Distances(self):
        pass

    def Make_Child_Nodes(self):
        pass


# Creating subclass
class state_string(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(state_string, self).__init__(value, parent, start, goal)
        self.dist = self.Get_Distances()

    def Get_Distances(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def Make_Child_Nodes(self):
        if not self.children:
            for i in range(len(self.goal) - 1):
                val = self.value
                val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
                child = state_string(val, self)
                self.children.append(child)

# Creating a class that hold the final magic


class A_Star_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.vistedQueue = []
        self.pQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve_A_Star(self):
        startState = state_string(self.start, 0, self.start, self.goal)

        count = 0
        self.pQueue.put((0, count, startState))
        while(not self.path and self.pQueue.qsize()):
            closest_child = self.pQueue.get()[2]
            closest_child.Make_Child_Nodes()
            self.vistedQueue.append(closest_child.value)
            for child in closest_child.children:
                if child.value not in self.vistedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.pQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal Of  is not possible !" + self.goal)
        return self.path


# Calling all the existing stuffs

source = "hema"
end = "mahe"
solver = A_Star_Solver(source, end)
solver.Solve_A_Star()
for i in range(len(solver.path)):
    print("{0}){1}".format(i, solver.path[i]))
