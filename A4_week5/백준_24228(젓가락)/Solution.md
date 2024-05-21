## 풀이
원래는 젓가락의 종류를 숫자로 표현하여 만약 n이 3이라면 각각 0, 1, 2로 표현하고 chop이라는 배열에 append해주고, 짝이 맞으면 pop하여 r개의 짝을 만들면 현재까지의 전체 젓가락 개수를 세는 방식으로 작성하려고 했지만 계속하여 시간초과가 발생하여 생각해본 결과 규칙을 찾을 수 있었다.

```python
# 처음 코드
n, r = map(int, input().split())
chop = []
cnt = 1

while r > 0:
	for i in range(n):
		chop.append(i)
		#print(chop)
		chop.sort()
		#print(chop)
		if len(chop) >= 2 and chop[0] == chop[1]:
			chop.pop(0)
			chop.pop(1)
			r -= 1
			if r == 0:
				break
		cnt += 1
		#print(cnt, r)

print(cnt)
```

위에서 찾은 규칙은 전체 젓가락의 개수는 `짝의 개수 * 2 + 젓가락의 종류 - 1`이라는 것을 알아내어 결과코드를 도출해낼 수 있었다.
```python
n, r = map(int, input().split())

result = r * 2 + n - 1
print(result)
```
