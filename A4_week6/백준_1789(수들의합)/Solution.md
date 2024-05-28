n까지 1부터 더해가다가 n보다 큰 값이 나오면 그 직전의 수(result-1)가 n의 최댓값이다.

이렇게 하는 방법도 있지만 -> 더 간단하게 코드 칠 수 있는 방법이 있다

### 공식 이용하기
```py
import math

def max_n(S):
    return int((-1 + math.sqrt(1 + 8 * S)) // 2)

# 입력 값을 받습니다.
S = int(input().strip())

# 최대 N을 계산하여 출력합니다.
print(max_n(S))
```
