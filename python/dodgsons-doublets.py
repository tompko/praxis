import heapq

wordlist = set()
letters = "abcdefghjiklmnopqrstuvwxyz"

with open("wordlist") as fin:
    for line in fin:
        word = line.strip()
        if word.isalpha():
            wordlist.add(word.lower())

class Problem:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        self.expanded = 0

    def get_start_state(self, ):
        return self.start

    def is_goal(self, state):
        return state == self.finish

    def get_neighbours(self, state):
        ret = []
        for i in range(len(state)):
            curr = state[i]
            for l in letters:
                if l == curr:
                    continue
                new_state = state[:i] + l + state[i+1:]
                if new_state in wordlist:
                    ret.append((new_state, 1))
        self.expanded += 1
        return ret

    def heuristic_cost(self, state):
        return sum([x[0] == x[1] for x in zip(state, self.finish)])

def search(problem):
    start_cost = problem.heuristic_cost(problem.get_start_state())
    start = (start_cost, problem.get_start_state(), problem.get_start_state())
    queue = [start]
    visited = set([start])

    while queue:
        cost, path, curr = heapq.heappop(queue)
        cost -= problem.heuristic_cost(curr)

        visited.add(curr)
        
        if problem.is_goal(curr):
            return path

        for n,c in problem.get_neighbours(curr):
            if n in visited:
                continue
            visited.add(n)
            new_cost = cost + c + problem.heuristic_cost(n)
            new_path = path + " " + n
            heapq.heappush(queue, (new_cost, new_path, n))

    return None        

def doublets(start, finish):
    prob = Problem(start, finish)
    return search(prob)
