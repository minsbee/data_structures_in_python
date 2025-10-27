# 온도 리스트 temperatures가 주어진다.
# 각 날짜에 대해, 더 따뜻한 날이 처음 나타나는 데 걸리는 일수를 구하라.
# 없으면 0 출력

# 입력: temperatures = [73,74,75,71,69,72,76,73]
# 출력: [1,1,4,2,1,1,0,0]

temperatures = [73,74,75,71,69,72,76,73]


def solution1(temper):
    stk = []
    answer = [0] * len(temper)
    
    for i in range(len(temper)):
        while stk and temper[-1] < temper[i]:
            last_idx = stk.pop()
            answer[last_idx] = i - last_idx
        
        stk.append(i)
        
        
    print(f"answer: {answer}")
    return answer
    
solution1(temperatures)


# 추가 해설: Daily Temperatures (모노토닉 스택 패턴)
#
# 핵심 개념: "미래가 과거의 답을 채워준다"
# - 일반적 발상: 각 날짜마다 뒤를 탐색 (브루트 포스, O(n²)) -> 처음 떠올린 것.. 아무래도 직관은 순차적인 순회를 생각하므로..
# - 스택 발상: 현재 날짜가 과거 날짜들의 답이 되어준다 (O(n))
#
# 알고리즘 흐름:
# 1. answer 배열을 0으로 초기화 (답을 못 찾은 경우 기본값으로 자동 세팅되도록)
# 2. 스택에는 "아직 더 따뜻한 날을 못 찾은 날짜의 인덱스"를 저장
# 3. 매 순회마다:
#    - 현재 온도가 스택 top의 온도보다 높으면 → pop하며 답 계산 (while로 조건 만족할 때까지 반복)
#    - 현재 인덱스를 스택에 push
# 4. 스택에 남은 날짜들은 답을 못 찾은 것 → answer가 0으로 유지됨
#
# 예시: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# i=0 (73): stk=[0]
# i=1 (74): 74>73 → 0 pop, answer[0]=1, stk=[1]
# i=2 (75): 75>74 → 1 pop, answer[1]=1, stk=[2]
# i=3 (71): 71<75 → stk=[2,3]
# i=4 (69): 69<71 → stk=[2,3,4]
# i=5 (72): 72>69 → 4 pop, answer[4]=1
#           72>71 → 3 pop, answer[3]=2
#           72<75 → stk=[2,5]
# i=6 (76): 76>72 → 5 pop, answer[5]=1
#           76>75 → 2 pop, answer[2]=4
#           stk=[6]
# i=7 (73): 73<76 → stk=[6,7]
# 최종: answer=[1,1,4,2,1,1,0,0]
#
# 시간복잡도: O(n) - 각 원소가 스택에 최대 1번 push, 1번 pop
# 공간복잡도: O(n) - 스택과 answer 배열
#
# 단조 스택(Monotonic Stack)이란?
# - 스택 내부 원소들이 단조 증가 또는 단조 감소하는 성질을 유지하는 스택
# - 이 문제에서는 온도가 감소하는 순서로 스택에 쌓임 (내림차순 스택)
# - "다음에 나올 더 큰/작은 값"을 찾는 문제에 자주 사용됨