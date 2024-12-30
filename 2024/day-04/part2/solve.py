from utils.process_input_file import process_input_file
    
def solve():
    input_lines = process_input_file(file_solver_abspath=__file__.replace("part2", "part1"))
    
    input_matrix = list(map(lambda line: list(line.removesuffix('\n')), input_lines))

    count_lines = len(input_matrix)
    count_columns = len(input_matrix[0])
    max_index_column = count_columns - 1
    max_index_line = count_lines - 1

    count_xmas_occurences = 0
    
    for index_line in range(count_lines):
        for index_column in range(count_columns):
            current_letter = input_matrix[index_line][index_column]
            if current_letter != 'A':
                continue
            is_enough_left = index_column + 1 <= max_index_column
            is_enough_up = index_line + 1 <= max_index_line
            is_enough_right = index_column - 1 >= 0
            is_enough_down = index_line - 1 >= 0
            if is_enough_left and is_enough_up and is_enough_right and is_enough_down:
                if ((input_matrix[index_line-1][index_column-1], input_matrix[index_line+1][index_column+1]) in [('M','S'),('S','M')]) and ((input_matrix[index_line-1][index_column+1], input_matrix[index_line+1][index_column-1]) in [('M','S'),('S','M')]):
                    count_xmas_occurences += 1

    print(f"{count_xmas_occurences = }")

if __name__ == "__main__":
    solve()