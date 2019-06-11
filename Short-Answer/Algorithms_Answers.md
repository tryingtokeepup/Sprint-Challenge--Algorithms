Add your answers to the Algorithms exercises here.

## Question 1

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

The above algorithim would have a run time of `O(n)`, as the algorithim clearly takes whatever `n` you have, multiplies it by `3`, and then
divides it by `2`. For example, for a `n` of `3`, the algorithim loops while `a` is less than `3n`, and then makes `a` the equal of `a` plus the
product of `2n`, forcing the while loop through `3n / 2n` iterations, or `n`.

Dasterdly little thing lol.

```
b)  sum = 0
    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1
```

Note: This above algorithim took so much time to analyze. Thought it was `O(n)` because I thought it was a trick question, then `O(n^4)`, and then realized it was `O(n^3)` only after a good long look at the last loop.

This algorithim runs at `O(n^3)`, with some caveats. At lower `n` values, the equation actually never reaches the lower loops, with a `n = 1` actually having a runtime of `O(n)`, `n = 2 to 3` having a run time of `O(n^2)`. At all other values, it hits the 3rd loop, becoming `O(n^3)`, and the final loop just multiplies everything by `10x`, with `x` being some constant between `0.9 and 1`. Very tricky. Removing all constants, we can say that the worst run time is `O(n^3)`.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

This is a recursive function that calls its function `n` times before reaching the base case here, `bunnies == 0`. Therefore, it has a run time of `O(n)`, our first textbook linear equation. Function `a` is also linear time, but it was a little harder to deduce than this one.

## Question 2

```
Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken
if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_.
Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.
```

Let's begin with some constraints:

We have a building with `n` floors, and we can treat this like a sorted array or just an integer.
We need to find the last `safe` floor `f`, where if we go even one floor higher, the `egg` we drop will break.
We need to make an efficent searching algorithim so we make the least amount of passes, here repesented by broken `eggs`.

So, since we can assume that this is a building that's in some sort of real gravity situation (i.e. eggs dropped from higher levels increases
the chance the `egg` breaks, and we won't have weird phenomenon like `eggs` breaking on the 3rd floor while the 4th floor is safe), it is
basically a sorted array that we are traversing through. I.e. Our building is in order.

So, we can use binary search to go through this array efficently and find that `safe` floor.

the code will look something like:

```
last_safe_floor = 0 # let's keep it at zero until we find it

def drop_egg_and_return_false_if_it_breaks(floor):
    if egg_dropped_and_it_breaks:
        return False
    if egg_dropped_and_it_doesn't_break:
        return True


For i floors in n:
    middle_check = n // 2

1) Then, check middle_check against our drop_egg function

2a) If the function returns False, as in, the egg breaks and the floor is unsafe for eggs,
then we know that our `last_safe_floor` is going to be on the lower half of the array,
and so we need to traverse the lower floors.
So, we remove the RHS of the array, and then take a new midpoint of the new, truncated array.

2b) However, if the function returns True, as in the egg is safe (yippee), we are not done yet.
We now need to go through the upper half of the array from that midpoint, so we elliminate
the LHS of the array, or the lower floors, and then take the midpoint of the
remaining array.

3) Keep doing the above until we get the `last_safe_floor`, which we `return` as our answer.

4) Celebration dance!

5) Time complexity of ... O(log n)

```
