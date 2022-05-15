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
"""


def numberOfFriends(list_of_relations, list_of_people_to_get_friend_counts_for):
    """
    >>> numberOfFriends(["Anne:Barbara","Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"])
    'Anne: 2, Vinny: 1'

    >>> numberOfFriends(["Octavia:Zoltan", "Zoltan:Marko", "Marko:Diego", \
    "Diego:Andres"], ["Octavia", "Diego"])
    'Diego: 4, Octavia: 4'

    >>> numberOfFriends(["Vanja:Sergio", "Sergio:Pedro", "Pedro:Martin", \
    "Martin:Pablo", "Pablo:Sergio", "Jelena:Ivan", "Jelena:Alan", \
    "Alan:Tomislav"], ["Tomislav", "Martin"])
    'Martin: 4, Tomislav: 3'

    >>> numberOfFriends(["Alvaro:Alex", "Roman:Nikola", "Octavia:Barbara", \
    "Joao:Marko", "Luis:Vanja", "Gabriel:Gustavo", "Alan:Pablo", "Ivan:Andres", \
    "Artem:Anne", "Martin:Alessandro", "Sebastian:Vinny", "Eduardo:Francis", \
    "Zoltan:Vlad"], ["Zoltan", "Ivan"])
    'Ivan: 1, Zoltan: 1'

    >>> numberOfFriends(["David:Francis", "Francis:Alessandro", "Alessandro:Ivan", \
    "Tomislav:Ivan", "Anne:Tomislav", "Anne:David", "Francis:Tomislav"], \
    ["Francis", "David"])
    'David: 5, Francis: 5'

    >>> numberOfFriends(["Alessandro:Anna", "Anna:Anne", "Anne:Barbara", \
    "Barbara:David", "David:Francis", "Francis:Eduardo", "Eduardo:Anna", \
    "Eduardo:Alessandra", "Luis:Marko", "Joao:Vlad", "Vlad:Luka", "Luka:Nikola", \
    "Nikola:Roman", "Vlad:Roman", "Vlad:Vinny", "Vinny:Roman", "Vlad:Andres", \
    "Vinny:Ivan"], ["Barbara", "Joao"])
    'Barbara: 7, Joao: 7'

    :return:
    """
    list_of_friend_sets = _get_friend_sets(list_of_relations)
    person_names_to_friend_counts = _get_dict_of_person_names_to_friend_counts(list_of_people_to_get_friend_counts_for, list_of_friend_sets)
    output_string = _get_output_string(list_of_people_to_get_friend_counts_for, person_names_to_friend_counts)
    return output_string


def _get_friend_sets(list_of_relations):
    list_of_friend_sets = []
    for relation in list_of_relations:
        person_1_name, person_2_name = relation.split(':')
        person_1_existing_friend_set = None
        person_2_existing_friend_set = None
        person_1_existing_friend_set_index = None
        person_2_existing_friend_set_index = None
        for index, friend_set in enumerate(list_of_friend_sets):
            if person_1_name in friend_set:
                person_1_existing_friend_set = friend_set
                person_1_existing_friend_set_index = index
            if person_2_name in friend_set:
                person_2_existing_friend_set = friend_set
                person_2_existing_friend_set_index = index
        if person_1_existing_friend_set is None and person_2_existing_friend_set is None:
            list_of_friend_sets.append({person_1_name, person_2_name})
        elif person_1_existing_friend_set is not None and person_2_existing_friend_set is None:
            person_1_existing_friend_set.add(person_2_name)
        elif person_1_existing_friend_set is None and person_2_existing_friend_set is not None:
            person_2_existing_friend_set.add(person_2_name)
        elif person_1_existing_friend_set is not None and person_2_existing_friend_set is not None:
            list_of_friend_sets[person_1_existing_friend_set_index] = person_1_existing_friend_set.union(person_2_existing_friend_set)
            if person_1_existing_friend_set_index != person_2_existing_friend_set_index:
                list_of_friend_sets.pop(person_2_existing_friend_set_index)
    return list_of_friend_sets


def _get_dict_of_person_names_to_friend_counts(list_of_people_to_get_friend_counts_for, list_of_friend_sets):
    persons_to_get_friend_counts_for_to_their_friend_counts = dict()
    for person_name in list_of_people_to_get_friend_counts_for:
        person_friend_count = 0
        for friend_set in list_of_friend_sets:
            if person_name in friend_set:
                person_friend_count = len(friend_set) - 1
        persons_to_get_friend_counts_for_to_their_friend_counts[person_name] = person_friend_count
    return persons_to_get_friend_counts_for_to_their_friend_counts


def _get_output_string(list_of_people_to_get_friend_counts_for, person_names_to_friend_counts):
    output_string = ''
    for person_name in sorted(list_of_people_to_get_friend_counts_for):
        if output_string:
            output_string += ', '
        output_string += '%s: %d' % (person_name, person_names_to_friend_counts[person_name])
    return output_string
