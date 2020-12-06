def check_bracket(text):
    stack = []
    bracket_idx = []
    match = {')': '(', '}': '{', ']': '['}

    for index, letter in enumerate(text):
        if letter in '({[':
            stack.append(letter)
            bracket_idx.append(index)

        elif letter in ')}]':
            if len(stack) == 0:
                return False
            elif match[letter] == stack.pop():
                bracket_idx.append(index)
            else:
                return False
    if len(stack) != 0:
        return False

    return True, bracket_idx

if __name__ == '__main__':

    exp = input("inputexpression>> ")
    print(check_bracket(exp))

#text를 입력 시 text에 알맞은 괄호들이 나열되어 있다면 True와 괄호들의 index값을,
#알맞지 않은 괄호들이 나열되어 있다면 False를 return하는 함수를 작성하였습니다.
