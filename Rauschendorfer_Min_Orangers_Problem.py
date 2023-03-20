"""
Denise Rauschendorfer
CSI5610: Project 2 - Hard Level
3/17/2023

Minimum Number of Days to Eat n Oranges
"""


"""Checking functional arguments:
        Condition 1. 1 <= n <= 2 * 10^9
"""
def areFunctionConditionsMet(n):
    if 1 > n or n > 2 * pow(10, 9):
        print("Orange Amount Error: The initial amount of oranges n (", n, ") is not valid.")
        return False
    else:
        return True

""" Minimum Number of Days to Eat n Oranges Solution """
class Solution(object):
    def minDays(self, n):
        """checking the function constrains"""
        if areFunctionConditionsMet(n) == False:
            return None

        """Because we go through the BFS tree one layer at a time, if a value is visited multiple times either:
                1. The path taken to reach the already known value is determined not to be the fasted route
                2. At least two different paths can reach that value at the same layer, and therefore took 
                    the same number of days.
            Anytime q[0][0] == 1 (q[0][0] will never = 0 before q[0][0] = 1) a minimum path has been found. 
            Another minimum path may also exist in the same layer, however, it will take the same number of days 
            to eat the oranges"""
        visited_values = set()
        q = [[n, 0]]
        while q[0][0] != 1:
            if q[0][0] not in visited_values:
                # Case 1: eat one orange
                case1 = q[0][0] - 1
                days = q[0][1] + 1
                q.append([case1, days])

                # Case 2: eat n/2 oranges
                if q[0][0] % 2 == 0:
                    case2 = q[0][0] / 2
                    q.append([case2, days])

                # Case 3: eat 2(n/3) oranges
                if q[0][0] % 3 == 0:
                    case3 = q[0][0] / 3
                    q.append([case3, days])

                # q[0][0] is added to the set of visited_values
                visited_values.add(q[0][0])

            # remove this value from the list
            q.pop(0)

        """No matter what path we use to eat oranges, we will also end up with 1 orange left, 
            that will always take 1 day to eat."""
        min_days = q[0][1] + 1
        return min_days


