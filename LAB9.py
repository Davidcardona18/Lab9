#DAVID CARDONA
# NOVEMBER 22, 2024

from typing import List, Optional


def problem1():
    # Infinite while loop
    while True:
        print("Infinite loop")


def problem2():
    """
    Using a while loop, create a list called L that contains the numbers 0 to 10.
    On each iteration, the loop should append the current value of a counter variable to the list
    and then increase the counter by 1. The while loop should stop once the counter variable
    is greater than 10.
    """
    L = []
    counter = 0
    while counter <= 10:
        L.append(counter)
        counter += 1
    print(L)  # Confirm the list results


def problem3():
    """
    Using a while loop, ask the user to enter a number. Append each entered number
    to a list and add them together. Continue asking for a number until the sum of the list of
    numbers is greater than 100.
    """
    numbers = []
    total_sum = 0
    while total_sum <= 100:
        number = int(input("Enter a number: "))
        numbers.append(number)
        total_sum += number
    print(f"Numbers entered: {numbers}")
    print(f"Total sum: {total_sum}")


def problem4():
    """
    Create a while loop that initializes a counter at 0 and will run until the counter
    reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
    Confirm the list results using a print statement.
    """
    tens = []
    counter = 0
    while counter <= 50:
        if counter % 10 == 0:
            tens.append(counter)
        counter += 1
    print(tens)  # Confirm the list results


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isMirror(root: Optional[TreeNode]) -> bool:
    """
    Check if the binary tree is a mirror of itself.
    A tree is symmetric if it is a mirror of itself, return True if it is.
    """
    def is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)

    return is_symmetric(root.left, root.right) if root else True


def findRelativeRanks(score: List[int]) -> List[str]:
    """
    Assign ranks to athletes based on their scores.
    Scores are ranked in descending order, with the top three being awarded medals.
    """
    sorted_scores = sorted(((s, i) for i, s in enumerate(score)), reverse=True)
    ranks = [""] * len(score)
    for rank, (s, i) in enumerate(sorted_scores):
        if rank == 0:
            ranks[i] = "Gold Medal"
        elif rank == 1:
            ranks[i] = "Silver Medal"
        elif rank == 2:
            ranks[i] = "Bronze Medal"
        else:
            ranks[i] = str(rank + 1)
    return ranks


if __name__ == "__main__":
    print("Running Problem 1 (Infinite Loop - Disabled to prevent freezing)")
    # Uncomment the following line to test Problem 1
    # problem1()

    print("\nRunning Problem 2 (List of numbers from 0 to 10)")
    problem2()

    print("\nRunning Problem 3 (Sum numbers until greater than 100)")
    problem3()

    print("\nRunning Problem 4 (Multiples of 10 up to 50)")
    problem4()

    print("\nTesting isMirror (Binary Tree Symmetry Check)")
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    print(f"Is symmetric: {isMirror(root)}")

    print("\nTesting findRelativeRanks (Athlete Rankings)")
    scores = [10, 3, 8, 9, 4]
    print(f"Relative Ranks: {findRelativeRanks(scores)}")
