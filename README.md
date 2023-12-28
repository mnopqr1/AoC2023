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

## Day 7
Reasonably happy with how today went. The rules for the game are a bit simpler to implement than actual poker. 
* I first considered classes and `__lt__` but didn't remember how it worked and worried that objects & classes in Python might be too slow.
* I had a funny bug in part 2 that took me a while to figure out: in order to evaluate a hand containing one or more J's, I was taking the maximum score over all possible replacements for J by one of the other cards that is already present in the hand, thinking that you never need to try any cards that are not already in the hand since they won't help improve the score. That's true, except for one case: the hand "JJJJJ", where you actually _do_ want to try replacing "J" by "A", even if "A" is not already in the hand! I figured it out by print-debugging and finding "JJJJJ" at the very bottom of te sorted list, instead of at the top...

## Day 8

I got part 2 a little haphazardly. After some testing I realized that you only ever end up in a Z node by reading the entire instruction list (of length 307 in my case). So we don't care what happens in the middle, we only care what happens after reading the entire list of instructions once (a "big step"). There were only 6 A nodes in the input and they took about 60 "big steps" each. So then we can just take the least common multiple of these numbers, and multiply it by 307.
I always find it a bit unsatisfying when a special property of the inputs makes the whole problem much easier. I would like to know what the complexity would have been if we had a completely random input.

## Day 9

This was definitely easier than yesterday even though I wasn't fully awake today and I was thinking that I needed to do something smart with arithmetic sequences or quadratic increments. But I didn't. Also I think this was the smallest difficulty increase from part 1 to part 2 that I've seen so far.

## Day 10

Part 1 was OK, and this was the first day where I really struggled with Part 2, for several hours.
I first missed "In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed!"
My approach for Part 2: 
1. read the file and calculate `neighbors` for each node in the grid
2. calculate where the loop is (in a better way than I did for part 1): 
  * begin at the startnode, `curr = startnode`, `prev = None`
  * choose a neighbor of the current node that you did not just visit
  * update `prev` and `curr`
3. find the pipe that fits at the `startnode` and pretend from now on that it is that pipe.
   clean everything up in the `loopgrid`: no more loose pipes.
4. to deal with the paths that "squeeze between pipes", "zoom in" on the grid: create a `biggrid`
   that has an extra cell between every two cells of the original grid, and a border around it
5. "interpolate" by connecting the pipes in the loop to this bigger grid, and keep the original `.` symbols
6. starting from the outer border, mark as many cells as possible as "outside", and then count how many `.` were left unmarked: these must be inside the loop.
The code is not super-organized and there are hardly any functions but I've worked on this long enough for today...

## Day 11

This one was alright.

## Day 12

I struggled. Brute force approach in part 1 did not work at all in part 2, went down a lot of useless paths yesterday, eventually watched Jonathan Paulson's youtube to get the idea of how to apply dynamic programming in this problem. Then a *lot* of print debugging this morning.

## Day 13

Comparatively much easier for me than yesterday's puzzle. 
Try all possible mirror-rows and return as soon as you find one.
For part 2, allow for exactly one error in the diff, once per mirror-check. 
If nothing was found yet, do the same for columns.

## Day 14

This was alright, I read off the answer from part 2 from a raw text output first, noticing there were loops. Then wrote a little code to simulate that.

## Day 15

I found today to be satisfying; putting things in boxes. I woke up so early (5:50am) that I could see the new day "appear", that was exciting. May take a nap later.

## Day 16

My main idea was that as soon as a beam comes into a node with a direction that has already happened 
we can stop tracking it. I was worried that I would need to be more efficient in part 2. You could 
memoize a beam's trajectory and as soon as you enter the same trajectory, just recall from memory
what happened. But it turned out that wasn't needed.

## Day 17

After struggling with part 1 for a few hours I decided I didn't want to spend my entire Sunday
on this (especially because it's finally nice and sunny again here in Paris) so I watched
[Jonathan Paulson solve part 1](https://www.youtube.com/watch?v=jcZw1jRkUDE). I was happy to see he went more or less through the same
thought process as I did (just at approximately 20x speed). Then he pulled `heapq` out of a
hat and I'm still not entirely sure why that works, but with that clue I solved part 1, and 
then was also able to do part 2 "on my own" after a few more smaller struggles.
Another reminder that I would like to understand the ins and outs of heaps better.
I also learned a Python print debugging trick from Jonathan Paulson: `print(f"{x=}{y=}")` 
prints out something like `x=5 y=6` which is useful when you have a lot of different variables.

## Day 18

Didn't have much time and struggled with part 1... 

## Day 19

Got part 1 pretty quickly and then had to go to work, thought a bit about part 2 during
the day and got back to writing some code in the evening. I figured that you could work from the "bottom up", meaning first find out what is the range of inputs accepted by lines that only have A's and R's, then figure out that same thing for instructions that have A's, R's, and things already treated previously. To evaluate a single line, I iterate through the list of tests in order and keep track of what range could remain. It was nice and a bit surprising that this just.. worked.

## Day 20

Got something almost working for part 1 in the morning but had to leave for work.
Then got part 1 pretty quickly in the afternoon.
A little bit of objects and classes was helpful to me for this problem.
For part 2 when reading it I first thought "this can't be that hard",
famous last words, until I realized that `rx`  requires four inputs to 
be high at exactly the same time.
I printed out the times when these four inputs are high, and, as I hoped, it happens 
cyclically, and even for each of them the first time they are high is after a prime number
of button presses. This means the first time all of them will be high is after the product
of these four prime numbers, which is a gigantic number of button presses.

## Day 25

I struggled and then saw that people online used the `networkx` library.
But I wanted to do it without a library.
I read about "max flow min cut" for a while but thought it was too complicated.
Then I found [this paper](https://dl.acm.org/doi/10.1145/263867.263872) that explains
in a fairly readable way how to find a min cut.
It took me a while to get to an implementation that was both not too slow and not wrong.
But I learned something!
And I am "just" missing 7 stars (holidays made me spend less time on this 
over the last few days).

## Day 18 (on day 26)
Got part 1 on the actual 18th, then left part 2 until now.
Lowest line-of-code per time-spent-on-this ratio yet.
Eventually found a way to do it at [this Stackoverflow answer](https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon) and then experimented with the test input to see how much of the perimeter I needed to add.
Felt hacky and maybe I want to get back to this at some point to at least understand how it works...

## Day 22 (on day 27)
This took me a few hours. 
Nothing super hard, it was just complicated to keep track of all the different moving parts,
and hard to debug because of the 3D.
I first implemented bricks as tuples and the grid as a global variable, but then decided to be a bit more structured and make use of classes and objects which I think was helpful.

## Day 24 (on day 28)
I solved part 1 on the 24th itself and then sat on my family's couch thinking about part 2 for a looong time. I eventually looked on reddit and also saw athat the solutions separate largely into two groups, sat-solving or linear algebra.
since linear algebra is an old love of mine, I thought this afternoon I should try to understand that solution and I did, but only by a very close reading of [one particularly elegant-looking Reddit solution](https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kersplf/) which I essentially just re-implemented once I felt like I more or less understood it. Will write some details about my understanding below.

Here is my understanding of [that solution on Reddit](https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kersplf/).

We only use the first three stones to find the velocity and position from where we want to throw.
The trajectory of each of these stones is specified by two 3d-vectors, (p1,v1), (p2,v2), (p3,v3)
The key idea is that the velocity vector that we're looking for (I call it **w**) needs to be a vector in three different planes.
But there is only one such vector! 
That gives the velocity and then the starting position you need to throw from (I call it **p**) will be deduced from that.

Now, how do you find these three planes? 
They come from comparing the three pairs of stones: (1,2), (1,3), and (2,3).
Each comparison will give you a plane.
Focus on the first and second stone. 
Imagine you can throw from some place **p** with velocity **w** and hit both of these stones.
That means there are some moments in time **t1** and **t2** where you hit stone 1 and 2, respectively.
This gives equations 

**p** + t1**w** = p1 + t1 v1

**p** + t2**w** = p2 + t2 v2

Bringing the **w** terms over to the other side, both are equal to **p**, so that

p1 + t1 (v1 - **w**) = p2 + t2 (v2 - **w**)

For **w** to satisfy such a linear equation, it must lie in a certain plane specified by p1, p2, v1, v2.
You can compute precisely which plane using some cross product magic.
Now do that for the first and third stone and second and third stone as well. 
This gives three planes, which you can intersect with each other using again some cross product magic.
Finally, to find the starting position **p** you solve the equation

p1 + t1 (v1 - **w**) = p2 + t2 (v2 - **w**)

which is possible now since you know p1, v1, p2, v2, and also **w**.