# 주어진 두 정렬된 배열을 하나의 배열 안에 작은 순서대로 병합하기

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8, 9, 20]

capacity = len(arr1 + arr2)
result = [None] * capacity

ptr1 = 0
ptr2 = 0

for i in range(0, capacity):
    if ptr1 >= len(arr1):
        result[i] = arr2[ptr2]
        ptr2 += 1
        print("ptr1 limit reached")

    elif ptr2 >= len(arr2):
        result[i] = arr1[ptr1]
        ptr1 += 1
        print("ptr2 limit reached")

    else:

        if arr1[ptr1] >= arr2[ptr2]:
            result[i] = arr2[ptr2]
            ptr2 += 1
            print(f"ptr1: {ptr1}, ptr2: {ptr2}, result: {result}")

        else:
            result[i] = arr1[ptr1]
            ptr1 += 1
            print(f"ptr1: {ptr1}, ptr2: {ptr2}, result: {result}")


print(result)

# 결과적으로 투 포인터를 사용해 각각 정렬된 배열의 인덱스를 추적하면서 더 작은 값을 먼저 result 결과값 배열에 추가하는 방식으로 해결.
# 각각의 포인터를 매 반복마다 각자 배열의 길이와 비교하고 초과하지 않는지 검증함으로써, 서로 다른 배열에 대한 병합도 가능함.
