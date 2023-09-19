# fortigate-bulk-add-address-group-script
Fortigate Bulk Adding Objects to Address Groups


Fortigate Bulk Adding Address Objects to Address Group

Overview:

This Python script automates the process of adding multiple address objects to an address group on a FortiGate firewall. The script reads a list of CIDR notation IP address blocks from an input file and converts them into FortiGate CLI commands for address groups, which are then written to an output file. The output can be directly used to configure a FortiGate firewall.

Features:

Converts CIDR notation to CLI commands for adding each CIDR IP address block to the address group configuration. Generates an output file that can be used directly in FortiGate CLI. Adds config firewall address group and end statement commands to the output file

Prerequisites:

Python 3.x ipaddress module (built into Python's standard library)

Usage:

Clone the repository or download the script.
Modify the input_file and output_file variables in the script to specify your input and output file paths.
input_file = "path/to/your/fortigate-cidr-bulk-add-input.txt" output_file = "path/to/your/fortigate-cidr-bulk-output.txt"

Ensure your input file contains CIDR notation IP address blocks, one per line.
Example: 192.168.1.0/24 10.0.0.0/16

While this script can theoretically add as many objects to an Addresss Group that you need; make sure to limit the number of addresses to 300 addresses or less per address group. This is a standard limit among Fortigate firewalls.

Run the script again with new IP subnets to reate additional groups for each set of 300 IP's.

Run the script.
python fortigate-bulk-add-address-group-script.py


The output file will contain the CLI commands needed to add these address objects to an address group on a FortiGate firewall.

Example Output:

config firewall addrgrp
edit script-address-group-1
set member 192.168.1.0/24 172.16.0.0/16 10.0.0.0/8 10.1.2.0/24 172.31.0.0/16 192.168.100.0/24 10.20.30.0/24 172.18.0.0/16 192.168.50.0/24 10.100.0.0/16 192.168.2.0/24 172.19.0.0/16 10.5.0.0/16
next
end

Contributing: Feel free to open issues or pull requests if you have suggestions for improvements or bug fixes.

