import os

# Process "input.txt" files: 
#   - Ignore first two lines
#   - Return a list of strings with each retrieved line as a string
def process_input_file(file_solver_abspath: str, file_name: str="input.txt"):
    file_path = os.path.join(os.path.dirname(file_solver_abspath), file_name)
    with open(file_path, "r") as file:
        return file.readlines()[2:]
        
def _test_process_input_file():
    result = process_input_file(file_solver_abspath="/home/vincent/advent-of-code/2024/day-01/part1/solve.py", file_name="input.txt")
    print(f'len(result) is {len(result)}')
    print(f'result[0] is {result[0]}')

if __name__ == "__main__":
    _test_process_input_file()