class LinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [None] * 1543
        

    def add(self, key: int) -> None:
        hashedVal = self.hashValue(key)
        keyNode = LinkedList(key)
        if self.array[hashedVal] == None:            
            self.array[hashedVal] = keyNode
        else:
            if self.contains(key):
                return
            before = self.array[hashedVal]            
            keyNode.next = before
            self.array[hashedVal] = keyNode

    def remove(self, key: int) -> None:
        hashedVal = self.hashValue(key)
        head = self.array[hashedVal]
        prev = None
        
        if head == None:
            return 
        if head.val == key:
            self.array[hashedVal] = head.next
        else:            
            while(head != None and head.val != key):                
                prev = head
                head = head.next 
        
        if prev != None and head != None:
            prev.next = head.next            
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashedVal = self.hashValue(key)
        head = self.array[hashedVal]        
        while(head != None):            
            if head.val == key:
                return True
            head = head.next
        return False
    
    def hashValue(self,key):
        return key % 1543
