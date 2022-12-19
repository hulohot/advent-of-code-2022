data_file_path = "data/day-4.txt"
test_file_path = "data/day-4-test.txt"

# Load the data
def load_data(file_path):
    with open(file_path, "r") as f:
        data = f.read()
        return data


def preprocess_data(data):
    """
    The orignal data is in the format:
    5-7,7-9
    The output should be two tuples with this format:
    (5, 7), (7, 9)
    """
    # Split the data into a list of strings
    data_list = data.split(",")
    # Split those lists on the "-"
    data_list = [d.split("-") for d in data_list]
    # Convert the strings to integers
    data_list = [[int(d) for d in dl] for dl in data_list]
    # Convert the list to a tuple
    data_list = [tuple(dl) for dl in data_list]
    return data_list


def is_fully_contained(tuple_a, tuple_b):
    """
    This function checks if tuple_a or tuple_b is fully contained
    within the other tuple.
    """
    start_inner, end_inner = tuple_a
    start_outer, end_outer = tuple_b
    return (
        start_inner >= start_outer
        and end_inner <= end_outer
        or start_inner <= start_outer
        and end_inner >= end_outer
    )


if __name__ == "__main__":
    # Load the data
    data = load_data(data_file_path)

    # Define the counter variable
    counter = 0

    # Loop through each line of data
    for d in data.splitlines():

        # Preprocess the data
        data_list = preprocess_data(d)

        # Check if fully contained
        if is_fully_contained(data_list[0], data_list[1]):
            counter += 1

    # Print the result
    print(f"The number of fully contained tuples is {counter}")
