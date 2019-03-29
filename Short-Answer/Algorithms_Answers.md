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

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
