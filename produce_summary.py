
def org_file_content(filename):
    """organize files...by opening them/creating an object, 
    striping them of white space, and delimiting them by "|" 
    and putting each line into list"""
    the_file = open(filename)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


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

