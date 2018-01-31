#### Problem statement

The Telnyx Chicago Point of Presence has five network devices. Each device has a primary
port. Some devices also have a secondary port. Each port has a range of VLAN IDs that are
available for use.

We have incoming requests to reserve VLAN IDs for later use. Once a request reserves a VLAN
ID on a particular port and device, no other request may reserve that VLAN ID on that port and
device. There are two types of requests:

1. Requests that do not require redundancy - for these we would like to reserve a single
VLAN ID that meets the following criteria:
    1. The VLAN ID should be the lowest available VLAN ID on any **primary** port.
    1. In the event of a tie, we would choose the VLAN ID on the device with the lowest
device ID
1. Requests that require redundancy - for these we would like to reserve a pair of VLAN
IDs that meet the following criteria:
    1. One VLAN ID must be from a **primary** port and the other must be from a
**secondary** port
    1. The two ports must be on the same device
    1. The VLAN IDs must be the same on both ports
    1. The VLAN IDs should be the lowest possible IDs that meet the above criteria
    1. Again, in the event of a tie, we would choose the VLAN IDs on the device with
the lowest device ID

Write a program which will take vlans.csv and requests.csv as input and produce an output.csv
file that specifies which requests reserved which VLAN IDs on which port and device. There
should be one row for a request that does not require redundancy and two rows for a request
that does require redundancy.

To make your solution easier to evaluate, please sort your output.csv first ascending by
request_id and then ascending by primary_port. A working solution will produce test_output.csv
when provided test_vlans.csv and test_requests.csv as input.

Please treat this challenge as you would treat an actual problem to solve in a professional role.
At a minimum, this means:

1. Your solution must be correct for all possible inputs
1. Your solution must be efficient enough for production use
1. Your solution must be easy to read and understand
1. Your solution must include unit tests

Please submit the source files that make up your solution as well as your output.csv file.

#### CSV Specifications

1. vlans.csv - This file specifies which devices have secondary ports and which VLAN IDs
are available on every port prior to any requests
    1. device_id - Unique integer specifying a device
    1. primary_port - 1 if the port is the primary port on the device, 0 if it is the
secondary port on the device
    1. vlan_id - Integer value representing the VLAN ID
1. requests.csv - This file specifies the requests in the order they are received and whether
they require redundancy
    1. request_id - Unique integer specifying a request
    1. redundant - 1 if the request requires redundancy, and 0 if it does not
1. output.csv - This file is produced by your solution and specifies which VLAN IDs on
which port and device were reserved for which requests.
    1. request_id - Integer reference to the request_id in requests.csv
    1. device_id - Integer reference to the device_id in vlans.csv
    1. primary_port - 1 if the port is the primary port on the device, 0 if it is the
secondary port on the device
    1. vlan_id - Integer value representing the VLAN ID reserved


