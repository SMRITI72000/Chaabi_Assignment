dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

swapped_dict = {value : key for key,value in dict.items()}

print(swapped_dict)