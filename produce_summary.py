def summary_report(day):
    while 1:

        user_input = input('what day do you want to look up? ')

        if user_input == "Day1":
            print("Day 1")
            the_file = open("um-deliveries-day-1.txt")
        elif user_input == "Day2":
            print("Day 2")
            the_file = open("um-deliveries-day-2.txt")
        elif user_input == "Day3":
            print("Day 3")
            the_file = open("um-deliveries-day-3.txt")

        for line in the_file:
            line = line.rstrip()
            words = line.split(' ')
            melon = words[0]
            count = words[0]
            amount = words[0]

        print(f"Delivered {count} {melon}s for total of ${amount}")
        the_file.close()

    return (day)


day = "Day1"
bucket = summary_report(day)


# print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]
