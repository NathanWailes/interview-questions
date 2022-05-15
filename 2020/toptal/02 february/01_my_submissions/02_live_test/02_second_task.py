"""
Task description: You're given a list of relations, where Person1:Person2 means that Person1 is friends with Person2.
Relations are transitive, so if Person1:Person2 and Person2:Person3, then Person1:Person3.
Your task is to return the total number of friends that one or more specified persons has.
"""

from collections import defaultdict

"""
numberOfFriends(["Anne:Barbara","Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"]) // Anne:2, Vinny: 1
numberOfFriends(["Octavia:Zoltan", "Zoltan:Marko", "Marko:Diego", "Diego:Andres"], ["Octavia", "Diego"]) // Octavia: 4, Diego: 4


"""


def numberOfFriends(list_of_relations_as_strings, list_of_names_to_get_friend_counts_for):
    name_to_list_of_friends = defaultdict(list)
    for relation in list_of_relations_as_strings:
        two_names = relation.split(':')
        first_name = two_names[0]
        second_name = two_names[1]
        name_to_list_of_friends[first_name].append(second_name)
    print(name_to_list_of_friends)

    list_of_results = []
    for outer_name in list_of_names_to_get_friend_counts_for:
        friends_count = 0
        name_to_check = outer_name
        while True:
            if name_to_check not in name_to_list_of_friends.keys():
                break
            else:
                friends_count += 1
                name_to_check = name_to_list_of_friends[name_to_check][0]
        list_of_results.append(friends_count)

    print(list_of_results)
    return list_of_results




"""

    for outer_name in list_of_names_to_get_friend_counts_for:
        friends_count = 0
        set_of_visited_names = set([outer_name])
        set_of_names_to_check = set()
        current_name_friends_to_check = name_to_list_of_friends[outer_name]
        for friend_name in current_name_friends_to_check:
            if friend_name not in set_of_visited_names:
                set_of_names_to_check.add(friend_name)

        for friend_name in set_of_names_to_check:
            current_name_friends_to_check = name_to_list_of_friends[outer_name]
            if friend_name not in set_of_visited_names:
                set_of_names_to_check.add(friend_name)
        list_of_results.append(friends_count)

"""

if __name__ == '__main__':
    numberOfFriends(["Anne:Barbara","Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"])
    numberOfFriends(
        ["Vanja:Sergio", "Sergio:Pedro", "Pedro:Martin", "Martin:Pablo", "Pablo:Sergio", "Jelena:Ivan", "Jelena:Alan",
         "Alan:Tomislav"], ["Tomislav", "Martin"])
