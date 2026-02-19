def countBinarySubstrings(s: str) -> int:
    prev_group = 0
    curr_group = 1
    result = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr_group += 1
        else:
            result += min(prev_group, curr_group)
            prev_group = curr_group
            curr_group = 1

    # last comparison
    result += min(prev_group, curr_group)

    return result
