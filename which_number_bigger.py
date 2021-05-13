#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program shows which is bigger or smaller
#    with number inputted from the user

import math


def main():
    # This function shows which is bigger or smaller

    # input
    print("This program finds the larger and smaller of two numbers")
    print("")
    first_string = input("Enter the first number: ")
    second_string = input("Enter the second number: ")
    print("")

    # process/# output
    try:
        first = int(first_string)
        second = int(second_string)
        if first < second:
            print("{} is smaller than {}".format(first, second))
        elif first > second:
            print("{} is bigger than {}".format(first, second))
        elif first == second:
            print("{} is equal to {}".format(first, second))
        else:
            print("Not an integer")
    except Exception:
        print("{} is not an number".format(first_string))
    except Exception:
        print("{} is not an number".format(second_string))
    finally:
        print("Thanks for trying")
    print("\nDone.")


if __name__ == "__main__":
    main()
