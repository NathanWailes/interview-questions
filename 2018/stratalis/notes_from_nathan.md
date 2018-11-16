
# Notes from Nathan


## Question 1

If I remember correctly, I didn't really encounter any problems with this one.

## Question 2

This one was quick and easy to do.  I was worried about an off-by-one error but the example case worked, so I didn't 
bother to check it any further.

## Question 3

This is where things started to go south.  I developed my solution in ~9 minutes but none of the test cases were passing
(even the simple example case), and I could not figure out why.  IIRC I had ~30 minutes for this question and I spent 
the remainder of the time trying to figure out why my solution wouldn't pass the example case, but I never figured it 
out.

## Question 4

I developed an initial solution that isn't visible in the current code that just used `.pop()` to update the list of 
tiles, and that passed the simple test cases, but it did not pass the lots-of-values case.

I looked into why and it was clear that my solution was O(n^2), as the `.pop()` was running in the middle of the list 
and (from looking on Google) I realized that that was an O(N) task, running within an O(N) loop (the outer loop being 
the character jumping around until there are no tiles left to jump to).

I then spent a few minutes thinking about how to get a faster solution and realized that this seemed to be a situation
that called for a doubly-linked list.

I worked to implement the new solution but unfortunately couldn't iron out the remaining bugs before my time ran out.

## Question 5

I was able to solve this one very quickly.  In hindsight I notice that the question stipulates that the solution should
have the entries in the final tuple match the order of the entries in the original tuples, and I'm not sure that my 
solution guarantees that, as I store everything in a dict before passing it into a new namedtuple.

## Question 6

I was able to quickly join the tables and add the `count()`, but (embarrassingly) I could not figure out how to get the
customers with no transactions to show up with a `0` result before my time ran out.  Google was giving me a bunch of
unhelpfully-complicated answers rather than the quick solution I was looking for.

## Question 7

I was able to get this one done correctly.

## Question 8

I was unsure of how to proceed for a good portion of the time allotted to me for this question; I know I could have done
this quickly two years ago when I was writing SQL queries every day for my job, and I knew I needed to think about the 
query in a step-by-step way (I had a method back then), but I couldn't remember exactly how I used to proceed to write a
query like this.

Eventually I broke through my haze and was able to develop a nearly-finished query. My solution was returning `Adam 20`
but wasn't returning the Eve result, and I ran out of time before I could figure out why. 

## Result

I took 2 hours 21 minutes.  I bombed it, but I'm not too concerned because I have other clients who are willing to hire
me without asking these sorts of questions, and they seem to be happy with the work I do for them.  The one time I've
done very well on a test like this, it was because I had just finished working on a similar problem, and the fact that 
the interviewer attributed my success to general good programming ability rather than having recently seen the problem
has made me skeptical about how useful these tests are for judging a programmer's productivity.

From the website:

> Python Backend Developer
> 
> YOUR TEST SCORE: 42%
> 
> Your answers have been sent to the employer for consideration.
> 
> The employer will contact you with further information.
