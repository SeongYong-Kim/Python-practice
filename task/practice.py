def check_bracket(text):
    stack = []
    matching = {
        ')': '(',
        '}': '{',
        ']': '['
    }  # 괄호 간 매칭
    for index, letter in enumerate(text):
        if letter in '({[':
            stack.append(index)  # 여는 괄호이면 일단 push
        elif letter in matching:  # 닫는 괄호이면 괄호 쌍 매칭되는지 비교
            if stack == []:  # 닫는 괄호 들어왔는데 stack 비어있으면 해당 원소 index 스택에 push하고 check_bracket 종료
                stack.append(index)
                return stack
            elif list(enumerate(text))[stack[-1]][1] == matching[letter]:  # 현재 괄호의 index를 stack에 push하고 있음
                # stack[-1]의 index에 대응되는 letter는 list(enumerate(text))의 [stack[-1]][1]
                stack.pop()  # 매칭되는 top을 pop
            else:  # 여는 괄호가 stack에 들어 있는데 닫는 괄호가 stack의 top과 매칭되지 않는 경우 check_bracket 종료
                stack.append(index)
                return stack
    return stack  # 괄호 수, 순서, 쌍 다맞으면 stack에 남아 있는 원소 없다


if __name__ == "__main__":
    exp = input("input expression >> ")
    print(check_bracket(exp), '--->', check_bracket(exp) == [])
