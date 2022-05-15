"""
minutes since open, duration in minutes
storeEmptyAt([[0,7], [1,3], [1,4]]) // 7  minutes

"""
from collections import defaultdict


def store_empty_at(list_of_customer_data):
    """
    >>> store_empty_at([[0,7], [1,3], [1,4]])
    7

    >>> store_empty_at([[0,7]])
    7

    :return:
    """
    arrival_times_to_wait_times = defaultdict(list)
    for customer_data in list_of_customer_data:
        customer_arrival_time = customer_data[0]
        time_to_process_this_customer = customer_data[1]
        arrival_times_to_wait_times[customer_arrival_time].append(time_to_process_this_customer)

    total_number_of_customers_served = 0
    customers_waiting_to_be_served = []
    current_minute = 0
    while total_number_of_customers_served < len(list_of_customer_data):
        if current_minute in arrival_times_to_wait_times.keys():
            customers_waiting_to_be_served.extend(arrival_times_to_wait_times[current_minute])

        for index in reversed(range(3)):
            try:
                customers_waiting_to_be_served[index] -= 1
                if customers_waiting_to_be_served[index] == 0:
                    customers_waiting_to_be_served.pop(index)
                    total_number_of_customers_served += 1
            except IndexError:
                pass
        current_minute += 1

    return current_minute
