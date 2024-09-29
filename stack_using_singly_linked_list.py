class Linked_stack:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element,next):
            self._element = element
            self._next = next
    def __init__(self):
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def __isEmpty__(self):
        return self._size == 0
    
    def push(self,e):
        
        newest = self._Node(e,self._tail)
        self._tail = newest
        self._size = self._size + 1
    
    def pop(self):
        delEl = self._tail._element
        self._tail=self._tail._next 
        return delEl
    
    def display(self):
        while(self._tail != None):
            print(self._tail._element)
            self._tail=self._tail._next 
            
        
        
        
        
        
    
        
        
            
        