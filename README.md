# AoC2023
my work on advent of code in 2023

## Day 1
Harder than I expected / remembered from last year.

Probably also because I thought I'd try C++ and I don't really know it...

## Day 2
Easier than yesterday, I thought, although I had no idea how to parse the input in C++.

Instead of trying to figure it out directly, I first wrote the code in Python
and then asked Copilot to help me translate it in C++. Is that a good way to
learn?

## Day 3
Today went alright except for the fact that after writing the function for part
2 I forgot to change the main so that it actually calls part 2 so I kept
getting the wrong answer...
Oh and I did it in Python, I guess I'm already giving up on C++...

## Day 4
My fastest day so far, by far! I was blocked once because I tried to re-use the function I wrote for part 1 in part 2 but forgot that that function does not give me the number I want but 2^ the number I want. 
And also I re-learned today that `sum(d)` when `d` is a dict gives you the sum of the dictionary keys, not the values! 

## Day 5
Got part 1 pretty quickly and part 2 took a while: I thought I'd written enough unit tests but apparently not... Interval intersection and subtraction is tricky.

## Day 6
Finally a day where things went smooth and where my implementation of part 1 just worked for part 2.
Since I was done quickly I thought I'd try translating into C++, this time
without Copilot. Tricky things: 
  * types: need to use `long long int` instead of `int` everywhere because the numbers
    are too big otherwise, and `double` for the calculation with floating point
    numbers.
  * parsing is so much harder than the simple `split` and range one-liners in
    Python.
