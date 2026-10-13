"""
Lab: Dice Roll Evaluation

Name: Josef Magallon

Instructions:
1) Complete the DESIGN section first.
2) Write your test cases.
3) Then implement the functions.
4) Run the program and compare your results.
5) Complete the extensions.
"""

# ------------------------------------------------------------
# TASK 1: DESIGN (Answer BEFORE coding)
# ------------------------------------------------------------

# 1) What is the responsibility of your main dice evaluation function?
DESIGN_Q1 = """
YOUR ANSWER: The main responsibility of the main dice evaluation
is to define the range of categories for the numbers 1 - 6

"""

# 2) What input does the function need? What data type?
DESIGN_Q2 = """
YOUR ANSWER: The input function needs a random number from 1-6 and the
data type is an integer

"""

# 3) What should the function return? Why?
DESIGN_Q3 = """
YOUR ANSWER: The function should return you a random number from 1-6 since
a dice has 6 sides ranging from 1-6

"""

# 4) Write the decision logic in words:
DESIGN_Q4 = """
If the roll is 1, 2, or 3: Low roll
If the roll is 4 or 5: High roll
If the roll is 6: Lucky roll
"""


# ------------------------------------------------------------
# TASK 2: TEST PLAN (Write BEFORE coding)
# ------------------------------------------------------------

# Write at least 4 test cases.
# Each test case must include:
# - input
# - expected output
# - why

# Test Case 1:
# input = 1 
# expected = low roll
# why = 1 is in the category for a low number

# Test Case 2:
# input = 4
# expected = high roll
# why = 4 is in the catgory for a high number

# Test Case 3:
# input = 6
# expected = lucky roll
# why = 6 is in the catgory for a lucky number

# Test Case 4:
# input = 8
# expected = invalid roll
# why = 8 is outside the range from 1-6 for a random dice roll


# ------------------------------------------------------------
# TASK 3: CODE (Write AFTER design + test plan)
# ------------------------------------------------------------


def dice_roll(num: int) -> str:
    if num >= 1 and num <= 3:
        return "Low Roll"
    elif num >= 4 and num <= 5:
        return "High Roll"
    elif num == 6:
        return "Lucky Roll"
    else:
        return "Invalid Roll"

    # TODO: Replace pass with your decision logic
        """
        Input: Random number from 1-6
        Process: Calculate a random number from 1-6
        Output: return Low roll, High roll or lucky roll depending on the number
        """

# ------------------------------------------------------------
# Task 5: RANDOM DICE ROLL
# ------------------------------------------------------------
import random
# TODO: Import the random module above this section

def roll_die() -> int:
    roll = random.randint(1,6)
    return roll


    # TODO: Use random.randint() to generate and return a value
    pass


# ------------------------------------------------------------
# TASK 4: RUN YOUR TESTS
# ------------------------------------------------------------

if __name__ == "__main__":

    #Test cases from test plan

    print(dice_roll(1)) # Expected Low Roll
    print(dice_roll(4)) # Expected High Rol
    print(dice_roll(6)) # Expected Lucky Roll
    print(dice_roll(7)) # Expected Invalid Roll

    #random roll

    roll = roll_die()
    print("You rolled:", roll)
    print(dice_roll(roll))


    # call dice_roll with your test cases
    # print(dice_roll(#))  # Expected: ...
    pass
