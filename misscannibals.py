from search import * #search is another given file that has all the search algos

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def actions(self, state):
        m, c, onLeft = state
        possible_actions = []
        if onLeft:
            if m >= 2:
                possible_actions.append('MM')
            if m >= 1 and c >= 1:
                possible_actions.append('MC')
            if c >= 2:
                possible_actions.append('CC')
            if m >= 1:
                possible_actions.append('M')
            if c >= 1:
                possible_actions.append('C')
        else:
            if self.M - m >= 2:
                possible_actions.append('MM')
            if self.M - m >= 1 and self.C - c >= 1:
                possible_actions.append('MC')
            if self.C - c >= 2:
                possible_actions.append('CC')
            if self.M - m >= 1:
                possible_actions.append('M')
            if self.C - c >= 1:
                possible_actions.append('C')
        return [action for action in possible_actions if self.valid_state(self.result(state, action))]

    def result(self, state, action):
        m, c, onLeft = state
        num_m = action.count('M')
        num_c = action.count('C')
        if onLeft:
            new_state = (m - num_m, c - num_c, not onLeft)
        else:
            new_state = (m + num_m, c + num_c, not onLeft)
        return new_state

    def goal_test(self, state):
        return state == self.goal

    def valid_state(self, state):
        m, c, _ = state
        if m < 0 or c < 0 or m > self.M or c > self.C:
            return False
        if m > 0 and m < c:
            return False
        if self.M - m > 0 and self.M - m < self.C - c:
            return False
        return True

# Main function to test the MissCannibals class
if __name__ == '__main__':
    from search import depth_first_graph_search, breadth_first_graph_search

    mc = MissCannibals(M=3, C=3)
    
    # Testing the actions method
    print(mc.actions((3, 2, True)))  # Test your code as you develop! This should return  ['CC', 'C', 'M']

    path = depth_first_graph_search(mc).solution()
    print("Depth First Search Solution:", path)
    
    path = breadth_first_graph_search(mc).solution()
    print("Breadth First Search Solution:", path)
