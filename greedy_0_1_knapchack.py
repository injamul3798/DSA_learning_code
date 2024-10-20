# Define Item with value and weight
class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight
  
def greedy_0_1_knapchack(items,capacity):
    #sorts the item by value to weight ratio
    # First sort the item/value ratio and then revrserse it
    items.sort(key = lambda x: x.value/x.weight,reverse = True)
    
    total_value = 0
    for item in items:
        if item.weight <= capacity:
            capacity = capacity - item.weight
            total_value = total_value + item.value
        else:
            break
            
    print('Total Value: ',total_value)
            
    
# We have created three items with their value and weight      
items = [
    Item(60,10),
    Item(100,20),
    Item(120,30)
]

#Assume  Capacity of Bags is 50kg
capacity = 50
greedy_0_1_knapchack(items,capacity)
        
