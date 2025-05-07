def boyer_moore_search(haystack: str, needle: str) -> list:
    if not needle:
        return []

    bad_char_shift = {char: i for i, char in enumerate(needle)}

    result = []
    i = 0
    while i <= len(haystack) - len(needle):
        j = len(needle) - 1
        while j >= 0 and needle[j] == haystack[i + j]:
            j -= 1
        if j < 0:
            result.append(i)
            i += 1
        else:
            bad_char_index = bad_char_shift.get(haystack[i + j], -1)
            shift = j - bad_char_index
            i += max(1, shift)
    return result


if __name__ == '__main__':
    haystack = "ababcabcababc"
    needle = "abc"
    positions = boyer_moore_search(haystack, needle)
    print(f"Підрядок '{needle}' знайдено в позиціях: {positions}")
