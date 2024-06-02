# Create a list of food items
food_list = ["apple", "banana", "carrot", "doughnut", "eggplant"]
print("Initial list:", food_list)

# Add a new item to the list
food_list.append("french fries")
print("After appending 'french fries':", food_list)

# Insert 'grapes' at the second position (index 1)
food_list.insert(1, "grapes")
print("After inserting 'grapes' at index 1:", food_list)

# Remove 'carrot' from the list
food_list.remove("carrot")
print("After removing 'carrot':", food_list)

# Remove the item at the third position (index 2)
removed_item = food_list.pop(2)
print("After popping item at index 2:", food_list)
print("Removed item:", removed_item)

# Access the first item (index 0)
first_item = food_list[0]
print("First item in the list:", first_item)

# Iterate through the list and print each item
print("Iterating through the list:")
for item in food_list:
    print(item)

# Check if 'apple' is in the list
if "apple" in food_list:
    print("'apple' is in the list")
else:
    print("'apple' is not in the list")
