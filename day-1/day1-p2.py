import heapq

file_path = "data/day-1.txt"

values = []

current_value = 0

# Load the data from day-1.txt
with open(file_path, "r") as f:
    data = f.read()
    # Read the data into a list
    for line in data.splitlines():
        if line != "":
            current_value += int(line)
        else:
            values.append(current_value)
            current_value = 0

largest_values = heapq.nlargest(3, values)
largest_values_sum = sum(largest_values)

print(largest_values_sum)