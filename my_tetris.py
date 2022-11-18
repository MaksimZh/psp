def evaluate(field: list[str]) -> tuple[list[str], int]:
    new_field: list[str] = []
    full_line = "*" * len(field[0])
    line_count = 0
    for line in reversed(field):
        if line == full_line:
            line_count += 1
        else:
            new_field.append(line)
    empty_line = "." * len(field[0])
    new_field = [empty_line] * line_count + list(reversed(new_field))
    return new_field, line_count
