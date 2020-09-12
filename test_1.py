# Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом.
# Оценить эффективность своего решения.

import random

def bi_search(target_array, search_value):
    start = 0
    end = len(target_array)

    while start < end:
        mid = (end + start)//2
        mid_element = target_array[mid]

        if mid_element < search_value:
            start = mid + 1
        elif mid_element > search_value:
            end = mid
        else:
            return True

    return False   
        


list_one = random.sample(range(50), 15)
list_two = random.sample(range(50), 15)

list_two.sort() # O(nlogn) сложность Timsort, которую использует Python

result = []
for el in list_one: # n раз проходимся на по массиву list_one
    if bi_search(list_two, el): # на каждой из n итераций делаем logn итераций поиска в list_two в худшем случае
        continue
    
    result.append(el)

# решение имеет сложность O(n logn)
assert all([x not in list_two for x in result])
print(list_one)
print(list_two)
print(result)
