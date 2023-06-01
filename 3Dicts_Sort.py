# Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g.
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"}
# ]
# AND
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "color")
# Should Output
# [
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"}
# ]


def sort_list_of_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

# Example usage
input_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

# Sort by 'fruit' key
sorted_list_by_fruit = sort_list_of_dicts(input_list, "fruit")
print(sorted_list_by_fruit)

# Sort by 'color' key
sorted_list_by_color = sort_list_of_dicts(input_list, "color")
print(sorted_list_by_color)
