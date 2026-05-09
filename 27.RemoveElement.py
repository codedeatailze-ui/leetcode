def remove_element(nums, val):
    nums = [int(x.strip()) for x in nums.split(',')]
    while val in nums:
        nums.remove(val)
    return f"nums: {nums}"

print(remove_element(input("Enter your array: "), int(input("Enter your value: "))))