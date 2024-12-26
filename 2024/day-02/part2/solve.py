from utils.process_input_file import process_input_file


min_diff_adjacent_levels, max_diff_adjacent_levels = 1, 3

def recursive_analyze_report(report: list):
    count_intervalles = len(report) - 1
    signed_diff_extreme_levels = report[-1] - report[0]
    
    if signed_diff_extreme_levels == 0:
        return False

    min_diff_extreme_levels = min_diff_adjacent_levels * count_intervalles
    max_diff_extreme_levels = max_diff_adjacent_levels * count_intervalles
    abs_diff_extreme_levels = abs(signed_diff_extreme_levels)
    if not(min_diff_extreme_levels <= abs_diff_extreme_levels <= max_diff_extreme_levels):
        return False
    
    if count_intervalles == 1:
        if signed_diff_extreme_levels > 0:
            return "increasing"
        else:
            return "decreasing"
    
    index_split_report = count_intervalles // 2
    if (analyze_first_subreport := recursive_analyze_report(report[:index_split_report+1])) and (analyze_second_subreport := recursive_analyze_report(report[index_split_report:])) and (analyze_first_subreport == analyze_second_subreport):
        return analyze_first_subreport
    else:
        return False
    
def solve():
    input_lines = process_input_file(file_solver_abspath=__file__.replace("part2", "part1"))

    count_safe_reports = 0

    for report in map(lambda line: list(map(int, line.rstrip().split(" "))), input_lines):
        is_safe_report = False
        for index_level in range(len(report)):
            subreport = report.copy()
            del subreport[index_level]
            is_safe_report = recursive_analyze_report(subreport)
            if is_safe_report:
                break
        if is_safe_report:
            count_safe_reports += 1
        else:
            count_safe_reports += bool(recursive_analyze_report(report))
    
    print(f"{count_safe_reports = }")

if __name__ == "__main__":
    solve()