import filecmp
import unittest

import os

import time

from assign_vlan_ids import output_csv_of_request_assignments

vlans_csv_headers = ['device_id', 'primary_port', 'vlan_id']
requests_csv_headers = ['request_id', 'redundant']
output_headers = ['request_id', 'device_id', 'primary_port', 'vlan_id']

base_path = './'
vlans_csv_path = base_path + 'unittest_vlans.csv'
requests_csv_path = base_path + 'unittest_requests.csv'
expected_output_csv_path = base_path + 'unittest_expected_output.csv'
actual_output_csv_path = base_path + 'unittest_actual_output.csv'


def save_setup_files(vlan_id_string, requests_string, expected_output_string=None):
    save_string_to_file(vlan_id_string, path=vlans_csv_path)
    save_string_to_file(requests_string, path=requests_csv_path)

    if expected_output_string:
        save_string_to_file(expected_output_string, path=expected_output_csv_path)


def save_string_to_file(string_to_save, path):
    rows = [row.strip() + '\n' for row in string_to_save.split('\n')]
    with open(path, 'w') as outfile:
        outfile.writelines(rows)


def remove_file(path, retries=3, sleep=0.1):
    """ I'm using this to fix an issue where the tests will sometimes fail because one of the CSV files can't be deleted.
    The error it shows is "The process cannot access the file because it is being used by another process"

    Solution from https://stackoverflow.com/a/45447192/4115031
    """
    for i in range(retries):
        try:
            os.remove(path)
        except WindowsError:
            time.sleep(sleep)
        else:
            break


class TestAssignVlanIdsToRequests(unittest.TestCase):

    def setUp(self):
        self.tearDownClass()

    @classmethod
    def tearDownClass(cls):
        for file_path in [vlans_csv_path, requests_csv_path, expected_output_csv_path, actual_output_csv_path]:
            if os.path.isfile(file_path):
                remove_file(file_path)

    def test_successful_nonredundant_request(self):
        vlans_data = """device_id,primary_port,vlan_id
                        1,1,1"""
        requests_data = """request_id,redundant
                            0,0"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,1,1"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_successful_redundant_request(self):
        vlans_data = """device_id,primary_port,vlan_id
                        1,1,1
                        1,0,1"""
        requests_data = """request_id,redundant
                            0,1"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,0,1
                                    0,1,1,1"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_successful_combined_redundant_and_nonredundant_requests(self):
        vlans_data = """device_id,primary_port,vlan_id
                        1,1,1
                        1,0,1
                        1,1,2"""
        requests_data = """request_id,redundant
                            0,1
                            1,0"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,0,1
                                    0,1,1,1
                                    1,1,1,2"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_nonredundant_request_not_assigned_to_available_secondary_port_vlan_ids(self):
        """ The idea here is to have secondary port VLAN IDs with no associated primary port VLAN IDs, and to have these
        secondary port VLAN IDs be lower than any available primary port VLAN IDs. Then make sure that the program
        doesn't get confused and only assigns an incoming request to a primary port VLAN ID.
        """
        vlans_data = """device_id,primary_port,vlan_id
                        1,0,1
                        1,0,2
                        1,0,3
                        1,1,4"""
        requests_data = """request_id,redundant
                            0,0"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,1,4"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_choose_lowest_device_id_when_multiple_available_vlan_ids_with_same_value(self):
        """ The idea here is to have secondary port VLAN IDs with no associated primary port VLAN IDs, and to have these
        secondary port VLAN IDs be lower than any available primary port VLAN IDs. Then make sure that the program
        doesn't get confused and only assigns an incoming request to a primary port VLAN ID.
        """
        vlans_data = """device_id,primary_port,vlan_id
                        3,1,1
                        2,1,1
                        1,1,1"""
        requests_data = """request_id,redundant
                            0,0"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,1,1"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_successful_redundant_request_passing_over_nonredundant_vlan_id(self):
        """ The idea here is to create a situation where the lowest available VLAN ID is not redundant, and to make
        sure that an incoming request for a redundant VLAN ID will pass over the nonredundant VLAN IDs and instead
        choose the lowest *redundant* VLAN ID.

        :return:
        """
        vlans_data = """device_id,primary_port,vlan_id
                        1,1,1
                        1,1,2
                        1,0,2"""
        requests_data = """request_id,redundant
                            0,1"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,0,2
                                    0,1,1,2"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_input_fields_in_a_different_order(self):
        vlans_data = """vlan_id,primary_port,device_id
                        1,1,1
                        1,0,1
                        2,1,1"""
        requests_data = """redundant,request_id
                            1,0
                            0,1"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,0,1
                                    0,1,1,1
                                    1,1,1,2"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_input_vlan_ids_out_of_order(self):
        """ In this test the CSV containing the VLAN IDs has them out of order.

        :return:
        """
        vlans_data = """device_id,primary_port,vlan_id
                        1,1,3
                        1,0,3
                        1,1,2"""
        requests_data = """request_id,redundant
                            0,1
                            1,0"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,0,3
                                    0,1,1,3
                                    1,1,1,2"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_motivating_example(self):
        """ This tests the example input and output given as part of the assignment to create this functionality.
        """
        vlans_data = """device_id,primary_port,vlan_id
                        0,1,2
                        0,1,5
                        0,1,8
                        0,0,2
                        0,0,3
                        0,0,4
                        0,0,6
                        0,0,7
                        0,0,8
                        0,0,10
                        1,1,1
                        1,1,5
                        1,1,6
                        1,1,9
                        1,0,1
                        1,0,4
                        1,0,5
                        1,0,7
                        2,1,1
                        2,1,4
                        2,1,10"""
        requests_data = """request_id,redundant
                            0,1
                            1,0
                            2,1
                            3,0
                            4,1"""
        expected_output_data = """request_id,device_id,primary_port,vlan_id
                                    0,1,0,1
                                    0,1,1,1
                                    1,2,1,1
                                    2,0,0,2
                                    2,0,1,2
                                    3,2,1,4
                                    4,1,0,5
                                    4,1,1,5"""
        save_setup_files(vlans_data, requests_data, expected_output_data)

        output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                          output_path=actual_output_csv_path)

        self.assertTrue(filecmp.cmp(expected_output_csv_path, actual_output_csv_path))

    def test_input_requests_out_of_order(self):
        """ The assignment stated that the input request CSV will always have the requests in the order in which they
        were received.
        """
        vlans_data = """device_id,primary_port,vlan_id
                        1,1,1
                        1,1,2"""
        requests_data = """request_id,redundant
                            2,0
                            1,0"""
        save_setup_files(vlans_data, requests_data)

        with self.assertRaises(RuntimeError) as error:
            output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                              output_path=actual_output_csv_path)

        self.assertEqual(error.exception.args[0], 'Request IDs in the CSV are not in order.')

    def test_more_requests_than_primary_port_vlan_ids(self):
        vlans_data = """device_id,primary_port,vlan_id"""
        requests_data = """request_id,redundant
                            0,0"""
        save_setup_files(vlans_data, requests_data)

        with self.assertRaises(AssertionError) as error:
            output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                              output_path=actual_output_csv_path)

        self.assertEqual(error.exception.args[0], 'Not enough available primary port VLAN IDs')

    def test_more_redundant_requests_than_redundant_vlan_ids(self):
        vlans_data = """device_id,primary_port,vlan_id
                        1,1,1"""
        requests_data = """request_id,redundant
                            0,1"""
        save_setup_files(vlans_data, requests_data)

        with self.assertRaises(RuntimeError) as error:
            output_csv_of_request_assignments(vlan_csv_path=vlans_csv_path, requests_csv_path=requests_csv_path,
                                              output_path=actual_output_csv_path)

        self.assertIn("Not enough available redundant VLAN IDs.", error.exception.args[0])


if __name__ == '__main__':
    unittest.main()
