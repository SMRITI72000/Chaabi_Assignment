from datetime import date
def diff_days(from_date,to_date,diff):
    list1 = from_date.split("-")
    list2 = to_date.split("-")

    from_datetime = date(int(list1[0]), int(list1[1]), int(list1[2]))
    to_datetime = date(int(list2[0]), int(list2[1]), int(list2[2]))

    date_diff = abs((to_datetime-from_datetime).days)

    if date_diff < diff:
        return True
    return False






from_date = input("Enter the from_date: ")

to_date = input("Enter the to_date: ")

diff = int(input("Enter the difference: "))

res = diff_days(from_date,to_date,diff)

print(res)

