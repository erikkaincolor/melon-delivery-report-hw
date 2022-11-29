
def org_file_content(filename):
    """organize files...by opening them/creating an object, 
    striping them of white space, and delimiting them by "|" 
    and putting each line into list"""
    the_file = open(filename) # Create a file object from the string passed in as path
    #^^^^is associated with line 17: "the_file.close()"

    for line in the_file:
        line = line.rstrip() # Remove extra whitespace to the right of the line
        words = line.split('|') # Create a list of strings

        melon = words[0] # Assign a meaningful variable name to each item from the words list
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close() #The close() method closes an open file.
# You should always close your files in some cases, 
# due to buffering, changes made to a file may not 
# show until you close the file


#script starts here:
print("\nDay 1\n")
filename = "um-deliveries-day-1.txt"
org_file_content(filename)

print("\nDay 2\n")
filename = "um-deliveries-day-2.txt"
org_file_content(filename)

print("\nDay 3\n")
filename = "um-deliveries-day-3.txt"
org_file_content(filename)

