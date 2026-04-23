def roman_number(roman_num):
    roman_num = roman_num.upper()  
    dic = {"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
    
    roman_sum = 0
    for num in roman_num :
        roman_sum += dic[num]
    return roman_sum

print(roman_number(roman_num = input("enter your roman_number :")))