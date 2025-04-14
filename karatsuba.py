#karatsuba --> divide and conquer
def karatsuba_multiply(num1_str:str, num2_str:str) -> str:
    # base case
    if len(num1_str) == 1 or len(num2_str) == 1:
        return str(int(num1_str) * int(num2_str))

    # make the numbers the same length
    max_len = max(len(num1_str), len(num2_str))
    half_len = max_len // 2

    # split the numbers into halves
    a = num1_str[:-half_len]
    b = num1_str[-half_len:]
    c = num2_str[:-half_len]
    d = num2_str[-half_len:]

    # recursively calculate three products
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    abcd = karatsuba_multiply(str(int(a) + int(b)), str(int(c) + int(d)))

    # combine the results using the formula
    return str(int(ac) * (10 ** (2 * (max_len - half_len))) + (int(abcd) - int(ac) - int(bd)) * (10 ** (max_len - half_len)) + int(bd))