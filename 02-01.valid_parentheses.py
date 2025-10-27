# 주어진 문자열 s가 올바른 괄호 쌍으로만 이루어져 있는지 판별하시오
# 괄호 종류: (), {}, []
# 출력 예시
# 1. 입력: s = "([{}])"
#    출력: True
# 2. 입력: s = "([)]"
#    출력: False

s1 = "([{}])"
s2 = "([)]"

def solution1(string):
    open_pair = ['(', '{', '[']
    parentheses = ['()', '{}', '[]']
    temp = []
    
    for x in string:
        if x in open_pair:
            temp.append(x)
        else:
            if not temp:
                print('False')
                return False
            last_value = temp.pop()
            if last_value + x not in parentheses:
                print('False')
                return False
            
    if not temp:
        print('True')
        return True
    
    print('False')
    return False

solution1(s1)
solution1(s2)

# 위 방식은 초보자가 이해하기 쉽도록 문자열 + 문자열이 저장된 쌍 리스트에 있는지 확인하는 방식으로 가독성이 좋음. 다만 비교해야 할 쌍이 많이 늘어나는 경우 시간복잡도상 딕셔너리 매칭 방식보다 살짝 불리함
# 전체 시간복잡도는 O(n)으로 같으나 개별 비교 시에 parentheses 비교와 딕셔너리 비교는 O(n) :O(1)으로 차이 존재

def solution_by_dict(string):
    pairs = {')': '(', '}': '{', ']': '['}
    temp = []

    for x in string:
        if x not in pairs:
            temp.append(x)
        else:
            if not temp:
                print('False')
                return False

            if pairs[x] != temp.pop():
                print('False')
                return False
        
    if not temp:
        print('True')
        return True

    print('False')
    return False