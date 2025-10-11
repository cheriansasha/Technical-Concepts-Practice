"""
Created a minimal Python script that demonstrates:

Script components:
1. Shebang line (#!/usr/bin/env python3) - tells system how to execute
2. Import statement - brings in required modules
3. Main logic - actual processing code

What it does:
1. Opens and reads a CSV file
2. Processes each row as a dictionary
3. Outputs formatted data

This demonstrates the core elements of any Python script: imports, file handling, 
data processing, and output - all in just 6 lines of code.
    
"""

#!/usr/bin/env python3
import csv

# Process CSV file
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: ${row['salary']}")