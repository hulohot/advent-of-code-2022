file_path = "data/day-1.txt"

max_value = 0
current_value = 0

# Load the data from day-1.txt
with open(file_path, "r") as f:
    data = f.read()
    # Read the data into a list
    for line in data.splitlines():
        if line != "":
            current_value += int(line)
        else:
            if current_value > max_value:
                max_value = current_value
            current_value = 0
            
print(max_value)