"""

Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!


Q:Shuffle characters of  a string so that no same characters are together
aaabc => abaca, / acaba

aaabbbccc = > abcabcabc

input_string = 'abccba'
sorted_string = sorted(input_string)
aaabbbccc
abaabbccc
abababccc

aaaaaa --> ''
None, null, 'invalid'

aabb
abab

aabbb
ababb
wrong: bbaba

goal: babab

aabbb
ababbababb
babab

aaabbbccc
abaabbccc
abababcccabababccc
bababcaccbababccc
ababcacbc

aabbb
ababb

aa

aaab
abaa

aaaabc
abacaa

Input: aabbb
babb

nlogn
n
a(average
number
of
duplicates
per
character), worst
case
O(N)



Later: Here's a discussion on Stack Overflow of how to solve this:
https://stackoverflow.com/questions/39171840/
"""


def get_string_sorted_so_there_are_no_two_same_characters_in_a_row(
        input_string):
    if len(input_string) < 2:
        return input_string
    sorted_string = sorted(input_string)
    index_of_current_character_to_check = 1
    index_of_the_last_character = len(input_string) - 1
    while index_of_current_character_to_check <= index_of_the_last_character:
        index_of_the_previous_character = index_of_current_character_to_check - 1
        current_character = sorted_string[index_of_current_character_to_check]
        previous_character = sorted_string[index_of_the_previous_character]
        current_character_matches_previous_character = current_character == previous_character
        if current_character_matches_previous_character:
            # search forward for a different character and insert it into the position of the current character
            index_of_potential_separator_character = index_of_current_character_to_check + 1
            we_have_wrapped_around = False
            while True:
                if index_of_potential_separator_character > index_of_the_last_character:
                    index_of_potential_separator_character = 0
                    we_have_wrapped_around = True
                potential_separator_character = sorted_string[
                    index_of_potential_separator_character]
                if we_have_wrapped_around and potential_separator_character == current_character:
                    raise ValueError("This string cannot be sorted as desired.")
                if potential_separator_character == current_character:
                    pass
                else:
                    if not we_have_wrapped_around:
                        sorted_string.pop(
                            index_of_potential_separator_character)
                        sorted_string.insert(potential_separator_character,
                                             index_of_current_character_to_check)
                    else:
                        sorted_string.insert(potential_separator_character,
                                             index_of_current_character_to_check)
                        sorted_string.pop(
                            index_of_potential_separator_character)
                    break
                index_of_potential_separator_character += 1
        index_of_current_character_to_check += 1
