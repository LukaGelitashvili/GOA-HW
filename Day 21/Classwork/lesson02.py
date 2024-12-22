# Existing queue
queue = ['John', 'Amy', 'Bob', 'Adam']  

# Prompt the user for input to add a new person to the queue
new_person = input("Enter the name of the new person: ")  
# If the user inputs "Emily", new_person will hold the value "Emily"

# Add the new person to the end of the queue using the append() method
queue.append(new_person)  
# The queue now includes the new person at the end. For example: ['John', 'Amy', 'Bob', 'Adam', 'Emily']

# Output the updated queue
print(queue)  
# This will display the updated list with the new person added


# Output:
# ['John', 'Amy', 'Bob', 'Adam', 'Emily']
