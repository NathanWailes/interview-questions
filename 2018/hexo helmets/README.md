# Task description
*Note: This was written by Nathan Wailes to summarize the task description as given during the interview.*

1. You have a list of partially-sorted integers.
1. You know that each element is at most `k` positions away from the position it would be in if the list was completely sorted.
1. You are given `k`.
1. Write a function that takes the list of integers and `k` and returns the list completely sorted.

The code that I was provided with as an example was this:

    list = [4, 2, 1, 3, 10, 7, 8]
    k = 3

# My approach to solving the task

1. I followed my standard approach to problems like this: I would try to start with as simple a case as possible, develop a plain-English algorithm for that case, and then try to handle more-complicated cases and change my plain-English algorithm to handle the more-complicated cases.  I would then implement that final plain-English algorithm in code.
1. I switched `k` to the smallest possible value and made the example list smaller: `k=1, n=2` (`[1, 2]` and `[2, 1]`)
1. After writing out a plain-English algorithm for handling that case, I expanded to `k=2, n=3` (`[1, 2, 3]`, `[1, 3, 2]`, `[2, 3, 1]`, `[2, 1, 3]`, `[3, 1, 2]`, `[3, 2, 1]`).
1. After expanding my plain-English algorithm for `k=2`, it seemed to me that the algorithm would generalize to any `k` and any `n`, so I switched to implementing the plain-English algorithm in code.

# Additional notes

- This was for a live interview where I shared my screen and explained my thought process out-loud as I developed the solution.
- I have not changed / cleaned up the text of the solution at all, so it contains comments that I would normally remove from final code.