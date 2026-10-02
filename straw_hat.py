'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate 
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        # Crewmate heap based on loads for storing treasure
        self.crew_mate_heap = heap.Heap(self.comparison_for_crewmate,[crewmate.CrewMate() for i in range(m)])
        # to increase optimality of code i have stored those crewmates in a list which have atlease one treasure
        self.list_in_which_crewmate_have_treasure = []
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        # I add treasure based on at what time the crewmate will be free
        # I will assign treasure to that crewmate which will be free earliest to all of them
        crewmate = self.crew_mate_heap.extract()  
        # I have extracted Top priority crewmate 
        if crewmate.isempty is True: 
            # If crewmate has not any assigned treasure then
            crewmate.total_load = treasure.arrival_time + treasure.size 
            # its load will be at what time it will be free from it
            crewmate.isempty = False # Uodated the empty attribute
            crewmate.treasure_list_of_crewmate.append(treasure) 
            # I kept a list of treasure in crewmate assigned to that crewmate
            self.list_in_which_crewmate_have_treasure.append(crewmate) 
            # I also kept list of crewmates that have atleast one treasure
            self.crew_mate_heap.insert(crewmate) 
            # Then i am inserting it in heap of crewmates
        else:
            crewmate.total_load = max(treasure.arrival_time, crewmate.total_load) + treasure.size 
            # As explained earlier my load is defined as at what time my crewmate will be free from all treasures
            crewmate.treasure_list_of_crewmate.append(treasure) 
            # Same thing i am doing like kept a list of treasure in crewmate
            self.crew_mate_heap.insert(crewmate) 
            # And then inserted in heap
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        list = [] 
        # List of treasures storing them as object for their completion time

        # My concept is that for each crewmate i will process the treasure between two consecutive time 
        # of added trasures and in between that time i am processing treasures by maintaining a heap of treasures
        # But i am doing this only till n-1 to nth treasure
        # for nth treasure i am doing processing separately
        for crewmate in self.list_in_which_crewmate_have_treasure:
            # for each crewmate that have atleast treasure i am processing their treasure between two consecutive
            # treasure arrival times
            # if crewmate's heap has not created yet then initialise it with empty list
            if crewmate.treasure_heap_for_process is None:
                crewmate.treasure_heap_for_process = heap.Heap(self.comparison_treasure,[])
            # I am traversing from 1st to 2nd, 2nd to 3rd, ..... till last treasure's arrival time
            for i in range(len(crewmate.treasure_list_of_crewmate)-1):
                previous_time = crewmate.treasure_list_of_crewmate[i].arrival_time
                current_time = crewmate.treasure_list_of_crewmate[i+1].arrival_time
                # Previous and current times are timestamp between two consecutive treasures
                # I am making a copy of treasure for inserting it in heap for processing 
                temp =  crewmate.treasure_list_of_crewmate[i].copy()
                crewmate.treasure_heap_for_process.insert(temp)
                # I will keep processing till when treasure heap becoms empty or i reach current time
                while (len(crewmate.treasure_heap_for_process.heap)!=0):
                    # Base case for loop break when i reach the current time
                    if previous_time>=current_time:
                        break
                    # If I have the required time to process completely a treasure of maximum priority then i will completely process it
                    if previous_time + crewmate.treasure_heap_for_process.heap[0].size<=current_time:
                        time = previous_time + crewmate.treasure_heap_for_process.heap[0].size 
                        # Time is the present time when treasure process is completed
                        crewmate.treasure_heap_for_process.heap[0].completion_time = time
                        # I am updating the completion time to current time
                        crewmate.treasure_heap_for_process.heap[0].size = 0
                        # making its size zero
                        list.append(crewmate.treasure_heap_for_process.extract())
                        # and appending it in list which contains processed treasures and removing it from treasure heap
                        previous_time = time
                        # Updating the previous time
                        # The below condition is to increase previous time to next treasures arrival time if arrival time
                        # of next treasure is greater than current time
                        if crewmate.treasure_heap_for_process.size()>0 and crewmate.treasure_heap_for_process.heap[0].arrival_time>previous_time:
                            previous_time = crewmate.treasure_heap_for_process.heap[0].arrival_time
                    else:
                        # This else condition is executed when a treasure is somewhat processed but not completely
                        crewmate.treasure_heap_for_process.heap[0].size-=(current_time-previous_time)
                        crewmate.treasure_heap_for_process.rebalance(0)
                        previous_time = current_time

        # In this I am doing processing of treasures for each crewmate after the time their last treasure has arrived
        for crewmate in self.list_in_which_crewmate_have_treasure:
            # Now for all crewmates that have remaining treasure I have to process it after last treasure's arrival time
            # Initialising heap if it is not initialised
            if crewmate.treasure_heap_for_process is None:
                crewmate.treasure_heap_for_process = heap.Heap(self.comparison_treasure,[])
            # If heap contains some treasure then below code will be executed for processing it
            if len(crewmate.treasure_list_of_crewmate)!=0:
                temp = crewmate.treasure_list_of_crewmate[-1].copy()
                # I am making copy of treasure that is not inserted in the heap yet and then inserting it
                crewmate.treasure_heap_for_process.insert(temp)
                # Current time is the last treasure's arrival time
                current_time = crewmate.treasure_list_of_crewmate[-1].arrival_time
                # Process till all the treasures are not processed
                while (len(crewmate.treasure_heap_for_process.heap)!=0):
                    # Calculate the completion time of that treasure
                    time = current_time + crewmate.treasure_heap_for_process.heap[0].size
                    # Update the completion time
                    crewmate.treasure_heap_for_process.heap[0].completion_time = time
                    # Update the remaining size
                    crewmate.treasure_heap_for_process.heap[0].size = 0
                    # Append the processed treasure
                    list.append(crewmate.treasure_heap_for_process.extract())
                    # Update the current time
                    current_time = time
                     # The below condition is to increase current time to next treasures arrival time if arrival time
                    # of next treasure is greater than current time
                    if crewmate.treasure_heap_for_process.size()>0 and crewmate.treasure_heap_for_process.heap[0].arrival_time>current_time:
                        current_time = crewmate.treasure_heap_for_process.heap[0].arrival_time
        # sort the list based on treasure id
        sorted_array = sorted(list, key=lambda x: x.id)
        return sorted_array
    
    # You can add more methods if required
    def comparison_for_crewmate(self,crewmate1,crewmate2):
        # Comparison function of heap of crewmates based on their total_load
        return crewmate1.total_load < crewmate2.total_load

    def comparison_treasure(self,treasure1,treasure2):
        # Since as explained in piazza, i made a minimum heap of treasure by minimizing negative of priority
        # Here size is the remaining size of treasure
        # first priority is given according to the pdf document formula (there is no use of current time)
        p1 = treasure1.arrival_time + treasure1.size 
        p2 = treasure2.arrival_time + treasure2.size
        if p1<p2:
            return True
        # If two treasure have same priority then process that treasure which has least id
        elif p1==p2:
            return treasure1.id < treasure2.id
        else:
            return False