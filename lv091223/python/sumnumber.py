def add(num1, num2):
    num1 = convertToInt(num1)
    num2 = convertToInt(num2)
    sum = num1 + num2
    sum = convertToStr(sum)
    return sum

def convertToInt(str):
    num = 0
    negative = str[0] == '-'
    if negative:
        str = str[1:]

    for i in range(len(str)):
        char = str[i]
        num = num * 10 + int(char)
    
    num = num if not negative else -num
    return num

def convertToStr(num):
    if num == 0:
        return '0'
    
    negative = False
    if num < 0:
        negative = True
        num = abs(num)
    
    string = ''
    while(num > 0):
        digit = num % 10
        string = str(digit) + string
        num = num // 10

    return string if not negative else '-' + string

print(add('-12','-1'))