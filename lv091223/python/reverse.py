def reverse(input):
    stack = []
    for i in range(len(input)):
        stack.append(input[i])
        print(stack)

    result = ''
    for char in range(len(stack)):
        result += stack.pop()
    return result

print(reverse('hello'))