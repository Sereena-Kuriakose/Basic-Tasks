import re

ip_address_pattern = re.compile(r'''
    ^                           # Start of the string
    (                           # Group for the first three segments
        25[0-5]|                  # 250-255
        2[0-4][0-9]|              # 200-249
        1[0-9][0-9]|              # 100-199
        [1-9][0-9]|               # 10-99
        [0-9]                     # 0-9
    )
    \.
    (                           # Group for the fourth segment
        25[0-5]|                  # 250-255
        2[0-4][0-9]|              # 200-249
        1[0-9][0-9]|              # 100-199
        [1-9][0-9]|               # 10-99
        [0-9]                     # 0-9
    )
    \.
    (                           # Group for the fifth segment
        25[0-5]|                  # 250-255
        2[0-4][0-9]|              # 200-249
        1[0-9][0-9]|              # 100-199
        [1-9][0-9]|               # 10-99
        [0-9]                     # 0-9
    )
    \.
    (                           # Group for the sixth segment
        25[0-5]|                  # 250-255
        2[0-4][0-9]|              # 200-249
        1[0-9][0-9]|              # 100-199
        [1-9][0-9]|               # 10-99
        [0-9]                     # 0-9
    )
    $                           # End of the string
    ''', re.VERBOSE)

# Example usage
ip_address = "192.168.1.1"
if ip_address_pattern.match(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid address.")
