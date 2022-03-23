def dec_to_bin(num):
    rems = ""
    while num != 0:
        rem = num % 2
        num = num // 2
        rems = str(rem) + rems
    return int(rems)


def bin_to_dec(num):
    res = 0
    num = str(num)[::-1]
    for power, digit in enumerate(num):
        digit = int(digit)
        if digit > 1:
            raise ValueError("Wrong Input. Try a valid binary number!")
        else:
            res += digit * (2 ** power)
    return res
