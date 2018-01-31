"""
The Telnyx Chicago Point of Presence has five network devices. Each device has a primary port. Some devices also
have a secondary port. Each port has a range of VLAN IDs that are available for use.

We have incoming requests to reserve VLAN IDs for later use. Once a request reserves a VLAN ID on a particular port
and device, no other request may reserve that VLAN ID on that port and device. There are two types of requests:

    1) Requests that do not require redundancy - for these we would like to reserve a single
    VLAN ID that meets the following criteria:

        a) The VLAN ID should be the lowest available VLAN ID on any primary​ port.
        b) In the event of a tie, we would choose the VLAN ID on the device with the lowest
        device ID

    2) Requests that require redundancy - for these we would like to reserve a pair of VLAN
    IDs that meet the following criteria:

        a) One VLAN ID must be from a primary​ port and the other must be from a
        secondary​ port
        b) The two ports must be on the same device
        c) The VLAN IDs must be the same on both ports
        d) The VLAN IDs should be the lowest possible IDs that meet the above criteria
        e) Again, in the event of a tie, we would choose the VLAN IDs on the device with
        the lowest device ID

This program will take a VLANs CSV and 'requests' CSV as input and produce an output CSV file that specifies which
requests reserved which VLAN IDs on which port and device. There is one row for a request that does not require
redundancy and two rows for a request that does require redundancy.

"""

import csv
from collections import defaultdict, namedtuple


def output_csv_of_request_assignments(vlan_csv_path, requests_csv_path, output_path):
    """
    Take a VLAN IDs CSV and a 'requests' CSV as input and produce an output CSV file that specifies which
    requests reserved which VLAN IDs on which port and device.

    Explanation of the implementation:

    Every incoming request must have a primary-port VLAN ID, and so to make sure the IDs are assigned in order, we
    maintain a sorted list of available primary port VLAN IDs. If there are multiple identical VLAN IDs, we're supposed
    to assign the one with the lowest device ID first, so we sort not only by VLAN ID but also by the device ID.

    For a request that does not require redundancy we pop off the first available VLAN ID in the sorted list and assign
    the request to it.

    To handle requests that require redundancy we use a second data structure: a dictionary that maps from a device ID
    to a set which contains all of the secondary port VLAN IDs on that network device. We step through the (sorted)
    available primary port VLAN IDs and check if it's redundant, stopping when we find one that is. We then assign the
    request to it and pop it out of the list of available primary port VLAN IDs.
    """

    sorted_available_primary_port_vlan_id_addresses = get_sorted_available_primary_port_vlan_id_addresses(vlan_csv_path)
    map_from_device_ids_to_secondary_port_vlan_ids = get_map_from_device_ids_to_secondary_port_vlan_ids(vlan_csv_path)

    assignments = get_assignments_of_requests_to_vlan_ids(sorted_available_primary_port_vlan_id_addresses,
                                                          map_from_device_ids_to_secondary_port_vlan_ids,
                                                          requests_csv_path)

    output_assignments_to_csv(assignments, output_path)


def get_sorted_available_primary_port_vlan_id_addresses(vlan_csv_path):
    VlanIdAddress = namedtuple('VlanEntry', ['device_id', 'vlan_id'])

    available_primary_port_vlan_id_addresses = []

    with open(vlan_csv_path) as csvfile:
        for row in csv.DictReader(csvfile):
            device_id = int(row['device_id'])
            is_on_a_primary_port = bool(int(row['primary_port']))
            vlan_id = int(row['vlan_id'])

            if is_on_a_primary_port:
                available_primary_port_vlan_id_addresses.append(VlanIdAddress(device_id=device_id, vlan_id=vlan_id))

    sorted_available_primary_port_vlan_id_addresses = sorted(available_primary_port_vlan_id_addresses,
                                                             key=lambda vlan_entry: (vlan_entry.vlan_id,
                                                                                     vlan_entry.device_id))
    return sorted_available_primary_port_vlan_id_addresses


def get_map_from_device_ids_to_secondary_port_vlan_ids(vlan_csv_path):
    """ This function returns a dictionary which has device IDs as its keys, and sets of secondary port VLAN IDs as its
    values. The idea is to make it easy to check if a particular device has a secondary port VLAN ID of a particular
    value.

    :param vlan_csv_path:
    :return:
    """
    map_from_device_ids_to_secondary_port_vlan_ids = defaultdict(set)

    with open(vlan_csv_path) as csvfile:
        for row in csv.DictReader(csvfile):
            device_id = int(row['device_id'])
            is_on_a_primary_port = bool(int(row['primary_port']))
            vlan_id = int(row['vlan_id'])

            if not is_on_a_primary_port:
                map_from_device_ids_to_secondary_port_vlan_ids[device_id].add(vlan_id)

    return map_from_device_ids_to_secondary_port_vlan_ids


def get_assignments_of_requests_to_vlan_ids(sorted_available_primary_port_vlan_id_addresses,
                                            map_from_device_ids_to_secondary_port_vlan_ids,
                                            requests_csv_path):
    assignments = []
    with open(requests_csv_path) as requestfile:
        requests = [row for row in csv.DictReader(requestfile)]
        if not len(requests) <= len(sorted_available_primary_port_vlan_id_addresses):
            raise AssertionError("Not enough available primary port VLAN IDs")

        last_request_id = None
        for row in requests:
            request_id = int(row['request_id'])
            if last_request_id and request_id < last_request_id:
                raise RuntimeError("Request IDs in the CSV are not in order.")
            else:
                last_request_id = request_id

            requires_redundancy = bool(int(row['redundant']))

            if not requires_redundancy:
                assigned_vlan_entry = sorted_available_primary_port_vlan_id_addresses.pop(0)
                assignments.append({'request_id': request_id,
                                     'device_id': assigned_vlan_entry.device_id,
                                     'primary_port': '1',
                                     'vlan_id': assigned_vlan_entry.vlan_id})
            else:  # If the request requires redundancy...
                redundant_vlan_id_found = False
                for index, vlan_entry in enumerate(sorted_available_primary_port_vlan_id_addresses):
                    # In this loop we're stepping through the available primary port VLAN IDs and looking for one
                    # that's redundant.
                    device_id = vlan_entry.device_id
                    vlan_id = vlan_entry.vlan_id

                    # If it's redundant...
                    if vlan_id in map_from_device_ids_to_secondary_port_vlan_ids[device_id]:
                        # Note: It has been specified that the output CSV should be sorted by request_id (ascending) and
                        # then primary_port (ascending), so the order of the two writerow calls below matters (the
                        # '0' must come before the '1').
                        assignments.append({'request_id': request_id,
                                             'device_id': device_id,
                                             'primary_port': '0',
                                             'vlan_id': vlan_id})
                        assignments.append({'request_id': request_id,
                                             'device_id': device_id,
                                             'primary_port': '1',
                                             'vlan_id': vlan_id})

                        sorted_available_primary_port_vlan_id_addresses.pop(index)
                        redundant_vlan_id_found = True
                        break
                if not redundant_vlan_id_found:
                    raise RuntimeError("Not enough available redundant VLAN IDs. Request ID: %d" % request_id)
    return assignments


def output_assignments_to_csv(assignments, output_path):
    with open(output_path, 'w', newline='') as output_csv_file:
        writer = csv.DictWriter(output_csv_file, fieldnames=['request_id', 'device_id', 'primary_port', 'vlan_id'])
        writer.writeheader()
        for row in assignments:
            writer.writerow(row)


if __name__ == '__main__':
    output_csv_of_request_assignments('./test_vlans.csv', './test_requests.csv', './test_actual_output.csv')
    output_csv_of_request_assignments('./vlans.csv', './requests.csv', './output.csv')
