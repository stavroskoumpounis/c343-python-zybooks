def remove_leading_trailing_whitespace(s):
    start_idx = 0
    end_idx = len(s) - 1

    while start_idx < len(s) and s[start_idx] == ' ':
        start_idx += 1

    if start_idx < len(s):
        while end_idx >= 0 and s[end_idx] == ' ':
            end_idx -= 1

        new_str = s[start_idx:end_idx + 1]
    else:
        new_str = ""

    return new_str


input_str = input("Enter a string: ")
result = remove_leading_trailing_whitespace(input_str)
print(f"String without leading and trailing spaces: '{result}'")
