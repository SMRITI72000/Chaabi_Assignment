
def sublist(list,first_index,last_index):
    answer=[]
    for ele in list[first_index:last_index:2]:
        answer.append(ele)

    return answer


list = [2,3,5,7,11,13,17,19,23,29,31,37,41]

first_index = int(input("Enter the first index: "))
last_index =  int(input("Enter the last index: "))

answer = sublist(list,first_index,last_index)

print(answer)
