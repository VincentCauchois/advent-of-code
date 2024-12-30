from utils.process_input_file import process_input_file

def solve():
    input_lines = process_input_file(file_solver_abspath=__file__)
    
    input_matrix = list(map(lambda line: list(line.removesuffix('\n')), input_lines))

    count_lines = len(input_matrix)
    count_columns = len(input_matrix[0])
    max_index_column = count_columns - 1
    max_index_line = count_lines - 1

    count_xmas_occurences = 0
    
    for index_line in range(count_lines):
        for index_column in range(count_columns):
            current_letter = input_matrix[index_line][index_column]
            if current_letter != 'X':
                continue
            is_enough_left = index_column + 3 <= max_index_column
            is_enough_up = index_line + 3 <= max_index_line
            is_enough_right = index_column - 3 >= 0
            is_enough_down = index_line - 3 >= 0
            if is_enough_left:
                if input_matrix[index_line][index_column+1] == 'M' and input_matrix[index_line][index_column+2] == 'A' and input_matrix[index_line][index_column+3] == 'S':
                    count_xmas_occurences += 1
                if is_enough_up:
                    if input_matrix[index_line+1][index_column+1] == 'M' and input_matrix[index_line+2][index_column+2] == 'A' and input_matrix[index_line+3][index_column+3] == 'S':
                        count_xmas_occurences += 1
            if is_enough_up:
                if input_matrix[index_line+1][index_column] == 'M' and input_matrix[index_line+2][index_column] == 'A' and input_matrix[index_line+3][index_column] == 'S':
                    count_xmas_occurences += 1
                if is_enough_right:
                    if input_matrix[index_line+1][index_column-1] == 'M' and input_matrix[index_line+2][index_column-2] == 'A' and input_matrix[index_line+3][index_column-3] == 'S':
                        count_xmas_occurences += 1
            if is_enough_right:
                if input_matrix[index_line][index_column-1] == 'M' and input_matrix[index_line][index_column-2] == 'A' and input_matrix[index_line][index_column-3] == 'S':
                    count_xmas_occurences += 1
                if is_enough_down:
                    if input_matrix[index_line-1][index_column-1] == 'M' and input_matrix[index_line-2][index_column-2] == 'A' and input_matrix[index_line-3][index_column-3] == 'S':
                        count_xmas_occurences += 1
            if is_enough_down:
                if input_matrix[index_line-1][index_column] == 'M' and input_matrix[index_line-2][index_column] == 'A' and input_matrix[index_line-3][index_column] == 'S':
                    count_xmas_occurences += 1
                if is_enough_left:
                    if input_matrix[index_line-1][index_column+1] == 'M' and input_matrix[index_line-2][index_column+2] == 'A' and input_matrix[index_line-3][index_column+3] == 'S':
                        count_xmas_occurences += 1

    print(f"{count_xmas_occurences = }")

if __name__ == "__main__":
    solve()