from itertools import product
from math import prod
from utils.process_input_file import process_input_file

import re
    
def solve():
    input_lines = process_input_file(file_solver_abspath=__file__.replace("part2", "part1"))
    
    result = 0

    # Adding "do()" at the beginning to get sure that the first substring before any "don't()", in the original string,
    #   actually gets retrieved in `list_strings_do` below
    input_string = "do()" + "".join(input_lines)
    list_strings_dont = input_string.split("don't()")
    list_strings_do = [string_do for string_dont in list_strings_dont for string_do in string_dont.split('do()')[1:]]
    list_strings_mul = re.findall(r'\bmul\(\d{1,3},\d{1,3}\)', ''.join(list_strings_do))
    result += sum(map(lambda string: prod(map(int, string.removeprefix('mul(').removesuffix(')').split(','))), list_strings_mul))

    print(f"{result = }")

if __name__ == "__main__":
    solve()