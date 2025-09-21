# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top # Point to the old top
        self.top=new_node #puts the new node on top, first to come off 

    def pop(self):
        if  not self.top:
            return None #returns none if there's nothing in the top node
        removed_node=self.top #stores current node to be removed
        self.top=self.top.next #updates the stack, second node becomes new | node under old top
        return removed_node.value #returns data| remmoved value because it was stored in removed_node

    def peek(self):
        if self.top:
            return self.top.value #This returns data on top if top is not empty 
        else:
            return None #returns none if empty
    
    def print_stack(self):
        current=self.top #an instance/object to the data on top
        if not current:
            print("Stack is empty")
            return
        while current:
            print(f"-{current.value}") #while current is not empty, current prints
            current=current.next #current/top moves down to print data below

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack=Stack()
    redo_stack=Stack()
    

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action) #add new action to undo stack
            redo_stack.top=None  # resetting redo history by simply dropping its top reference

            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()
            if action is None: #if there is nothing in undo stack
                print("No actions to undo.")      # message when stack is empty
            else:
                redo_stack.push(action)
                print(f"Undid action: {action}")

            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            
            action = redo_stack.pop()
            if action is None:
                print("No actions to undo.")
            else:
                undo_stack.push(action)
                print(f"Redid action: {action}")



        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()