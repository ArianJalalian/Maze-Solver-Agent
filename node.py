import math 

class Node: 
    def __init__(self, state, father):
        """  
        args =
        state : an dict containing board as a np array of 0s and 1s
        a agent as a tuple of cordinates and a end as a tuple of cordinates
        father : node
        """
        self.state = state
        self.father = father   
        self.path_cost = 0 if father is None else father.path_cost + 1 
        self.total_cost = self.path_cost + self.calculate_heuristic()
        
        
        
    def is_goal(self):  
        return self.state['agent'] == self.state['end']  
    
    def calculate_heuristic(self):
        x_start, y_start = self.state['agent'] 
        x_end, y_end = self.state['end']
        
        return math.sqrt((x_start-x_end)**2 + (y_start-y_end)**2)