file_path = "data/day-3.txt"
# file_path = "data/day-3-test.txt"

class Rucksack():
    def __init__(self):
        self.compartment_a = []
        self.compartment_b = []
        
    def load_compartments(self, data):
        list_data = list(data)
        compartment_length = len(list_data)       
        
        for i in range(0, compartment_length):
            if i < compartment_length / 2:
                self.compartment_a.append(list_data[i])
            else:
                self.compartment_b.append(list_data[i])
                
    def get_priority_value(self):
        item = self.find_similar_item()
        item_ord = ord(item)
        if(item_ord >= 65 and item_ord <= 90):
            return item_ord - 38
        elif(item_ord >= 97 and item_ord <= 122):
            return item_ord - 96
                
    def find_similar_item(self):
        """
            This function checks both compartments for the same item.
        """
        item_list = list(set(self.compartment_a).intersection(self.compartment_b))
        
        return item_list[0]
                
    def __str__(self):
        output_str = "Compartment A: " + str(self.compartment_a) + "\n"
        output_str += "Compartment B: " + str(self.compartment_b)
        return output_str

priorities = []
# Load the data from day-3.txt
with open(file_path, "r") as f:
    data = f.read()
    for d in data.splitlines():
        r = Rucksack()
        r.load_compartments(d)
        priorities.append(r.get_priority_value())

print(sum(priorities))
        