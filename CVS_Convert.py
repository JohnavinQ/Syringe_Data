import csv

# Input and output file paths
txt_file = "pump_data_log.txt"
csv_file = "pump_data_log.csv"

with open(txt_file, "r") as infile, open(csv_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["timestamp", "message"])  # CSV header

    for line in infile:
        if " - " in line:
            timestamp, message = line.strip().split(" - ", 1)
            writer.writerow([timestamp, message])

print(f"Converted {txt_file} to {csv_file}")