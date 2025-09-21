# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    def __init__(self):
        self.front=None #first node(customer) in line set to None
        self.rear=None #last node in line set to None

    def enqueue(self,customer):
        new_node=Node(customer) #new node holding customer
        if not self.front: #if queue is empty
            self.front=new_node #point front to new node
            self.rear=new_node #point rear to new node
        else: #if queue is not empty
            self.rear.next=new_node  #links the current last node to new node
            self.rear=new_node #move rear to new node
    
    def dequeue(self):
        if not self.front:
            return None #returns none if queue is empty
        removed_node=self.front
        self.front=self.front.next
        if not self.front:
            self.rear=None
        return removed_node.value

    def peek(self): #shows the next customer without removing them
        if self.front:
            return self.front.value 
        else:
            return None
        
    def print_queue(self): 
        current=self.front
        if not current:
            print("Queue is empty")
            return
        while current: #while current is not empty, current prints
            print(f"-{current.value}")
            current=current.next # Update current to next value
    


def run_help_desk():
    # Create an instance of the Queue class
    queue=Queue()


    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name=queue.dequeue()
            if name is None:
                print("No waiting customer")
            else:
                print(f"Helped: {name}")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            name=queue.peek()
            if name is None:
                print("No customers waiting")
            else:
                print(f"Next customer: {name}")
            


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()


# MEMO





# Why is a stack the right choice for undo/redo?

# Stack is the right chioce for undo/redo because it puts the most recent on top or in other words, 
# the last entry on top.  It also follows a last in first out principle, this  means we can remove 
# the last entry(undo) to return to a previous version and redo(add the removed item back on top)

# Why is a queue better suited for the help desk?
    
# Queue on the other hand follows a first in first out approach and this means the very first entry 
# is taken care of first just like how a real life queue works. This makes it better suited for the help desk.

# How do your implementations differ from Python’s built-in lists?

# My stack and queue implementations differ from Python’s built-in lists because they are built to
# handle additions and removals at specific ends without relying on list shifting. A stack made with
# custom nodes or methods clearly shows push and pop behavior, while a queue uses enqueue and
# dequeue to add and remove from the queue. Python lists can imitate a stack using append and pop, but
# removing from the front of a list moves every other element forward. By creating our own classes,
# we control how data is linked and accessed, making the purpose of each structure clearer and
# separating stack actions from queue actions.
