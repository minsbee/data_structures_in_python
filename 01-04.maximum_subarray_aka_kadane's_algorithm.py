# 제공된 배열에서 연속된 부분 배열의 합 중 가장 큰 값 찾기 (카데인 알고리즘)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# 우연히 주어진 케이스에 대한 답은 맞았지만 로직은 틀림..
def solution1(array):
    # 현재 max 값 혹은 현재 부분배열의 합을 0으로 초기화했는데 답이 음수인 경우에는 치명적인 오류가 될 수 있음.
    # 따라서 0이 아니라 배열의 첫 값으로 설정하는게 일반적임
    max_value = 0
    current_sum = 0
    # 전체 순환 오류(range 메서드는 주어진 끝 인덱스를 순회하지 않음..) 자바스크립트와 다르게 부등호 조절이 안되므로 첫 인덱스부터 끝까지 순회하기를 원한다면
    # 간단하게는 for i in array 혹은 range(len(array))로 가능하고 원래대로라면 range(0, len(array))로 작성해주면 된다.
    # 참고***** 반복문의 in 뒤에 바로 배열이 오는 경우 i는 배열의 인덱스가 아닌 값을 나타내고, range를 사용하게 되면 기존 반복문처럼 index를 나타냄*****
    for i in range(0, len(array) - 1):
        current_sum += array[i]
        if current_sum < 0:
            current_sum = 0
        max_value = max(max_value, current_sum)
        
    print(f"max value1: {max_value}")
    return max_value

solution1(arr)


def solution2(array):
    if not array:
        print(f"this is not an array. answer: {0}")
        return 0
    
    max_value = current_sum = array[0]
    for x in array[1:]:
        current_sum = max(x, current_sum + x)
        max_value = max(max_value, current_sum)
        
    print(f"max value2: {max_value}")
    return max_value

solution2(arr)


# 추가 설명
# 카데인 알고리즘은 왜 DP의 일종인가?
# DP는 여러가지 종류가 있음. 최적 부분구조, 중복 부분문제 해결, 메모이제이션 or 타뷸레이션 등
# 이 때, 카데인 알고리즘의 경우 1번, 2번을 만족하며 3번은 변수로 저장하는 방식으로 메모이제이션을 충족한다고 볼 수 있음
# 또한 카데인 알고리즘은 DP의 점화식을 그대로 사용함
# DP 점화식
# DP[i] = max(arr[i], DP[i - 1] + arr[i])
# 카데인 알고리즘
# current_sum = max(arr[i], current_sum + arr[i])

# 카데인 알고리즘은 DP의 공간복잡도 최적화 버전이라고 이해하면 됨
# 일반적인 DP의 경우 DP 배열 전체를 저장하여 O(n)의 공간복잡도를 이루고 있으나,
# 카데인 알고리즘의 경우 dp[i - 1]만 필요로 하므로 변수 하나, 즉 O(1)의 공간 복잡도를 가짐