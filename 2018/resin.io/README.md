# Exercises

## Introduction

The first step of our interview process includes an automated programming test - https://www.qualified.io/assess/(NW: link removed) .

Note that the test _will not_ start automatically once you visit it, so no need to worry about that.

After opening the page you'll see some basic instructions, as well as a link to the _practice assessment_, which we recommend reviewing so you can get used to the testing system interface.

The actual test consists of 3 programming questions covering basic algorithms, data structures, and general programming skills. The test should be solved in JavaScript (ES6 is OK).

Each question has several pre-defined test cases. One or two of these are provided as visible unit tests, which you can extend or change to help you develop your solution. There are also some more in depth tests, where the full test definition is hidden, however you will still be able to run your program as many times as you like, and check that both visible and non-visible test cases pass.

The time limit is 90 minutes.

We feel this should be enough to get everything done, but we understand things don't always go to plan, so completing 100% of the test is not a critical requirement. Rather, we're interested in seeing how you approach the problems, how you structure the code and how you write your algorithms.

Note that you can get points even for programs that don't produce the correct result for every test case: each passing test case contributes to your score, though overall it's better to get 2 problems correct than to submit partial solutions to all 3 of them.

Please note that once you start the test you can't stop or pause it, so be sure to give yourself enough time to complete it and ensure your computer and internet connection are reliable. We recommend using a modern browser such as Google Chrome stable.

Note that the testing system has plagiarism detection, so while it's OK to research the problems and consult online or offline docs, we prohibit copying other people's source code.

We expect you to complete the test within the next 7 days. Please let us know if you are unable to do so and we can potentially rearrange it for you.

## Exercise 1
Complete the `mergeStrings` function in your editor.

Your function must merge strings a and b, and then return a single merged string. A merge operation on two strings is described as follows:

Append alternating characters from a and b, respectively, to some new string, mergedString.
Once all of the characters in one of the strings have been merged, append the remaining characters in the other string to mergedString.

### Documentation
`mergeStrings(a, b)`

#### Parameters
- `a`: String
- `b`: String

#### Return Value
- String - The `mergedString`

#### Constraints
- `0 ≤ |a length|, |b length| ≤ 25000`

### Examples

|            | a     | b     | returns  |
|------------|-------|-------|----------|
| Example #1 | "abc" | "def" | "adbecf" |
| Example #2 | "ab"  | "def" | "adbef"  |
| Example #3 | "abc" | "de"  | "adbec"  |


## Exercise 2

For this exercise you will be strengthening your page-fu mastery. You will complete the `PaginationHelper` class, which 
is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each 
page. The types of values contained within the collection/array are not relevant.

The following are some examples of how this class is used:
```
PaginationHelper<Character> helper = new PaginationHelper(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f'), 4);
helper.pageCount(); //should == 2
helper.itemCount(); //should == 6
helper.pageItemCount(0); //should == 4
helper.pageItemCount(1); // last page - should == 2
helper.pageItemCount(2); // should == -1 since the page is invalid

// pageIndex takes an item index and returns the page that it belongs on
helper.pageIndex(5); //should == 1 (zero based index)
helper.pageIndex(2); //should == 0
helper.pageIndex(20); //should == -1
helper.pageIndex(-10); //should == -1
```

### Sample tests
```
var collection = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24];
var helper = new PaginationHelper(collection, 10);

Test.assertEquals(helper.pageCount(), 3, 'page_count is returning incorrect value.');
Test.assertEquals(helper.pageIndex(23), 2, 'page_index returned incorrect value');
Test.assertEquals(helper.itemCount(), 24, 'item_count returned incorrect value');
```

## Exercise 3

Write a function that takes a string of braces, and determines if the order of the braces is valid.

Write a function called `validBraces` that takes a string of braces, and determines if the order of the braces is valid. 
`validBraces` should return true if the string is valid, and false if it's invalid.

All input strings will be nonempty, and will only consist of open parentheses `'('` , closed parentheses `')'`, open 
brackets `'['`, closed brackets `']'`, open curly braces `'{'` and closed curly braces `'}'`.

What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace. For example:

`'(){}[]'` and `'([{}])'` would be considered valid, while `'(}'`, `'[(])'`, and `'[({})](]'` would be considered invalid.

### Examples

| Input                     | Output |
|---------------------------|--------|
| `validBraces( "(){}[]" )` | `true`   |
| `validBraces( "(}" )`     | `false`  |
| `validBraces( "[(])" )`   | `false`  |
| `validBraces( "([{}])" )` | `true`   |