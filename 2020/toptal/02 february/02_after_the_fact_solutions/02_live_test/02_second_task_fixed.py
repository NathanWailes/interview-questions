"""
Task description: You're given a list of relations, where Person1:Person2 means that Person1 is friends with Person2.
Relations are transitive, so if Person1:Person2 and Person2:Person3, then Person1:Person3.
Your task is to return the total number of friends that one or more specified persons has.

My thought at how to solve this:
1. Solve the simplest case first, where each person appears on the left side of at most one relation and there are no
loops in the relations.

Test cases provided by the interviewer:
Simplest case: A chain of 2 and a chain of 1:
numberOfFriends(["Anne:Barbara","Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"]) // Anne:2, Vinny: 1

Testing whether your code can only go 'forwards' in a chain or if it can also detect 'previous' relations in the chain:
numberOfFriends(["Octavia:Zoltan", "Zoltan:Marko", "Marko:Diego", "Diego:Andres"], ["Octavia", "Diego"]) // Octavia: 4, Diego: 4

Testing whether your code can deal with 'loops' in the chains of relations:
numberOfFriends(["Vanja:Sergio", "Sergio:Pedro", "Pedro:Martin", "Martin:Pablo", "Pablo:Sergio", "Jelena:Ivan",
"Jelena:Alan", "Alan:Tomislav"], ["Tomislav", "Martin"]) // Tomislav: 3, Martin: 4

Testing whether your code can handle many different sets of friends.
numberOfFriends(["Alvaro:Alex", "Roman:Nikola", "Octavia:Barbara", "Joao:Marko", "Luis:Vanja", "Gabriel:Gustavo",
"Alan:Pablo", "Ivan:Andres", "Artem:Anne", "Martin:Alessandro", "Sebastian:Vinny", "Eduardo:Francis", "Zoltan:Vlad"],
["Zoltan", "Ivan"]) // Zoltan: 1, Ivan: 1

Testing whether your code can update a friend set when a new relation goes 'backwards' from the 'normal' direction of
the chain.
numberOfFriends(["David:Francis", "Francis:Alessandro", "Alessandro:Ivan", "Tomislav:Ivan", "Anne:Tomislav",
"Anne:David", "Francis:Tomislav"], ["Francis", "David"]) // Francis: 5, David: 5

Testing a bunch of different things from the previous test cases.
numberOfFriends(["Alessandro:Anna", "Anna:Anne", "Anne:Barbara", "Barbara:David", "David:Francis", "Francis:Eduardo",
"Eduardo:Anna", "Eduardo:Alessandra", "Luis:Marko", "Joao:Vlad", "Vlad:Luka", "Luka:Nikola", "Nikola:Roman",
"Vlad:Roman", "Vlad:Vinny", "Vinny:Roman", "Vlad:Andres", "Vinny:Ivan"], ["Barbara", "Joao"]) // Barbara: 6, Joao: 7

"""
from collections import defaultdict


def numberOfFriends(list_of_relations_as_strings, list_of_names_to_get_friend_counts_for):
    names_to_sets_of_friends = defaultdict(set)
    for relation in list_of_relations_as_strings:
        two_names = relation.split(':')
        first_name = two_names[0]
        second_name = two_names[1]
        names_to_sets_of_friends[first_name].add(second_name)
    print(names_to_sets_of_friends)

    list_of_results = []
    for outer_name in list_of_names_to_get_friend_counts_for:
        friends_count = 0
        name_to_check = outer_name
        while True:
            if name_to_check not in names_to_sets_of_friends.keys():
                break
            else:
                friends_count += 1
                name_to_check = names_to_sets_of_friends[name_to_check][0]
        list_of_results.append(friends_count)

    print(list_of_results)
    return list_of_results


if __name__ == '__main__':
    assert numberOfFriends(["Anne:Barbara", "Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"]) == [2, 1]
    assert numberOfFriends(["Octavia:Zoltan", "Zoltan:Marko", "Marko:Diego", "Diego:Andres"], ["Octavia", "Diego"]) == [4, 4]
