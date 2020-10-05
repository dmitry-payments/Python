# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.


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

# Список с ценами
items_cost = list_gen(10, 10, 1000)
quick_sort(items_cost)
print(items_cost)

high_cost = len(items_cost)-1 # индекс дорогого товара
low_cost = 0 # индекс дешевого товара
max_sum = 0 # максимальная сумма товаров в чеке
while low_cost <= high_cost:
    max_sum += items_cost[high_cost]
    low_cost += 1
    high_cost -= 1

print(max_sum)
