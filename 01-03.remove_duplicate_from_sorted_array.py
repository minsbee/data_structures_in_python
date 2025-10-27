# 정렬된 배열에서 중복을 제거하고, 고유한 요소들만 남기기
# 단, 제자리에서 수정해야하며
# 고유한 요소의 개수를 반환

array = [1, 1, 2, 2, 2, 3, 4, 4, 5]
array2 = [1, 1, 2, 2, 2, 3, 4, 4, 5]

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


# 이번에는 투포인터를 사용하여 하나의 포인터는 순차적으로 배열의 값을 하나씩 스캔하고 나머지 하나의 포인터는 앞선 포인터가 스캔한 값과 현재 값을 대조하여 배열 값을 고유의 값으로 변환하면서 카운트한다.
# 배열을 1번만 순회하므로 시간복잡도는 O(n)이며, 공간은 기존 주어진 배열공간 내에서 (in-place) 문제를 해결하므로 O(1) 공간복잡도를 가지게 된다.
def solution2(arr):
    if len(arr) <= 1:
        print(f"no duplicate found. answer:{len(arr)}")
        return len(arr)
    
    write = 0
    for read in range(1, len(arr)):
        if arr[read] != arr[write]:
            write += 1
            arr[write] = arr[read]
            print(f"read: {read}, write: {write}, array: {arr}")
        
    # 문제에서는 따로 조건을 걸지 않았지만 만약 문제에서 고유한 요소도 출력하라는 조건이 있다면 write가 도달하지 못한 나머지 배열의 쓰레기 값들을 지워주는 부분이 필요함
    # 해당 문제에서는 이게 없어도 정답. 하지만 이게 있어도 시간 복잡도는 slice O(n)으로 기존 시간복잡도에 거의 영향 미치지 않음)
    del arr[write + 1:]
            
    print(f"result array2: {arr}, answer: {write + 1}")
    return write + 1
            
            
solution2(array2)
        