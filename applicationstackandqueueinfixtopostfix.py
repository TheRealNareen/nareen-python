def infix_to_postfix(expression: str) -> str:
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    right_associative = {"^"}
    opening_brackets = {"(", "{", "["}
    closing_bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char in opening_brackets:
            stack.append(char)
        elif char in closing_bracket_map:
            target_opening = closing_bracket_map[char]
            while stack and stack[-1] != target_opening:
                output.append(stack.pop())
            if stack and stack[-1] == target_opening:
                stack.pop()
        elif char in precedence:
            while stack and stack[-1] not in opening_brackets and (
                precedence[stack[-1]] > precedence[char] or
                (precedence[stack[-1]] == precedence[char] and char not in right_associative)
            ):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())
        
    return "".join(output)

while True:
    print("\n\nPress 1 to exit")
    ui = input("Enter infix expression: ")
    if ui == "1":
        print("Exiting.....")
        break
    else:
        print("Postfix expression:", infix_to_postfix(ui))
