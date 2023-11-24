from functions import * 

class Agent:
    def __init__(self, root): 
        """ 
        args =
        root : node
        """
        self.root = root 
    
    def fs(self, kind): 
        """ 
        args = 
        kind : a string which is 'b' or 'd' that specifies which kind of first-search graph to use
        returns a list of nodes cordinates (tuple)
        """ 
        poping_index = lambda frontier : 0 if kind == 'b' else len(frontier) - 1
        
        node = self.root 
        if node.is_goal() : 
            return solution(node, []) 
        
        frontier = [node]  
        frontier_states = [node.state['agent']] 
        explored = []   
        
        while True:          
            if len(frontier) == 0: 
                return "failure"
        
            node = frontier.pop(poping_index(frontier))  
            frontier_states.pop(poping_index(frontier))
            explored.append(node.state['agent']) 
            
            actions = get_actions(node.state)
            for action in actions: 
                child = make_child(node, action) 
                if child.state['agent'] not in explored and child.state['agent'] not in frontier_states: 
                    if child.is_goal() :  
                        return solution(child, []) 
                    frontier.append(child) 
                    frontier_states.append(child.state['agent']) 
                                        

    def a_star(self): 
        """
        returns a list of nodes cordinates (tuple)
        """
        node = self.root 
        if node.is_goal() : 
            return solution(node, []) 
        
        frontier = [node]  
        frontier_state = [node.state['agent']]
        explored = []    
        
        while True:          
            if len(frontier) == 0: 
                return "failure" 
            
            node = frontier.pop(0)
            frontier_state.remove(node.state['agent'])
            
            if node.is_goal() : 
                return solution(node, [])
            
            explored.append(node.state['agent']) 
            
            actions = get_actions(node.state)
            for action in actions: 
                child = make_child(node, action)  
                
                if child.state['agent'] not in explored and child.state['agent'] not in frontier_state : 
                    frontier.append(child)   
                    frontier.sort(key=lambda node : node.total_cost)  
                    
                    frontier_state.append(child.state['agent']) 
                    
                elif child.state['agent'] in frontier_state : 
                    arr = list(filter(lambda node : node.state['agent'] == child.state['agent'] and 
                                                 node.total_cost > child.total_cost, frontier)) 
                    if len(arr) != 0 : 
                        replaced_node = arr[0] 
                        replaced_node.father = child.father
                        replaced_node.total_cost = child.total_cost
