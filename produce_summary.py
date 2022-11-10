# Define a function that accepts two arguments and prints the result of the filename from the second argument
def summary_report(day, filename):

    # Print the day of which we are displaying the results (argument 1)
    print(day)

    # Open the file which we are going through (argument 2)
    the_file = open(filename)

    # Loop through each line of the file, tokenize the line and print the desired output
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        melon = words[0]
        count = words[1]
        amount = words[2]
        print(f"Delivered {count} {melon}s for total of ${amount}")

    # Close the file before exiting the function
    the_file.close()


# Call the function with the three different files as arguments
summary_report("Day 1", "um-deliveries-day-1.txt")
summary_report("Day 2", "um-deliveries-day-2.txt")
summary_report("Day 3", "um-deliveries-day-3.txt")
