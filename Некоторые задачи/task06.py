# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые баллы получают дипломы одинаковой степени.
# Призером олимпиады считается участник, получивший диплом не хуже III степени.
# По результатам олимпиады определите количество призеров.

def list_gen(size, of=-100, to=100):
    from random import randint
    return [randint(of, to) for _ in range(size)]


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


res = list_gen(10, 0, 10)
quick_sort(res)
res.reverse()

print(res)
max_mark = res[0]

num_result = 3
num_wins = 0
for el in res:
    if el < max_mark:
        num_result -= 1
        max_mark = el
    if num_result == 0:
        break
    num_wins += 1

print(num_wins)