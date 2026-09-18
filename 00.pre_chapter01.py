# 1. 변수의 기본 자료형
# Python은 변수를 선언할 때 타입을 따로 적지 않음

a=10
name="minsu"
is_valid=True

print(type(a))
print(type(name))
print(type(is_valid))

a = 10
b = 3.14
c = "hello"
d = True
e = None

for value in [a,b,c,d,e]:
    print(value, type(value))



# 2. None
# python의 None은 JS/TS의 null과 상ㄷ당히 비슷함

result = None
print(result)

# 조건문에서도 확인 가능
if result is None:
    print("값이 아직 없음")

# None 타입의 관례
print(result == None) # None은 특정 singleton 객체라 동일한 객체인지 확인하는 is를 주로 사용함.

print(result is None)



# 3. 여러 변수 한 번에 할당
a = 10
b = 20

a, b = 10, 20 # 이렇게 한번에 사용할 수 있음

print(a)
print(b)

a, b = b, a # 굉장히 편한 점은 중간 변수 없이 바로 서로 변수 값을 교환할 수 있음 (나중에 언패킹과 연결)

print(a, b)



# 4. 산술 연산자
a = 7
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(type(a / b))
print(a // b)
print(type(a // b))
print(a % b)
print(a ** b)

# / 와 // 의 차이는 매우 중요한데, / 같은 경우 딱 나누어 떨어지는 수인 경우에도 float 타입을 반환함
# 반면, //로 구한 몫의 경우 정수 타입이 출력됨. 이는 이진 탐색 같은데서 매우 자주 사용함.



# 5. 비교 연산자 (결과는 전부 bool 로 출력됨)
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)



# 6. and, or, not
age = 25
has_ticket = True

if age >= 20 and has_ticket:
    print("입장 가능")

if age >= 65 or age <= 7:
    print("할인 대상")

is_blocked = False

if not is_blocked:
    print("접속 가능")



# 7. Python 특유의 연속 비교
# 다른 언어와 달리 Python 에서는 비교 연산자를 이중으로 사용하여 한방에 비교가 가능하다.
# if 0 <= x < 10:

x = 5
print(0 <= x < 10)

# 이런 비교 방식은 코테에서 좌표 범위 검사할 때 아주아주 자주 사용함
# if 0 <= nx < n and 0 <= ny < m:
#     ...



# 8. == 와 is
# 둘은 다른 개념으로 == 는 좌우의 값이 같은지를 비교한다면, is 는 좌우의 값이 같은 객체를 가리키는지를 나타냄.
# 코테에서 일반 숫자나 문자열의 비교에는 웬만하면 is를 쓰지 않고 == 로 확인하며, None 과 같이 singleton 객체를 가리키는 경우만 특별하게 is를 사용

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

c = a

print(a is c)



# 9. in / not in (포함 여부 검사)

numbers = [10, 20, 30]

print(20 in numbers)
print(99 in numbers)
print(99 not in numbers)

# 그리고 포함 여부 검사는 문자열에서도 가능함
text = "hello python"
print("python" in text)
# 이 개념은 dict, set에서도 특히 많이 사용함



# 10. 형변환(문자열과 정수 / 실수 사이만 사용)
text = "123"
number = int(text)

print(text)
print(type(text))
print(number)
print(type(number))

