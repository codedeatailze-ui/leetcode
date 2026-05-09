def longestCommonPrefix(strs):
    if not strs:
        return ""

    first_word = strs[0]
    prefix = []

    char_index = 0

    while char_index < len(first_word):
        current_char = first_word[char_index]

        for i in range(1, len(strs)):
            if char_index >= len(strs[i]) or strs[i][char_index] != current_char:
                return "".join(prefix)

        prefix.append(current_char)
        char_index += 1

    return "".join(prefix)
print(longestCommonPrefix(strs=input("inter your words: ")))