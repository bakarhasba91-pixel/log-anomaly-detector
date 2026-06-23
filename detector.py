# log-anomaly-detector
# This script reads a log file and identifies potential unauthorized access attempts.

log_file = 'logfile.log'

try:
    with open(log_file, 'r') as file:
        for line in file:
            # We look for 'Failed' as a keyword for unauthorized access
            if "Failed" in line:
                print("Anomaly Found: " + line.strip())
except FileNotFoundError:
    print(f"Error: {log_file} not found. Please ensure the log file is present.")

