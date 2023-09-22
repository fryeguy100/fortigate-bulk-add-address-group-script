# Fortigate Bulk Address Group

import os

# Replace with the path to your input file
input_file = "path/to/your/fortigate-cidr-bulk-add-input.txt"

# Replace with the path to your address group output file
output_file = "path/to/your/fortigate-bulk-add-addrgrp-output.txt"

# Address group name
addrgrp_name = "script-address-group-1"

# Remove the old output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

# Create an empty list to hold address members
addr_members = []

# Open files and process each line
with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
    outfile.write('config firewall addrgrp\n')  # Add this line to the top of the output file
    outfile.write(f'edit {addrgrp_name}\n')
    outfile.write('set member')

    for line in infile:
        subnet = line.strip()
        addr_members.append(subnet)

    # Write address members to output file
    for subnet in addr_members:
        outfile.write(f' {subnet}')

    outfile.write('\n')
    outfile.write('next\n')  # Add this line after address group definition
    outfile.write('end\n')  # Add this line to the end of the output file

