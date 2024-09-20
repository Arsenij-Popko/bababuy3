a = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', "анаконда"]
print("List Before ", a)
temp_list = []
for i in a:
    if i not in temp_list:
        temp_list.append(i)

a = temp_list
print("List After removing duplicates ", a)