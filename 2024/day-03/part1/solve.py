from itertools import product
from math import prod
from utils.process_input_file import process_input_file

import re
    
def solve():
    input_lines = process_input_file(file_solver_abspath=__file__)
    
    result = 0

    for line in input_lines:
        list_strings_mul = re.findall(r'\bmul\(\d{1,3},\d{1,3}\)', line)
        result += sum(map(lambda string: prod(map(int, string.removeprefix('mul(').removesuffix(')').split(','))), list_strings_mul))

    print(f"{result = }")

if __name__ == "__main__":
    solve()