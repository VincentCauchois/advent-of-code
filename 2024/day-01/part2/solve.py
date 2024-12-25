from utils.process_input_file import process_input_file
from collections import Counter

def solve():
    input_lines = process_input_file(file_solver_abspath=__file__.replace("part2", "part1"))
    first_list_locations, second_list_locations = zip(*(tuple(map(int, line.rstrip().split("  "))) for line in input_lines))
    counter_first_locations, counter_second_locations = Counter(first_list_locations), Counter(second_list_locations)
    result = sum((location * count_in_first_list * counter_second_locations[location] for location, count_in_first_list in counter_first_locations.items()))
    print(f"{result = }")

if __name__ == "__main__":
    solve()