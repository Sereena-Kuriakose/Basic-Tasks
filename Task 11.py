import re

mobile_number_pattern = re.compile(r'''
    ^                   # Start of the string
    [789]\d{9}          # Indian mobile numbers (starting with 7, 8, or 9 and followed by 9 digits)
    $                   # End of the string
    ''', re.VERBOSE)

# Example usage
mobile_number = "9876543210"
if mobile_number_pattern.match(mobile_number):
    print(f"{mobile_number} is a valid mobile number.")
else:
    print(f"{mobile_number} is not a valid mobile number.")
