

def avg(*num_list: float) -> float:
    total = 0
    for num in num_list:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise TypeError("Wrong input data. Make sure everything is a number")
    return total / len(num_list)