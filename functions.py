from node import * 
import colors

def make_child(father, action): 
    """
    args = 
    father : node 
    action : tuple of direction 
    
    returns a node
    """ 
    new_state = {} 
    new_state['board'] = father.state['board'] 
    new_state['end'] = father.state['end'] 
    
    new_agent_pos_x, new_agent_pos_y = father.state['agent'][0] + action[0], father.state['agent'][1] + action[1]  
    new_state['agent'] = (new_agent_pos_x, new_agent_pos_y) 
    
    child = Node(new_state, father) 
    return child     

def get_actions(state):
    """
    args =
    state : an dict containing board as a np array of 0s and 1s
    a agent as a tuple of cordinates and a end as a tuple of cordinates
    
    retruns a list of tuples that are corresponding directions
    """
    actions = []  
    
    x, y = state['agent']
    if x + 1 < 13 and state['board'][y, x + 1] == 1 :  
        actions.append((1,0)) 
        
    if x - 1 >= 0 and state['board'][y, x - 1] == 1 : 
        actions.append((-1,0))  
        
    if y + 1 < 13 and state['board'][y + 1, x] == 1 : 
        actions.append((0,1))  
        
    if y - 1 >= 0 and state['board'][y - 1, x] == 1 : 
        actions.append((0,-1))     
        
    return actions 

def solution(node, curr_path): 
    """ 
    args = node 
    
    returns a list of nodes cordinates  (tuple)
    """  
    curr_path.append(node.state['agent']) 
        
    if node.father == None :   
        return curr_path
         
    return solution(node.father, curr_path)     

def path_color(board, path):
    """
    args = 
    board : a Board object 
    path : list of cordinations from start to end 
    """ 
    for cor in path : 
        board.colorize(cor[0], cor[1], colors.green)
    