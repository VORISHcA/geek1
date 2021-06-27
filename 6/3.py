from memory_profiler import profile


@profile
def profile_rec(*args):
    def recursion_odd(num, odd=0, even=0):
        if num == 0:
            return f'{odd}, {even}'
        if (num % 10) % 2 == 0:
            odd += 1
            return recursion_odd(num // 10, odd, even)
        else:
            even += 1
            return recursion_odd(num // 10, odd, even)
    return recursion_odd(*args)


print(profile_rec(4353463623))