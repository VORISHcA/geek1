def func_1(nums):  # О(n)
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr





def without(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

from timeit import timeit
list_1 = list(range(50))

print(timeit("func_1(list_1)", globals=globals()))  # 3.8665799  # О(n)
print(timeit("without(list_1)", globals=globals()))  # 2.4330772000000005  # О(n), но без append