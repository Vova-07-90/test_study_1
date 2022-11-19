list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = []
for i in range(3):
    list_3.append(list_1[i])
    for j in range(i, i + 1):
        list_3.append(list_2[j])
print(list_3)