# 주어진 배열을 오른쪽으로 k만큼 회전시키기

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3


def solution1(array, n):
    # 주어진 회전 횟수가 배열의 전체 길이보다 길어질 수 있음. 그 경우 그냥 주어진 횟수로 자르려고 하는 경우 index range 에러 남
    m = n % len(array)

    sliced_arr = array[-m:]
    left_arr = array[:-m]
    result = sliced_arr + left_arr

    print(f"solution1 result: {result}")

solution1(arr, k)



def solution2(array, n):
    # 이 방식은 배열 공간을 새로 사용하지 않는 in-place(제자리) 회전 방식으로 면접에서 많이 물어봄 solution1 처럼 단순 회전 시키면
    # 내가 직접 배열 내 각 값들의 위치를 바꿔줄 수 있다는 점에 착안해서 내부에 뒤집기 함수를 만들어주면 인덱스에 따라 바로 변환이 가능함
    # 다만, 시간 복잡도는 반복문 사용에 따라 O(n)이 소요됨

    m = n % len(array)

    # 요걸 생각해내는게 처음에 어려울 수 있음
    def reverse(start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    reverse(0, len(array) - 1)
    reverse(0, m - 1)
    reverse(m, len(array) - 1)


    print(f"solution2 result: {array}")

solution2(arr, k)


def solution3(array, n):
    m = n % len(array)
    i = 0

    while i >= m:
        last_one = array[len(array)]
        array.pop()
        array.insert(0, last_one)

    print(f"solution3 result: {array}")

solution3(arr, k)