## 풀이
가장 먼저 막혔던 부분은 **파이썬으로 2차원 배열 입력받기** 였다.

C에서는 각각 열과 행을 나누어서 2차원 배열을 사용했지만, 파이썬에서는 `list`, `map`, `split`을 적절히 사용하면 한줄로 표현이 가능했다.

참고 사이트 : https://dailylifeofdeveloper.tistory.com/132 

근데 이 문제에서 입력은 공백을 사이에 두지 않기 때문에 아래와 같이 써야함
```python
c = [list(input()) for _ in range(n)]
```
