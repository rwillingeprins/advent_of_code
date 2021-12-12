with open('input/day10.txt') as file:
    chunk_lines = file.read().splitlines()

end_per_start = {'(': ')', '[': ']', '{': '}', '<': '>'}
score_per_syntax_error = {')': 3, ']': 57, '}': 1197, '>': 25137}
score_per_incomplete = {'(': 1, '[': 2, '{': 3, '<': 4}
syntax_error_score = 0
incomplete_scores = []
for line in chunk_lines:
    chunk_starts = []
    is_valid_syntax = True
    for character in line:
        if character in {'(', '[', '{', '<'}:
            chunk_starts.append(character)
        elif character == end_per_start[chunk_starts[-1]]:
            chunk_starts.pop()
        else:
            syntax_error_score += score_per_syntax_error[character]
            is_valid_syntax = False
            break
    if is_valid_syntax:
        incomplete_score = 0
        while chunk_starts:
            incomplete_score = incomplete_score * 5 + score_per_incomplete[chunk_starts.pop()]
        incomplete_scores.append(incomplete_score)
print(syntax_error_score)
print(sorted(incomplete_scores)[len(incomplete_scores) // 2])
