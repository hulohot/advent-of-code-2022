file_path = "data/day-3.txt"
# file_path = "data/day-3-test.txt"

class Group():
    def __init__(self, elf_a, elf_b, elf_c):
        self.elf_a_rucksack = elf_a
        self.elf_b_rucksack = elf_b
        self.elf_c_rucksack = elf_c
        
    def find_group_item(self):
        s1 = set(self.elf_a_rucksack)
        s2 = set(self.elf_b_rucksack)
        s3 = set(self.elf_c_rucksack)
        
        set1 = s1.intersection(s2)
        result_set = set1.intersection(s3)
        result_list = list(result_set)
        return result_list[0]
    
    def get_priority_value(self):
        item = self.find_group_item()
        item_ord = ord(item)
        if(item_ord >= 65 and item_ord <= 90):
            return item_ord - 38
        elif(item_ord >= 97 and item_ord <= 122):
            return item_ord - 96
        
priorities = []
# Load the data from day-3.txt
with open(file_path, "r") as f:
    data = f.read()
    idx = 0
    for d in data.splitlines():
        if idx == 0:
            items = []
        items.append(d)
        
        idx += 1
        if idx == 3:
            idx = 0
            g = Group(items[0], items[1], items[2])
            item = g.find_group_item()
            priorities.append(g.get_priority_value())
        
print(sum(priorities))
