# 1. 리스트 기본
# 리스트의 생성
numbers01 = [10, 20, 30]
empty_list = []


# 인덱싱
print(numbers01[0])
print(numbers01[-1]) # 역순의 경우 -1부터 끝 인덱스를 의미함
# 범위를 벗어난 인덱스를 지정하는 경우 IndexError 에러가 발생함


# 값 수정
# 리스트는 mutable이라 생성 후 요소 바꾸기가 가능함
print(numbers01)
numbers01[1] = 99
print(numbers01)



# 2. 요소의 추가와 삭제
numbers02 = [10, 20, 30]

# append 는 인자를 리스트 끝에 추가한다.
print(numbers02)
numbers02.append(40)
print(numbers02)

# extend는 여러 값을 펼쳐서 리스트의 끝에 추가한다.
numbers02.extend([50, 60])
print(numbers02)

# append vs extend
# a = [1, 2]
# a.append([3, 4])
# [1, 2, [3, 4]] <<< append는 extend처럼 배열이 인자로 주어져도 그걸 펼쳐서 저장하지 않음

# b = [1, 2]
# b.extend([3, 4])
# [1, 2, 3, 4]

# pop은 요소를 제거하면서 '그 값을' 반환한다.
# pop(0)은 앞 요소를 제거한 뒤, 나머지를 앞으로 당기게 되므로 O(N)의 시간 복잡도를 갖는다.
print(numbers02)
value02 = numbers02.pop()
print(value02)
print(numbers02)
value02 = numbers02.pop(1)
print(value02)
print(numbers02)

# remove는 해당 값의 첫 번째 등장만 삭제한다.
# 인자로 주어진 값이 리스트 안에 없는 경우 ValueError가 발생한다.
numbers02.remove(50)
print(numbers02)

# del은 인덱스 혹은 슬라이스 구간을 삭제할 수 있음
del numbers02[1]
print(numbers02)
del numbers02[1:3]
print(numbers02)


# 3. 길이와 포함 여부
# 리스트에서의 in 겁색은 일반적으로 O(N)이다.
# 이후 set에서는 평균 O(1) 조회를 배우게 된다.
numbers03 = [10, 20, 30, 40, 50]
print(len(numbers03))
print(20 in numbers03)
print(99 not in numbers03)


# 4. 슬라이싱
# 형식은 sequence[start:end:step] 이다. start 인덱스 요소는 포함, end 인덱스 요소는 미포함.
# 슬라이스는 새 리스트를 만든다.
# (그렇지만 이 리스트는 얕은 복사로 리스트 컨테이너는 복사하지만, 그 안에 들어 있는 mutable 객체까지 복사하지는 않는다.)
# 잘라낸 길이가 k 라면 대체로 O(k)시간과 공간이 든다.
numbers04 = [0, 1, 2, 3, 4, 5]
print(numbers04[1:4])
print(numbers04[:3])
print(numbers04[3:])
print(numbers04[::2])
print(numbers04[::-1])
print(numbers04[-2::-2])


# 5. 참조와 복사
# 같은 객체를 가리키는 경우는 다음과 같다.
numbers05 = [1, 2, 3]
numbers05b = numbers05
print(numbers05)
print(numbers05b)
numbers05b[0] = 99
print(numbers05) # << 원본의 0번 인덱스 값도 변경됨
print(numbers05b)

# 별도 리스트 복사
numbers05c = numbers05[:]
# 혹은 numbers05c = numbers05.copy() 를 사용한다.
# 다만 위 방식, 아래 방식 모두 얕은 복사로 내부에 중첩된 리스트를 요소로 갖고 있는 등의 mutable한 객체의 경우까지 완전히 복사되는 것은 아니다.


# 06. 2차원 리스트
# 기존 잘못된 생성 패턴은 아래와 같다.
board_wrong = [[0] * 3] * 3
# 위처럼 작성하는 경우 내부 행들이 같은 리스트를 공유하게 됨
print(board_wrong)
board_wrong[0][1] = 2
print(board_wrong)

# 안전한 2차원 리스트 작성
rows = 3
cols = 4
board06 = [[0] * cols for _ in range(rows)]
# 위 처럼만드는 경우 각 행을 반복문으로 새로운 내부 리스트를 만들게 된다.
print(board06)
board06[0][2] = 4
print(board06)


# 7. 문자열의 기본
# 문자열도 인덱싱, 슬라이싱이 가능하다.
text07 = "hello"
print(text07[0])
print(text07[-1])
print(text07[1:4])
print(text07[::-1])

# 다만, 문자열은 immutable이라 요소의 직접 수정이 불가능함.
# text[0] = 'H' <<< 이런식의 수정은 안됨


# 8. 문자열의 주요 메서드
# split
print("apple banana orange".split())
print("a, b, c".split(','))

# join
# 이 메서드는 호출자가 구분자가 된다.
words = ['apple', 'banana', 'orange']
print(" ".join(words))

# replace
# 원본 문자열이 바뀌지 않음. 따라서 값 저장이 필요하면 별도 변수 사용.
text08 = "hello world"
print(text08.replace("world", "python"))
print(text08)
text08_02 = text08.replace("world", "python")
print(text08)
print(text08_02)

# 기타 자주 쓰이는 메서드
print(text08.lower())
print(text08.upper())
print(text08.strip())
print(text08.find("lo"))
print(text08.count("l"))



# 9. 문자열 검사 메서드
char09_01 = "s"
char09_02 = "3"
char09_03 = " "

print(char09_01.isdigit())
print(char09_01.isalpha()) #호출자가 알파벳으로만 이루어졌는지 확인(공백 / 숫자 / 특수기호만 제외, 한글 같은 유니코드 계열 문자들은 True)
print(char09_02.isdigit())
print(char09_03.isspace())
print(char09_01.islower())
print(char09_01.isupper())



# 10 문자열 & 리스트 간 변환
chars10 = "python"
print(list(chars10))

# 문자열을 문자 리스트로
chars_list10 = list(chars10)
print(chars_list10)

# 문자 리스트를 문자열로
text10 = "".join(chars_list10)
print(text10)

# 정수 리스트를 "문자열"로
numbers10 = [1, 2, 3]
text_numbers10 = "".join(map(str, numbers10))
print(numbers10)
print(text_numbers10)

# 문자열 숫자를 정수 리스트로
reverse_numbers10 = list(map(int, text_numbers10))
print(text_numbers10)
print(reverse_numbers10)


# 11. 자주 사용되는 순회 패턴
numbers11 = [1, 2, 3, 4, 5]

# 값만 필요한 경우
# for value in numbers11:
#     ...

# 값과 인덱스가 필요한 경우
# for index, value in enumerate(numbers11):
#     ...

# 인접 값 비교
# for index in range(len(numbers11) - 1):
#     cur_value = numbers11[index]
#     next_value = numbers11[index + 1]
#     ...

# 인접 값 비교 2
# python 3.10 버전 이후부터는 pairwise 가 지원되어 두 인접값을 비교할 수 있음
# from itertools import pairwise
# for current, next_value in pairwise(numbers11):
#     ...

# 인접 값 비교 3
# zip 메서드를 사용하여 비교도 가능.(기존 리스트를 2번쨰 인덱스부터 복사하여 1:1 비교)
# for current, next_value in zip(numbers11, numbers11[1:]):
#     ...

board = [
    [1, 2, 3],
    [4, 5, 6]
]

def solution(a):
    answer = []
    print(a[len(a) -1][0])

    return answer

print(solution(board))