'''
    Python file to implement the class CrewMate
'''

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        # treasure_heap_for_process is heap of treasures used to 
        self.treasure_heap_for_process = None # Treasure heap stored in each crewmate for processing
        self.treasure_list_of_crewmate = [] # I keep record of all treasure assigned to a crewmate by storing them in a list
        self.total_load = 0 # Total load variable that represents the time at which the crewmate will be free from all treasures
        self.isempty = True # Boolean variable for checking crewmate has assigned some treasure or not

    # Add more methods if required