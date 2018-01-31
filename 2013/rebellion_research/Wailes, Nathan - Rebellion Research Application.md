# [Rebellion Research Employment Application Form](http://www.rebellionresearch.com/jobs.html)

## Basic Information [1/6]

##### First name:
Nathan

##### Last name:
Wailes

##### Email address:
_[Send your resume to [jobs@rebellionresearch.com](mailto:jobs@rebellionresearch.com) using the email address that
you list here.]_

[nathan.wailes@gmail.com](mailto:nathan.wailes@gmail.com)

([Link to my resume](https://www.dropbox.com/s/1taix0n3cmza1ld/Wailes%2C%20Nathan%20-%20Resume.doc))


## Programming [2/6]

_Consider the function below written in an unknown language. The questions below will refer to this function._

_Assume that this programming language has the following characteristics:_
1. _It uses zero based indexing of arrays (so 0 is the location of an array's first item)._
2. _The function size() is used to get the number of elements in an array_
3. _Code crashes if you access an element of an array that doesn't exist_
4. _The keyword "function" defines a new function,_
5. _In functions, it passes arrays by reference, not value._
6. _Variable types do not need to be explicitly specified, but the variable ara is an array._

```
function cyk(ara):
    i = 0
    s = ara[0]
    while i < size(ara):
        ara[i] = ara[i+1]
        i = i + 1
    if size(ara) < 1:
        ara[size(ara)-1] = s
        return ara
```

---

##### Question:
_Which of the following statements best describes the purpose of the function cyk()?_

##### Answer:
- _It reverses the elements in ara._
- **If ara has n elements, it moves the element in position 0 to position n-1, the element in position 1 to position 0, the element in
position 2 to position 1, etc.**
- _If ara has n elements, it moves the element in position n-1 to position 0, the element in position n-2 to position n-1, the element
in position n-3 to position n-2, etc._
- _If ara has n elements, it swaps the element in position 0 with the element in position n-1, swaps the element in position 1 with the
element in position n-2, etc._
- _Once it completes, the function ultimately ends up having no effect._

---

##### Question:
_If this function cyk(), implemented as above, were applied to the array ara=[1,3,2,4], what would happen?_

##### Answer:
- **The code would crash**
- _It would return []_
- _It would return [4,1,3,2]_
- _It would return [3,2,4,1]_
- _It would return [3,1,4,2]_
- _It would return [2,1,4,3]_
- _It would return [4,2,3,1]_
- _It would return [2,3,1,4]_

##### Reasoning:
The while loop's last loop will be when i is 1 less than the size of ara. Because the array's first element is accessed with 0,
that means that accessing ara[i] on that last iteration would access the **last** element in the array (think 1st-->0,
2nd-->1, so last-->length-1). And so when it attempts to access ara[i+1] on that iteration it would be attempting to access an element
of the array that doesn't exist, and the problem stipulates that that will crash the program.

---

##### Question:
_In the box below, write a function in any programming language that takes a text string as input and returns a data structure that
contains each character that appears in the string more than one time, and the number of total times that each such character appears.
Assume that this function is going to be called by code written by other programmers at our firm. Write this code as you would if this
was a real work assignment. Note: You may want to do the actual writing in a text editor or IDE and then just paste the result into the
box below._

##### Answer:
```
def repeated_chars(string):
    """takes a text string as input and returns a dictionary whose keys are the
    characters that appear in the string more than once, and whose values are
    the number of times that the characters appear"""
    import collections
    char_freq_dict = collections.defaultdict(int)  # defaults dict values to 0
    for character in string:
        char_freq_dict[character] += 1
    for key in char_freq_dict.keys():
        if char_freq_dict[key] < 2:
            del char_freq_dict[key]
    return char_freq_dict
```
---

##### Question:
_What language is the code you just wrote written in?_

##### Answer:
Python

## Multiple Choice [3/6]

##### Question:
_There are 4 shut doors in front of you. You know that each door has an animal painted on one side and a plant painted on the other
side. The four doors have the following painted on the sides that you can see (one per door): a lily, a pine tree, a fox, and an
eagle. You have been told that these doors satisfy the rule "if a door has a flower on its plant side, then it has a bird on
its animal side". What is the smallest set of doors that you must check the hidden side of to determine conclusively whether
this rule is true or false for these doors?_

##### Answer:
- _Just the door with the lily_
- _Just the door with the eagle_
- _Just the doors with the lily and the eagle_
- **Just the doors with the lily and the fox**
- _Just the doors with the lily, fox and eagle_
- _Just the doors with the pine tree and eagle_
- _All of the doors_

##### Reasoning:
If my understand is correct, logic has this rule that says that a conditional statement is only false if there's a counter-example
(or something like that). So in this case we just need to test the doors that could potentially prove the conditional false; we **don't
need to actually find an example where there is a flower and a bird (this is confusing when you first learn it). The only ways that the
conditional could be false is if the sufficient condition (flower) has been met and the necessary condition (bird) has **not** been met. So
we need to look at the doors that have an animal that isn't a bird, because if the other side has a flower then that would contradict
the rule; we also need to look at the doors that have a flower, because if the other side doesn't have a bird then that would also
contradict the rule.

---

##### Question:
_Suppose that in a group of people you find that X percent of people in the group have heights that are greater than the average (that
is, the mean) height in that group. Which of the following is a true statement about X?_

##### Answer:
- _X can be any percentage._
- _X cannot be bigger than 25%._
- _X can be bigger than 25% but cannot be bigger than 50%._
- _X can be bigger than 50% but cannot be as high as 99.9%._
- **X can be bigger than 99.9% but cannot be equal to 100%.**

##### Reasoning:
Imagine you have 10,000 people. 9,999 of them are 6' tall, and 1 is 5' tall. The average will be very slightly less than
6', and so 9,999 will have heights that are greater than the average. That, in turn, means that 99.99% will have heights that are
greater than average. 99.99% is bigger than 99.9%. Therefore X can be bigger than 99.9%.

However, you can't have 100% of any group have heights larger than the average. It's like a see-saw: if you want to have the
people on one side of the see-saw be higher in the air than the center of the see-saw (the center representing the average, and being
higher than the center representing having a higher value), then you MUST have something on the other end of the see-saw to outweigh
the group you want to be above the center. If you move everyone to one side of the see-saw, there's no way you'll be able to
get that end higher than the center of the see-saw, because there's nothing to counter-balance it.

---

##### Question:
_Suppose that you are at a casino playing roulette. The strategy you are using is to, before each bet, flip a coin to determine whether
to place your bet on red or on black (which, according to the rules of the game, should each have a 50% chance of occurring). After
you've placed each bet, the roulette wheel is then spun. Suppose that you lose fifty nine times in a row (i.e. for fifty nine
consecutive plays, when you place your bet on black the ball then lands on red, and when you place your bet on red the ball then lands
on black). From this experience, it is most rational to conclude that:_

##### Answer:

- _Using a coin toss to determine whether to bet on red or black is in general a very bad strategy for playing roulette_
- **The game is somehow rigged against you and the casino or its employees are cheating you**
- _You are very likely to win on your next bet if you continue this coin flip based strategy_
- _The roulette game is broken, but there is no reason to assume that it was broken intentionally_
- _You were merely very unlucky_
- _One cannot reasonably conclude which of the above options is more likely_

##### Reasoning:
The odds of losing any one round should be 1/2. The odds of losing two rounds in a row should be 1/2 x 1/2 = 1/4. So the odds of losing
59 rounds in a row should be 1/(2^59), or 1.73 x 10^-18, which is a very, very small chance that this would happen. For comparison, a
one-in-a-billion chance would be 1.00 x 10^-9. So basically there's a one-in-a-billion-billion chance that this would have happened
by chance.

---

##### Question:
_Suppose that I have a list of all the numbers from 1 to 64 (not necessarily in order) with no repetitions. You cannot see the list, but
you are allowed to ask me any questions you like about the list that have yes or no answers, and I will always answer truthfully (by
replying either "yes" or "no"). For example, one of your questions may be "Does 3 occur after 9 in the
list?" APPROXIMATELY how many yes-or-no questions will it be necessary to ask so that no matter what the ordering of the list is,
you will know the ordering exactly at the end of your questioning? In other words, if you ask questions in an optimal fashion in order
to minimize the number of questions asked, approximately how many questions will you need in the worst case scenario? Your questions
can be as long and complicated as you like. Note that the questions you decide to ask may depend on my answers to previous questions
that you have already asked._

##### Answer:

- _You will never be guaranteed to know the order, no matter how many yes or no questions you ask._
- _64!_
- _63!_
- _4096_
- _4032_
- _384_
- **296**
- _64_
- _63_

##### Reasoning:
There are 64! possible arrangements of the 64 numbers. Because you can only ask "yes" or "no" questions, with each
question you can only narrow the remaining possibilities down to one of two groups; whereas, for example, if you could ask a question
that had 3 possible answers, each question could lead to narrowing the number of possibilities to a different 1/3 of the remaining
possibilities. Here's a simple example: if I need to guess the arrangement of 3 numbers, 1, 2, and 3, and I can only ask yes-or-no
questions, my first question could be, "Is the arrangement '1, 2, 3'?" If your answer is "yes" (the best
case), then I'm done. If your answer is "no" (the worst case), then I've only knocked off one possibility from the
6 different possible arrangements. If I'm assuming a best-case scenario then this kind of question would be a good question to ask;
but if I'm assuming a worst-case scenario then this is a terrible kind of question to ask. So what IS the best kind of question to
ask if I'm assuming a worst case scenario (where each question is answered in the way that eliminates the fewest possibilities)?

If you're considering the worst case where you can only ask yes-or-no questions, then with each question the most you can hope to
narrow the number of possibilities is to chop the number of possibilities in half. In other words, if the person responds,
"yes", you've eliminated half of the possibilities, and if the person answers "no" you still eliminate half
the possibilities.

Therefore, when you arrive at 1 remaining possibility, it will be because you have divided the 64! possibilities by 2 over and over
again (n times), where n is the number of questions. In other words, 1 = 64!/2^n. Now you just need to solve for n to figure out how
many questions you need to ask.

Multiply both sides of the equation by 2^n and you'll have 2^n = 64!. The question we're left with is, "What power do we
need to raise 2 to to get 64 factorial?" The mathematical way of expressing this question is n = log(base 2)64!. The log button on
your calculator only handles base 10, though, so to change this equation to base 10 you need to look up another property of logs, that
log(base X) of Y = (logZ of Y) / (logZ of X), so in other words, n = (log10 64!) / (log10 2). At that point you can just plug it into
your calculator and you'll get 295.995...

---

##### Question:
_Suppose that you have an enormous pineapple that is 99% water (by weight). The pineapple weights 100 pounds. If the water content of
the pineapple evaporates until it is 98% water (by weight), then approximately how much does the pineapple now weigh?_

##### Answer:

- _99 pounds_
- _96 pounds_
- _95 pounds_
- _60 pounds_
- **50 pounds**
- _49 pounds_

##### Reasoning:
If the pineapple is 99% water by weight and weighs 100 pounds, that means that it has 99 pounds of water in it and 1 pound of other
stuff. So if the pineapple dries up and that 1 lb of other-stuff then makes up 2% of a pineapple by weight, then that means that the
total weight of the pineapple must be 50 pounds. That way, if you double the amount of everything in the dried-up pineapple, you'd
have a 100 pound pineapple with 2 pounds of other-stuff, which would make 2%.

## Linear Algebra [4/6]
_While knowledge of linear algebra is a plus, it is not necessary. If you don't know any linear algebra, just leave these questions
unanswered._

_Suppose you have a real valued square matrix M whose eigenvalues are all real numbers. Furthermore, suppose that none of the eigenvalues
is zero. Select whether each of the following statements is true or false about the matrix M._

---

##### Question:
_M must be invertible (i.e. there exists a matrix W such that W M is the identity matrix)_

##### Answer:
True

##### Reasoning:
While  [researching eigenvalues on Wikipedia](http://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors) I found this:

> The matrix is invertible if and only if all the eigenvalues are nonzero.

Scrap:
 [From KhanAcademy](https://www.khanacademy.org/math/linear-algebra/matrix_transformations/inverse_transformations/v/linear-algebra--matrix-condition-for-one-to-one-trans)-
 M is invertible if and only if its rank is equal to its number of columns/rows. So, if it is possible to construct a matrix which
 meets the conditions in the set-up but does not have a rank equal to its number of columns, then the answer would be "False".

---

##### Question:
_M M' = M' M (where M' is the transpose of M)_

##### Answer:
True

##### Reasoning:

 [This link](http://math.stackexchange.com/questions/170241/when-is-matrix-multiplication-commutative) says "two matrices that are
 simultaneously diagonalizable are always commutative", and  [this link](http://en.wikipedia.org/wiki/Diagonalizable_matrix) says
 "an n×n matrix A over the field F is diagonalizable if and only if the sum of the dimensions of its eigenspaces is equal to n,
 which is the case if and only if there exists a basis of Fn consisting of eigenvectors of A."

So it looks like if you have two nxn matrices, and you can form an n-dimensional (?) basis from each of them, then their multiplication
will be commutative. And since the rank (dimensionality) of a matrix can be gotten from either its rows or its columns, doing the
transpose of M shouldn't affect it. So it should be commutative.

---

##### Question:
_If x is a real valued vector, and M x = 0, then that necessarily implies that x = 0_

##### Answer:
True

##### Reasoning:
From getting the answer to the first T/F I know that the matrix is invertible, and from KhanAcademy I know that if it's invertible
then its rank must be equal to the number of columns/rows. And from knowing how the rank of a matrix is determined (putting the matrix
into reduced-row-echelon-form and counting the number of non-zero rows), I know that this matrix, when put into reduced-row-echelon-form,
 will be the identity matrix. And from knowing how to multiply a matrix by a vector I know that if the final result is zero, it has to
 be that the vector is zero.

For example:
If the top row in the square matrix is [1, 0] and we're multiplying it by a vector [x, y], and the value we're aiming to produce
for the final vector is a zero, then it has to be that 1x + 0y = 0. But the only way for that to happen is if x is zero.

## Risk [5/6]

_Consider a purely probabilistic game that you have the opportunity to play. Each time you play there are n potential outcomes x1, x2,
..., xn (each of which is a specified gain or loss of dollars)_

_These outcomes x1, x2, ..., xn occur with the probabilities p1, p2, ..., pn respectively (where p1 + p2 + ... + pn = 1.0 and 0 <= pi
<= 1 for each i)._

_Positive xi values mean a gain of |xi| dollars and negative values mean a loss of |xi| dollars._

_Assume that x1, x2, ..., xn and p1, p2, ..., pn are all known quantities._

_Furthermore, assume that each play of the game takes up one hour of your time, and that only you can play the game (you can't hire
someone to play for you)._

_Let E be the game's expected value. That is, E = p1 x1 + p2 x2 + ... + pn xn._

_Let S be the game's standard deviation. That is, S = SquareRoot( p1 \* (x1 - E)^2 + p2 \* (x2 - E)^2 + ... + pn \* (xn - E)^2 )._

---

##### Question:
_In the real world, should a rational player always play this game whenever the expected value E is not negative? Why or why not?_

##### Answer:
No.

The question asks whether something is always the case; saying something is always the case is an extremely strong claim. It is often
easier to prove that something is not always the case. To do so I only need to come up with a single example of a situation in which
a person shouldn't play the game.

So, suppose that the game is set up so that you have a single potential outcome of winning $0, and the probability of that outcome is 1.
The expected value will not be negative, but you will never make any money, so a rational player shouldn't play it. Therefore a
rational player should not always play this game whenever the expected value is not negative.

---

##### Question:
_Does the standard deviation S do a good job of capturing how risky this game is? Why or why not?_

##### Answer:
###### Shorter answer:

After creating a simulation in Python and looking at a bunch of examples my impression is that the answer is "sometimes, but not
 always".

Regarding why it can do a good job: it's because it measures the spread of the outcomes, and so when combined with the expectation
value, there will be times when the standard deviation can let you know that a game is a safe bet IF you know how to interpret the
numbers (eg if the game has an EV of $80/hr and StdDev of $7, then as far as I can tell there's no way there's a sneaky
1-in-100 chance of losing $1,000; such a possibility would increase the StdDev to a much higher number).

Regarding why the standard deviation may sometimes not do a good job of capturing the risk: it seems it's because the standard
deviation wasn't conceived of for the purpose of measuring risk; it's like using a brick as a hammer. There are variables
relevant to the riskiness of an activity that are not considered when calculating the standard deviation, such as the fact that a
person can be kept from playing if he runs out of money, or the fact that bankruptcy laws might put a lower bound on the risk. Those
variables seem to become extremely important when you're considering a game that is harder to make sense of than the example above.

###### Longer answer:

[important: if you were ONLY given the the expected value and the standard deviation, could you use that to decide whether to play
the game?]

Unfortunately I'm not good enough at math right now to give as in-depth an answer as I would like, but I can give an outline of
what a good answer would do, and then fill in as much of that outline as I can.

Here's my strategy for answering the question:
1. Use intuitions from simple examples to get a very clear idea of what we want "risky" and "good" to mean.
2. Figure out what would be the ideal way of measuring that definition of "risky".
3. See how closely the standard deviation comes to that ideal way of measuring riskiness, and use the definition of "good"
to decide if the standard deviation gets close enough to be "good". And check for a "it depends" answer, eg
"It depends, if the conditions are XYZ then yes, but in situations where ABC is the case the answer is no".

---

1a. The risk of an activity is its possible bad outcomes weighted by their probabilities.

Example: When considering whether to sign up as a soldier to go to war, soldiers should consider both the KINDS of potential losses
(eg, losing a finger, losing a leg, dying) as well as the probabilities of each kind of loss (eg, 0.0005% chance of losing a finger,
0.0001% chance of losing a leg, 0.00001% chance of dying).

Example: Skydiving has a very severe kind of undesired outcome (death), but the probability of that outcome is so low that skydiving
is not seen as very risky by those who know the probability of death. [On the other hand, people may still get nervous even if they
know the probabilities...I need to think about the implications of that.]

Example: Playing the boardgame Monopoly has a very high probability of a bad outcome (losing), but the severity of that outcome is so
low that playing Monopoly is not seen as being very risky.

It seems to me that there should be some separation between the good-outcomes and bad-outcomes when determining how risky the
activity is. I'm basing this on the fact that people talk about "weighing the risks against the rewards", and that
statement wouldn't seem to make sense if the rewards were already totally described by the risk-measure of the activity.

On the other hand, it seems like you should consider the positive outcomes if the positive outcomes may negate the negative outcomes.
For example, a game of blackjack involves winning some hands and losing some hands.

---

1b. A "good" measure of risk will prompt someone to behave in a way consistent with the level of risk they accept in the
rest of their life.

---

I'm going to define "good" by thinking about how people would use the word in conversation; I think one necessary
condition for a "good" measure of the riskiness of the game would be that if I have two games with the same expectation
value, except with one I could end up losing all my money, and in the other there's no possible way I could lose my money, those
two games should never have the same measures-of-risk. I think this condition will be enough to show that the standard deviation is
not a good measure of risk.

---

> I bet full Kelly, which generally turned out to be a percentage of my bankroll a little less than the percentage expectation in
favorable situations.

So, if it's not possible to limit your bets to that amount, you may end up losing everything, right?


---

Risk is generally taken to mean downside risk. But the standard deviation will not just be influenced with the potential downside of
the game, but also the potential upside.

Simple examples to get ideas from:

0a. The upside of a gamble may be important when determining the level of risk.

Suppose you are comparing two of these games, both of which involve a 90% chance of winning some amount of money and a 10% chance of
losing $500. In both games you are not allowed to play anymore if your balance goes negative, so in both games you would need to hit
the bad outcome twice in a row to be forced to stop playing.

If the upside of the game has no impact on how risky the game is, then these two games should be equally risky based on the information
 given above.

However, suppose that in the first game, the other 9/10 outcomes involve winning $10, while in the second game the other 9/10 outcomes
 involve winning $1,000.

---

Suppose you have two situations: in one, you can pick up a $100 bill on the highway while dodging traffic, and in the other situation
 you can pick up a $1,000,000 bill in identical traffic conditions. I think most people would agree that the two situations have equal
  risk. Hence the phrase "balancing risk and reward": if determining risk already took into account the reward, then that
  phrase wouldn't seem to make sense.


2. Knowing only the standard deviation and the mean would not always give you a good idea of how risky the game is.

For example, suppose you have two games, each with a mean expected result of $100 and a standard deviation of $100. If the mean and
standard deviation alone gave a good idea of the riskiness of a game, then those two games should be equally risky.

But suppose that both games have 10 possible outcomes, each with a probability of 0.1. In the first game, 9/10 times you win $

---

Possible situations:

- 0.5 chance of winning $10
- 0.5 chance of losing $10
- Expected value is 0, Std Dev is $10

I wouldn't play this game because 1) I'd end up even over the long run, and 2) even if I won every time I'd only be making
 $10/hr. I'd say the standard deviation gives a good idea of the risk of the game if it's played once.

- 0.5 chance of winning $100
- 0.5 chance of losing $100
- Expected value is 0, Std Dev is $100

I wouldn't play this game because I'd end up even over the long run, unless I had a really bad streak in which case I could
end up bankrupt. I don't know how to say it mathematically, but the upside and downside would be asymmetrical because if I run out
 of money I can't keep playing, whereas I can always keep playing if I'm up. I may not be explaining that well.

- 0.5 chance of winning $1,000
- 0.5 chance of losing $1,000
- Expected value is 0, Std Dev is $1,000

Same situation as the previous case ($100), although the thing to note here is that it would be easier for me to end up going bankrupt,
 so this might be an even worse deal than the $100 case.

- 0.5 chance of winning $10,000
- 0.5 chance of losing $10,000
- Expected value is 0, Std Dev is $10,000

Same situation as the previous case; it would be easier for me to end up going bankrupt. But the amount of money that I could
potentially win is now starting to get so large that I have to consider the cost of going bankrupt against the potential winnings
if I'm lucky.

- 0.5 chance of winning $100million
- 0.5 chance of losing $100million
- Expected value is 0, Std Dev is 100,000,000

If you can discharge the debt in bankruptcy this may actually be a good game to play.

---

I think the cut-off point for when it will be a good idea to play the game is: look at the total cost of losing the coin-flip,
including bankruptcy and future troubles because of the bankruptcy, and then ask yourself what the money value of that loss is.
When the potential winnings from a single coin-flip are greater than that potential bad outcome, the game will have be
positive-expectation.

---

Thought:
There may not be such a thing as the "inherent riskiness" of a game. The riskiness of a game may depend on the person
playing it. Here's an analogy: how risky is it being in Iraq? The answer to that question would seem to depend on who we're
talking about being in Iraq: is it an American soldier? Is it an Iraqi? Is it a stray cat? It may not be very risky for a stray cat
 to be in Iraq.

---

I'm not exactly sure what is being asked, so I am going to answer this question in two parts. In the first part I am going to
assume that the question is asking whether knowing the standard deviation of the game WITHOUT knowing the expectation value could
give a person a good idea of how risky the game is. In the second part I am going to assume that the question is asking whether
knowing the standard deviation IN COMBINATION WITH the expectation value could give a person a good idea of how risky the game is.

Part I: Does the standard deviation, taken on its own without knowing the expectation value or individual outcomes (and their
probabilities), do a good job of capturing how risky this game is?

If we don't know what the outcomes are, and we don't know anything about how the outcomes will be selected, then no, knowing
 only the standard deviation won't help us determine how risky the game is. This can be demonstrated by constructing examples
 that are "high risk" that have both high and low standard deviations, so that it becomes obvious that there's no
 necessary connection between the standard deviation on its own and whether the game is risky. Suppose there is only one outcome.
 The standard deviation of that game will be zero. If that lone outcome is a loss of $1,000,000, then the game is very risky

For example, suppose you have two different versions of the game: one in which the standard deviation is 0, and another game in which
 the standard deviation is $1,000. Some might think that the second game would be riskier since it has a higher standard deviation.

But suppose that the first game had a single possible outcome of -$1000. It's standard deviation would be 0. And suppose that
the second game had two potential outcomes, each with a probability of 0.5: in the first outcome you win $100, and in the second
outcome you win $1515. That game would have a standard deviation of about $1000, but it wouldn't be risky. Therefore the standard
deviation alone will not always do a good job of capturing how risky the game is.

---

##### Question:
_If YOU PERSONALLY had to decide whether or not to play this game, how would you decide?_

##### Answer:
In general I would try to make my decision consistent with the level of risk I accept in the rest of my life. The specifics would
depend on the circumstances under which I had to decide.

If I had access to a computer and enough time to use it, I would try to use the computer to run Monte Carlo simulations and get an
idea of what kinds of outcomes I could expect from playing the game.

If the game required that I consider small probabilities of large gains/losses, I would probably try to search Google / Wolfram Alpha
 for data on other risks that people commonly take so that I could get an intuitive sense of whether playing this game would be
 dramatically more risky than other things I've done.

I would ask whether the debt from playing the game was dischargeable in bankruptcy, and I would take the answer into account if the
 game involved a chance of that kind of catastrophic loss. The reason I ask: suppose the game had two outcomes, one with a probability
  of 0.5 and an outcome of a $1 billion loss, and the other with a probability of 0.5 and an outcome of a $1 billion gain. If the
  debt from losing is dischargeable in bankruptcy then it would be well worth risking bankruptcy for a 50% shot at $1 billion.

I would ask whether losses could end the game, and if so, when: is it when I run out of cash (like at a carnival), or when I run out
 of money in my bank account (like I imagine it would work at a casino), or when the losses exceed my net worth (including the value
  of everything I own, like books and my laptop), or can I just keep playing even as the losses become far larger than I could ever
  pay? The reason I ask: suppose the game had two outcomes, one with a probability of .99 and a loss of $1000, and other with a
  probability of .01 and a gain of $1 billion; the game would be positive expectation, but I wouldn't have enough money in my
  bank account to survive the likely losses until I hit the jackpot.


## Education [6/6]
##### What is your highest level of formal education?
Completed college

##### If you ever attended college, what was the college or university's name?
The College of New Jersey (TCNJ)

##### What was/is your college major?
Philosophy

##### If you had a second major, or minor, include it here.
Psychology

##### What was your college grade point average (GPA)?
3.81 (cum.), 3.91 in both majors

##### What grading system does your college use?
4 point scale (4=A, 3=B, 2=C)

##### If you ever began a masters or PhD, what was/is the name of the school?
N/A

##### What was/is your area of study in your masters or PhD?
N/A

## Other/Optional

##### Question:
_If there is anything else that you would like to tell us, you can write it below. This is entirely optional._

##### Answer:
I would really like to work at Rebellion. I found out about it through Scott Patterson's book, I've watched the
 talks that Spencer has given, I've read his blog posts, and I've read about Alexander Fleiss' early accomplishments, and
  I have a feeling Rebellion has a very, very bright future ahead of it. Spencer reminds me a lot of the books/articles I've read
   about Ray Dalio and Josh Levine, and to be honest I can't remember the last time I learned about someone whose thoughts /
   opinions were so close to my own. Alexander's investment story of making 10 times his money from a single stock as a 19-year-old
   reminded me a LOT of Ken Griffin's story of making money by shorting the Home Shopping Network as a 19-year-old freshman at
   Harvard. Those kinds of early victories are a common trend in the autobiographies I've read of successful entrepreneurs. I
   think it's extremely impressive how much press exposure Rebellion has been able to get; I'm not aware of any other fund
   run by young guys who are getting that much exposure. One thing I've learned is that it can be extremely valuable to be a
   recognizable name, so that seems like a huge early victory.

My programming ability:
- I have been messing around with code for over 10 years, on-and-off.
- For the first 4-6 years I was mainly interested in using programming for videogames.
- Since graduating college I have become interested in using programming to make my life easier by automating repetitive tasks.
- I have a github account at  [https://github.com/NathanWailes](https://github.com/NathanWailes)
- You can see my answers to USACO questions at  [https://github.com/NathanWailes/USACO-Puzzle-Answers](https://github.com/NathanWailes/USACO-Puzzle-Answers)
- You can play with an unfinished Venn-diagram-teacher I made from scratch at  [http://www.nathanwailes.com/games/venn-diagram-teacher/](http://www.nathanwailes.com/games/venn-diagram-teacher/)

My mathematics ability:
- I have become convinced that being good at math can be a huge advantage for people who know how to use it. I explain to my friends
that it's like having a machine gun in Roman times. At the moment I suspect I may spend the rest of my life studying math, because
 it's one of the few skillsets I've identified as being especially valued by society and in-line with my interests (the others
  are programming, finance, and entrepreneurship).
- I got a 740 on the math section of the SAT but I'm using John Chung's SAT book with Anki to fill the gaps necessary to get me
 to an 800.
- I'm using the Art of Problem Solving books to become very comfortable with probability and useful problem-solving techniques. I
have been praised by the founder, Richard Rusczyk (Princeton grad and former trader at DE Shaw), for using my programming ability to
help him solve a problem.
- I'm using KhanAcademy, MIT OpenCourseWare, and misc. books to learn linear algebra. Right now I'm trying to work through
a-problem-a-day from Halmos' "Linear Algebra Problem Book". I answered the linear algebra questions on the application
 by looking up different properties of matrices; I'm not yet at the point where I can answer questions like that without consulting
  references.
- I have been teaching the LSAT for 3 years now, which has gotten me very comfortable with basic proofs. I've especially learned
the value of 1) keeping track of old proofs/results to use as tools for future problems, 2) double-checking your work to avoid mistakes
 that can be hard to track down later.
- After studying for the LSAT I have become good enough at problem solving to be able to solve the self-referential aptitude test by
Jim Propp [http://www.drunkmenworkhere.org/170]
- I became very familiar with Sudoku puzzles and USA Today Logic Puzzles as part of my preparation for the LSAT, and they taught me
valuable lessons about problem solving (specifically, the need to double-check your work and to systematically look for any deductions
 you can make from any new information you learn).
- You can watch videos of me explaining how to do LSAT logic games here:  [http://www.nathanwailes.com/lg](http://www.nathanwailes.com/lg)
- And compare the depth of my explanations of LSAT games to the depth that other people [Harvard Law School grads] go to:
[http://7sage.com/logic-game-explanations/](http://7sage.com/logic-game-explanations/)
- One of my best friends in high school was exceptional at mathematics (he went on to MIT and is now earning his PhD in algebraic
topology), and over the years I became extremely impressed with his ability to break down problems (whether it was a history project
 or a videogame). I also have another high school friend who has a chess rating over 2100, graduated with a BA in CS from Princeton,
 and is now a quant developer at AQR; he's been giving me advice / moral support (eg I found out about USAMO, the Euler Project,
 and the Wilmott forums from him). I'm mentioning these guys because I've noticed that people often get motivation from looking
 at what their friends are doing, and so I think it's relevant that these are the people I consider friends. "Show me a
 man's friends and I'll show you the man." [or something like that.]

It seems to me that I won't fall into a traditional category of people who would be impressive to you; I didn't go to a
prestigious college, I haven't had any internships at investment banks or tech-savvy companies (eg, Google), I didn't major in
 mathematics or computer science.

However, I think that my unusual path has actually given me some advantages over traditional candidates. I have read a lot of
autobiographies of successful businessmen and hedge fund managers, and I've spent a lot of time thinking about what I've
read, so that when I'm having a conversation with someone I can frequently introduce examples from the books I've read. For
 example, when I was talking with my friend about what he should do after graduating from MIT's MSc in Finance program, I was
 able to draw on all of the stories I've memorized and give him examples of different things that successful hedge fund managers
 have done. I've met a few other people who work in finance who have read a fair number of books, but I always got the impression
  that they were reading them so quickly that they didn't remember a lot of what they had read. I keep copies of all the books I
   read, and I note any ideas I find useful with exclamation points so that when I skim the book later I'll be reminded of the
    best information in it. I used this method when studying 50+ pages of advice on studying for the LSAT and it gave me a huge
     advantage over other people; most people read something once and forget 99% of it, even many of the ideas they thought could be
      useful. The best way I've seen to extract all of the value from a book is to come back to it again and again, reminding
      yourself each time of the good ideas it contains, and pushing yourself to try out those useful ideas. If you have a busy
      conventional finance job, you may be less likely to use your free time to do something like that.

A video of me philosophizing with a friend:
 [http://www.youtube.com/watch?v=vezDYoI8ddU](http://www.youtube.com/watch?v=vezDYoI8ddU)

Another advantage I may have is that, because I haven't spent a lot of time at investment banks / hedge funds / etc, I haven't
 picked up a lot of the conventional wisdom that exists in those places. From briefly studying for the CFA and from conversations
  I've had, I've gotten the impression that those places require their workers to be a lot like soldiers: the soldier's
   job is to execute their missions without questioning some of the assumptions that underlie those missions. Similarly, the CFA
   textbooks seem to frequently make assertions about how the world works without giving the student a way of double-checking the
   assumptions upon which those assertions are based. I don't see anything inherently wrong with training people that way; it
   seems like a much more efficient way of running the military/banks, and I'm sure both the soldier and the CFA-er learn a lot
    about how war/finance work by doing their jobs day-to-day. However, if your eventual goal is to systematically examine all of
    the assumptions that the world's financial system is based on and look for exploitable inefficiencies, getting traditional
    training may have the drawback of having planted some unquestioned-assumptions in your head.

---

##### Question:
_If you feel that any of the questions in this quiz are unreasonable, ambiguous or poorly worded, please tell us which ones. We
appreciate your feedback, but this is entirely optional._

##### Answer:
N/A