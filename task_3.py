# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент 
# с нулевым значением.

import random
n_list = []
for i in range(1, (int(input('N: ')))+1):
    n_list.append(random.randint(-99, 100))
print(n_list,end=' => ')
for i in range(0, len(n_list)+1):
    if(n_list[i]<0):
        n_list.insert(i+1,0)
        i+=1
print(n_list)