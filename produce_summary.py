print("\nDay 1\n")
the_file = open("um-deliveries-day-1.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("\nDay 2\n")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("\nDay 3\n")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
