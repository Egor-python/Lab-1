from random import randint


def bin_to_int(binary_list: list[str]) -> list[int]:
    return [int(i, base=2) for i in binary_list]


def int_to_bin(int_list: list[int]) -> list[str]:
    return [bin(i) for i in int_list]

def bubble_sorting(binary_list: list[str]) -> list[str]:
    normal_list: list[int] = bin_to_int(binary_list)
    list_len: int = len(normal_list)
    for step in range(list_len):
        for i in range(list_len - step - 1):
            current_el: int = normal_list[i]
            next_el: int = normal_list[i+1]
            if current_el > next_el:
                normal_list[i] = next_el
                normal_list[i+1] = current_el

    res: list[str] = int_to_bin(normal_list)
    return res


binary_list: list[str] = [bin(randint(0,1000)) for i in range(20)]
print(bin_to_int(binary_list))

res = bubble_sorting(binary_list)
print(bin_to_int(res))
