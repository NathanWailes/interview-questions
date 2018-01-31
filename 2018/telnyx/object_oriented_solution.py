import csv
from collections import namedtuple

"""
Plain English explanation of the solution:

Read in the VLANs from vlans.csv.

Create a sorted list of tuples: (VLAN ID, Device ID) for the VLANs on a primary port.
  - We're going to repeatedly pop the first tuple off and use that for each incoming request.

Read in the requests from requests.csv.

For each request in the requests:
 - Check if it requires redundancy.
 - If it does not require redundancy:

Sort the result ascending by the request ID and then ascending by the primary port.
Export it to test_output.csv.

--------------------

Thoughts:
- You're going to want to be able to query for a lowest-redundant port and also for a lowest-any-kind port.
- Simpler first version: Just deal with the requests that don't require redundancy.
- For dealing with the primary/secondary ports, you'll need to track 


The problem is this: when a request comes in and it requires redundancy, how do you figure out what the lowest
redundant VLAN ID is? If you create a separate data structure to track the redundant devices, you need to keep it in-
sync with the other data structure that handles requests that *don't* require redundancy. If you use a single data
structure, you'll need to search through it for every request that requires redundancy; that's potentially duplicating
a lot of work.

If you just keep track of which 
"""


def main(vlans_csv_path, requests_csv_path, output_path):
    point_of_presence = PointOfPresence(vlans_csv_path)
    requests = Request.get_requests_from_csv(requests_csv_path)

    for request in requests:
        point_of_presence.assign_request(request)

    point_of_presence.export_assignments_to_csv(output_path)


class PointOfPresence:
    def __init__(self, vlans_csv_path=None):
        if vlans_csv_path:
            self.network_devices = self._get_network_devices_from_csv(vlans_csv_path)

    @staticmethod
    def _get_network_devices_from_csv(vlans_csv_path):
        network_devices = []

        vlan_ids_input_rows = PointOfPresence._get_vlan_id_input_rows(vlans_csv_path)

        # Before we create the network devices, let's figure out which ones have secondary ports.
        device_ids = set()
        device_ids_with_a_secondary_port = set()
        for row in vlan_ids_input_rows:
            device_id = row.device_id
            is_on_the_primary_port = row.primary_port

            if device_id not in device_ids:
                device_ids.add(device_id)

            if not is_on_the_primary_port and device_id not in device_ids_with_a_secondary_port:
                device_ids_with_a_secondary_port.add(device_id)

        # Create the network devices
        for device_id in device_ids:
            has_a_secondary_port = device_id in device_ids_with_a_secondary_port
            new_device = NetworkDevice(device_id, has_a_secondary_port, vlan_ids_input_rows)
            network_devices.append(new_device)

        return sorted(network_devices, key=lambda device: device.device_id)

    @staticmethod
    def _get_vlan_id_input_rows(vlans_csv_path):
        vlan_ids = []
        with open(vlans_csv_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vlan_id = VlanId(int(row['device_id']), bool(int(row['primary_port'])), int(row['vlan_id']))
                vlan_ids.append(vlan_id)
        return vlan_ids

    def assign_request(self, request):
        pass

    def export_assignments_to_csv(self, output_path):
        output = [{'request_id': '', 'vlan_id': '', 'device_id': ''}]

        with open(output_path, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['request_id', 'device_id', 'primary_port', 'vlan_id'])
            writer.writeheader()

            for row in output:
                writer.writerow(row)


VlanId = namedtuple('VlanId', ['device_id', 'primary_port', 'vlan_id'])


class NetworkDevice:
    def __init__(self, device_id, has_a_secondary_port, vlan_ids_input_rows):
        self.device_id = device_id
        self.has_a_secondary_port = has_a_secondary_port

        vlan_ids_for_this_device = [vlan_id for vlan_id in vlan_ids_input_rows if vlan_id.device_id == device_id]

        self.primary_port_vlans = [vlan_id for vlan_id in vlan_ids_for_this_device if vlan_id.primary_port]
        self.secondary_port_vlans = [vlan_id for vlan_id in vlan_ids_for_this_device if not vlan_id.primary_port]


class Request:
    def __init__(self, request_id, requires_redundancy):
        self.request_id = request_id
        self.requires_redundancy = requires_redundancy

    @staticmethod
    def get_requests_from_csv(requests_csv_path):
        requests = []
        with open(requests_csv_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_request = Request(request_id=int(row['request_id']),
                                      requires_redundancy=bool(int(row['redundant'])))
                requests.append(new_request)

        return requests


if __name__ == '__main__':
    main(vlans_csv_path="./test_vlans.csv", requests_csv_path="./test_requests.csv", output_path="./test_output2.csv")
