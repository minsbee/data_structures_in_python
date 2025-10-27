# 스택(Stack)은 기초적인 자료구조 중 하나로 후입선출(Last In First Out)의 전형적인 예시이다.
# 보통 '가장 최근 값'과 관련된 것들을 구현할 때 자주 사용됨
# 기본적으로 하나 이상의 스택 공간을 사용하게 되기 때문에 최소 O(n)의 공간복잡도를 가지게 되는 것이 특징이다.
# 반면 시간복잡도에서는 모든 연산이 O(1)의 상수 시간을 가지므로 매우 효율적임.
# 기본적으로 리스트 기반으로 스택을 구현함. (연결 리스트로도 구현 가능하나 난이도가 높아지는 것에 비해 코딩 테스트 수준에서는 리스트로도 충분)

class CustomStack:
    def __init__(self):
        self.stack = []
        
    # 가장 마지막 위치에 값 추가
    def push(self, item):
        self.stack.append(item)

    # 가장 마지막 값 제거 후 해당 값 반환
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack!")
        
        print(f"pop result: {self.stack.pop()}, stack: {self.stack}")
        return self.stack.pop()

    # 가장 마지막 값 제거 x, 해당 값 반환
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack!")
        
        print(f"peek result: {self.stack[-1]}")
        return self.stack[-1]
    
    # 스택이 비어있는지 확인
    def is_empty(self):
        return len(self.stack) == 0
    
    
    def __str__(self):
        return f"Stack: {self.stack}"
    
    
    
new_stack = CustomStack()

new_stack.push(1)
print(new_stack)
new_stack.push(2)
print(new_stack)
new_stack.push(3)
print(new_stack)

new_stack.pop()
print(new_stack)
new_stack.peek()

print(new_stack)