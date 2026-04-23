def equality (num:int):
    sr = str(num)
    if num < 0:
        return False
    return sr == sr [::-1]

print(equality((12321)))