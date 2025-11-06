class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data) # creates/sets the data as a NODE
        if self.head: # checks if self.head has a value
            new_node.next = self.head # if self.head has a value, then the previous node will be the node after the new node
            self.head = new_node # sets the new node as the head
        else: # if self.head is EMPTY
            self.tail = new_node  
            self.head = new_node # then new node is set as the head & tail (happens only once when you are first applying the FIRST node)

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node # if self.head has a value, then the previous tail will get a "next" which is the new node
            self.tail = new_node # sets the new node as the tail
        else:
            self.head = new_node 
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node: # while loop ends when data is found
            if current_node.data == data:
                return True
            else: 
                current_node = current_node.next # moves through the linked list til data is found
        return False
    
    def remove_beginning(self): # this will return the data that was removed at the beginning
        if self.head is None: # checks if linked list has nodes. If none, then do nothing
            return None
        
        removed_data = self.head.data # sets removed_data as the head's data
        self.head = self.head.next # sets the head as the next node
        return removed_data

    def remove_at_end(self): # this will return the data that was removed at the end
        if self.head is None:
            return None
        
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        
        current_node = self.head # Start at the head
        while current_node.next != self.tail: # the while loop will set the current_node to the node before the tail
            current_node = current_node.next

        removed_data = self.tail.data 
        self.tail = current_node
        self.tail.next = None
        return removed_data
            
    def remove_at(self, data): # this will return the data that was removed else return null if data not found // removes the argument data in the list if found, else return none
        if self.head is None:             
            return None
        
        if self.head.data == data: 
            return self.remove_beginning() # calls remove_beginning function
        
        current_node = self.head
        while current_node.next is not None: # goes through the list
            if current_node.next.data == data: # if current node data matches data then
                removed_data = current_node.next.data # save the data as removed_data

                if current_node.next == self.tail: 
                    self.tail = current_node
                    current_node.next = None # if the NEXT current node is the tail, then the current node will be the tail
                else:
                    current_node.next = current_node.next.next # else remove the current node's next node to the next NEXT node ("removes" the wanted node)
                return removed_data
            current_node = current_node.next
        return None 
        
    def get_linkedlist(self): 
        current_node = self.head 
        list = []
        while current_node: # goes through the entire list
            list.append(current_node.data) # appends the current node to the list
            current_node = current_node.next # moves to the next node
        return list

burger = LinkedList()
# Supreme Burger Recipe
burger.insert_at_beginning("Top Bun")
burger.insert_at_end("Lettuce")
burger.insert_at_end("Tomato")
burger.insert_at_end("Cheese")
burger.insert_at_end("Patty")
burger.insert_at_end("Pickles")
burger.insert_at_end("Bottom Bun")
print(f"Supreme Burger Recipe: {burger.get_linkedlist()}")

#Customer order: No Lettuce No Cheese
burger.remove_at("Lettuce")
burger.remove_at("Cheese")
print(f"Customer's Order: {burger.get_linkedlist()}")

# Changed order: Remove the two buns
burger.remove_beginning()
burger.remove_at_end()
print(f"Revised Customer's Order: {burger.get_linkedlist()}")

