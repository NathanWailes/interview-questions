*(Converted to Markdown from PDF by Nathan Wailes)*

A Blob is a shape in two-dimensional integer coordinate space where all cells have at least one
adjoining cell to the right, left, top, or bottom that is also occupied. Given a 10x10 array of
boolean values that represents a Blob uniformly selected at random from the set of all
possible Blobs that could occupy that array, write a program that will determine the Blob
boundaries. Optimize first for finding the correct result and then for minimizing the number of
cell value reads, balancing minimization against elegance and clarity.

Sample input:
```
0000000000
0011100000
0011111000
0010001000
0011111000
0000101000
0000101000
0000111000
0000000000
0000000000
```
Sample output:
```
Cell Reads: 44
Top: 1
Left: 2
Bottom: 7
Right: 6
```