'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.comparison_function = comparison_function
        self.heap = []
        # Initialise the heap using bottom up approach
        if len(init_array)>0 :
            self.heap = [None for i in range(len(init_array))]
            self.height = self.find_height(len(init_array))
            # The initialise heap function will initialise the heap based on comparison function using botttom up approach
            self.initialise_heap(init_array)

    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.heap.append(value)
        # Append the value in the heap
        child_index = self.size()-1
        # Get the index where it is added 
        parent_index = (child_index-1)//2
        # Calculate its parent's index
        # Bubble up it till it has lower weight then its parent
        while parent_index>=0 and self.comparison_function(self.heap[child_index],self.heap[parent_index]):
            self.heap[child_index],self.heap[parent_index] = self.heap[parent_index],self.heap[child_index]
            child_index = parent_index
            parent_index = (child_index-1)//2

    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        right_most_index = self.size()-1
        top_value = None
        # If heap is not empty then delete its top element by replacing it with right most child and delete the right most child
        if right_most_index>=0:
            top_value = self.heap[0]
            self.heap[0],self.heap[right_most_index] = self.heap[right_most_index],self.heap[0]
            self.heap.pop()
            # Rebalance the heap property means bubble down that element
            self.rebalance(0)
        return top_value
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        # Function returning top element of heap if it is non empty
        return self.heap[0] if self.size()>0 else None
    
    # You can add more functions if you want to

    def size(self):
        # function for size calculation of heap
        return len(self.heap)
    
    def find_height(self,size):
        # Function for height calcultion of heap
        height = 0
        while size!=0:
            height = height+1
            size = size//2
        return height-1
    
    def initialise_heap(self,init_array):
        # This function will initialise the heap using bottom up heap construction 
        height = self.height
        # Calulate the height and assign values to the leaf nodes
        for i in range(pow(2,height)-1,self.size()):
            self.heap[i] = init_array[i]
        height = height-1
        while height>=0:
            for i in range(pow(2,height)-1,pow(2,height+1)-1):
                # now plug element height wise and then bubble down them if possible
                self.heap[i] = init_array[i]
                self.rebalance(i)
            height = height-1

    def rebalance(self,index):
        # Rebalance the heap means bubble down the element if possible  
        if self.size()>2*index + 1:
                parent_index = index
                if self.size()>2*index+2:
                    child_index = 2*index + 1 if self.comparison_function(self.heap[2*index + 1],self.heap[2*index + 2]) else 2*index + 2
                else:
                    child_index = 2*index + 1
                while child_index<self.size() and self.comparison_function(self.heap[child_index],self.heap[parent_index]):
                    self.heap[child_index],self.heap[parent_index] = self.heap[parent_index],self.heap[child_index]
                    parent_index = child_index
                    if self.size()> 2*parent_index + 2:
                        child_index = (2*parent_index+1) if self.comparison_function(self.heap[2*parent_index + 1],self.heap[2*parent_index + 2]) else (2*parent_index +2)
                    else:
                        child_index = 2*parent_index+1