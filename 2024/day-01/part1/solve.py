from utils.process_input_file import process_input_file

def solve():
    input_lines = process_input_file(file_solver_abspath=__file__)
    first_list_locations, second_list_locations = zip(*(tuple(map(int, line.rstrip().split("  "))) for line in input_lines))
    sorted_first_list_locations, sorted_second_list_locations = sorted(first_list_locations), sorted(second_list_locations)
    result = sum(abs(first_location - second_location) for (first_location, second_location) in zip(sorted_first_list_locations, sorted_second_list_locations))
    print(f"result: {result}")

if __name__ == "__main__":
    solve()