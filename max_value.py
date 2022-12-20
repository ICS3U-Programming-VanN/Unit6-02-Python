#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: December 15, 2022
# This program generates 10 random numbers from
# 0-100 and then finds and displays the highest/max
# number of all of them


import random

import constants


# This function finds and returns the max value of an array
def find_max_value(random_integers_list):
    # Declared Variable
    highest_number = 0

    # Goes through each index of the list to determine the highest number
    for index in range(constants.MAX_LIST_SIZE):
        # Checks if the index of the list is higher than the placeholder value for the highest number
        if random_integers_list[index] > highest_number:
            # Assigns the placeholder variable to the number in the index of the list
            highest_number = random_integers_list[index]

    # Returns the max number to function call
    return highest_number


def main():
    # Initialized List
    list_of_integers = []

    # Loops through 10 times to generate ten random numbers
    for counter in range(constants.MAX_LIST_SIZE):
        # Generates a random number from (0-100) and added it to a list
        list_of_integers.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))

        # Displays to console what number was added to the list and what position it is at
        print(f"{list_of_integers[counter]} added to the list at position {counter}")

    # Calls function to find the highest number in the list
    max_number = find_max_value(list_of_integers)


    # Displays the max number to the console
    print(f"The max value: {max_number}")


if __name__ == "__main__":
    main()
