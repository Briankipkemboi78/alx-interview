#!/usr/bin/python3
'''Determines if a given data set represents a valid UTF-8 encoding.'''

def valid_utf8(data):
    '''Check if data is a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    '''
    # Number of bytes
    number_of_bytes = 0

    # Looping through dataset
    for num in data:
        # Get binary representation
        # Get least significant 8-bits
        binary_representation = format(num, '#010b')[-8:]

        # If no bytes, process new UTF-8 character
        if number_of_bytes == 0:
            # Get number of 1s at the beginning of string
            for bit in binary_representation:
                if bit == '0':
                    break
                number_of_bytes += 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False

        else:
            if not (binary_representation[0] == '1' and binary_representation[1] == '0'):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
