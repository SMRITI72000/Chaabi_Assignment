# making an extension dictionary

extension_dict = {'xls':'spreadsheet','xlxs':'spreadsheet','jpg':'image'}

# Empty list to input file types
input_list=[]


# User input
while True:
    file_name = input('Enter name of file or press -1 to quit')
    if file_name== '-1':
        break
    input_list.append(file_name)

#length of input_list
n = len(input_list)

answer = {}

for i in range(n):
    split_list = input_list[i].split(".")
    if split_list[-1] in extension_dict:
        answer[input_list[i]]=split_list[-1]
    else:
        answer[input_list[i]]="unknown"

print(answer)
