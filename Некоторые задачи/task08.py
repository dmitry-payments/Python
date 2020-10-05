# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67
from random import randint


def phone_list_gen(size):
    return [f"{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}" for _ in range(size)]

def quick_sort(nums):
    def partition(nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1
            j -= 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

phones = phone_list_gen(8)
print(phones)
quick_sort(phones)

print(phones)



