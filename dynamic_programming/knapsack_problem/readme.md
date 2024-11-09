# Knapsack problem statement
You’re in charge of selecting a football (soccer) team from a large pool of players. Each player has a cost, and a rating. You have a limited budget. What is the highest total rating of a team that fits within your budget. Assume that there’s no minimum or maximum team size.

## General problem statement
Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w.

## input
1. `weights`: a list of numbers containing weights
2. `profits`: a list of numbers containing profits (same length as weights)
3. `capacity`: the maximum weight allowed

## output
1. `max_profit`: maximum profit that can be obtained by selected elements of total weight no more than `capacity`

## test cases
1. some generic test cases
2. all the elements can be included
3. none of these elements can be included
4. only one of elements can be included
5. ***you don't use the complete capacity***

## Big-o notation complexity
`O(2^n)` exponential complexity because there are many possibilities for computing various things repeatedly, as we create many subproblems.


## used concepts to resolve this problem in Python
1. recursion
2. memorization
