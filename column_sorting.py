list_of_dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

key = input("Enter the key you want to sort: ")

sorted_list_of_dict = sorted(list_of_dicts, key=lambda x: x[key])

for key in sorted_list_of_dict:
    print(key)