#!/usr/bin/env python3

import sys
import signal
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

def print_statistics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")
    print()

def handle_interrupt(signal, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, handle_interrupt)

# Process each line from stdin
for line in sys.stdin:
    try:
        _, _, _, _, _, _, _, status_code_str, file_size_str = line.strip().split()
        status_code = int(status_code_str)
        file_size = int(file_size_str)

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except ValueError:
        # Skip invalid lines
        pass
