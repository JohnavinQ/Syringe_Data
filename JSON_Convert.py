import json

# Input and output file paths
txt_file = "pump_data_log.txt"
json_file = "pump_data_log.json"

data = []

with open(txt_file, "r") as infile:
    for line in infile:
        line = line.strip()
        if " - " in line:
            timestamp, message = line.split(" - ", 1)
            data.append({
                "timestamp": timestamp,
                "message": message
            })

# Write to JSON file
with open(json_file, "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Converted {txt_file} → {json_file}")