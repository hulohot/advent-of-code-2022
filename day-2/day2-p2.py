file_path = "data/day-2.txt"
# file_path = "data/day-2-test.txt"

# A : Rock - 1
# B : Paper - 2
# C : Scissors - 3

# X : Lose - 0
# Y : Draw - 3
# Z : Win - 6

def rock_paper_scissors(a, b):
    losing_map = {
        'A': 3,
        'B': 1,
        'C': 2
    }
    
    draw_map = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    
    winner_map = {
        'A': 2,
        'B': 3,
        'C': 1   
    }
    
    shape_score = 0
    winner_score = 0
    
    if (b == 'X'):
        # You need to lose
        winner_score = 0
        shape_score = losing_map[a]
    elif (b == 'Y'):
        # You need to Draw
        winner_score = 3
        shape_score = draw_map[a]
    elif (b == 'Z'):
        # You need to Win
        winner_score = 6
        shape_score = winner_map[a]
        
    # print("Shape score: " + str(shape_score))
    # print("Winner score: " + str(winner_score))
        
    return shape_score + winner_score

total_score = 0
current_value = 0

# Load the data from day-1.txt
with open(file_path, "r") as f:
    data = f.read()
    for d in data.splitlines():
        first_response = d.split(" ")[0].strip()
        second_response = d.split(" ")[1].strip()
        score = rock_paper_scissors(first_response, second_response)
        
        total_score += score
        
print(total_score)