def sum_list(numbers):
    if 1<= len(numbers) <= 1000:
        for i in numbers:
            try:
                i = int(i)
            except:
                return
            if not -1000 <= i <= 1000:
                return
        return sum(numbers)
