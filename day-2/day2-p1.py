file_path = "data/day-2.txt"
# file_path = "data/day-2-test.txt"

# A : Rock
# B : Paper
# C : Scissors

# X : Rock
# Y : Paper
# Z : Scissors

def rock_paper_scissors(a, b):
    losing_map = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }
    
    winner_map = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'   
    }
    
    shape_score = 0
    if (b == 'X'):
        shape_score = 1
    elif (b == 'Y'):
        shape_score = 2
    elif (b == 'Z'):
        shape_score = 3
    
    winner_score = 0
    # Determine the winner
    if (winner_map[a] == b):
        winner_score = 6
    elif (losing_map[a] == b):
        winner_score = 0
    else:
        winner_score = 3
        
    return shape_score + winner_score

max_score = 0
current_value = 0

# Load the data from day-1.txt
with open(file_path, "r") as f:
    data = f.read()
    for d in data.splitlines():
        first_response = d.split(" ")[0].strip()
        second_response = d.split(" ")[1].strip()
        # print("First response: " + first_response)
        # print("Second response: " + second_response)
        score = rock_paper_scissors(first_response, second_response)
        
        # print(score)
        max_score += score
        
print(max_score)