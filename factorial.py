#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: April 29th, 2025
# This program calculates the factorial starting from 1
# to the user's input and displays them.


def main():
    # get user number from user as a string
    user_number_string = input("Enter a whole number: ")

    try:
        user_num = int(user_number_string)
        counter = 0
        factorial = 1

        while user_num < 0:
            print("Please enter a whole number!")
            # The coed above will be displayed while user number
            # is less than 0.
            break

        else:
            while True:
                # We are incrementing by 1 each time
                # from 0 to the user number
                counter = counter + 1
                # We get the factorial by multiplying the factorial
                # with the counter
                factorial = factorial * counter
                # if counter is less than or equal to user_num
                # the loop will break
                if counter > user_num:
                    break
            # The user_num will be displayed with it's factorial
            print(f"{user_num}! = {factorial}")

    except ValueError:
        print("invalid number")

    finally:
        print("Thank you")


if __name__ == "__main__":
    main()
