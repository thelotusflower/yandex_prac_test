# Дан массив целых чисел. Нужно удалить из него нули. 
# Можно использовать только О(1) дополнительной памяти.
import random

def main():
    array = [random.randint(-5, 5) for x in range(2 * (10 ** 2))]
    zeroes = 0
    
    for i in range(len(array)-1, -1, -1):
        if array[i] == 0:
            zeroes += 1
            array[i], array[-zeroes] = array[-zeroes], array[i]

    for i in range(zeroes):
        array.pop()

    return array


if __name__ == '__main__':
    arr = main()
    assert 0 not in arr