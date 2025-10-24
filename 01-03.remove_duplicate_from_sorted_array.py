# 정렬된 배열에서 중복을 제거하고, 고유한 요소들만 남기기
# 단, 제자리에서 수정해야하며
# 고유한 요소의 개수를 반환

array = [1, 1, 2, 2, 2, 3, 4, 4, 5]

def solution1(arr):
    key = 0
    memo = None
    length = len(arr)

    def delete(target_arr, index):
        for i in range(index, len(target_arr) - 1):
            target_arr[i] = target_arr[i + 1]
        target_arr.pop()


    while key < len(arr):
        if memo != arr[key]:
            print("new memo applied!")
            memo = arr[key]
            key += 1
            print(f"memo: {memo}, array: {arr}")

        else:
            print("duplicate detected!")
            delete(arr, key)
            length -= 1
            print(f"memo: {memo}, array: {arr}")


    print(f"result array: {arr}, answer: {length}")
    return length


solution1(array)

# solution1 은 해결하면서 memo를 이용해 배열을 순회하면서 기존 값을 탐지하는 과정까지는 좋았으나
# 중복을 제거하는 과정에서 delete 반복문 함수를 통해 시간복잡도가 이중 for문에 해당하는 O(n2)로 증가하는 부분이 아쉬움..
# 시도는 좋았지만 투 포인터 활용한 더 좋은 방법이 있었음. 그래도 혼자 생각해서 푼게 어디야..