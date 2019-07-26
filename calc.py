def postfix(text):
    stack = []
    for item in text.split():
        try:
            num = float(item)
            stack.append(num)
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            if item == "+":
                stack.append(a + b)
            elif item == "-":
                stack.append(a - b)
            elif item == "*":
                stack.append(a * b)
            elif item == "/":
                stack.append(a / b)
            else:
                raise Exception(f"Invalid operator: {item}")
    # if stack is empty return 0
    if not stack:
        return 0
    return stack.pop()
