def longest_common_prefix(strs:str):
    strs = ["flower", "slow", "flight"]

    strs.sort()

    first = strs[0]
    last = strs[-1]

    result = ""
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            result += first[i]
        else:
            break

    return result
print(longest_common_prefix(strs=input("enter your 3 words :")))