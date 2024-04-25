# LCS

## LCS란?

- 최장 공통 부분 수열(Longest Common Subsequence)

### 분류

동적 프로그래밍 (Dynamic Programming)

### 예시

```
X=ABCBDAB
Y=BDCABA
```

위의 X와 Y에 대해 가장 긴 길이의 공통 부분 문자열을 찾는 문제이다.

위의 예에서 BCAB, BDAB가 있고 길이가 5 이상인 공통 부분 문자열은 없다.

- 그림 설명
  ![LSC](LSC1.png)
  ![LSC](LSC2.png)
  ![LSC](LSC3.png)
  ![LSC](LSC4.png)
  ![LSC](LSC5.png)

- 의사 코드
  ```
  Xi: x1, x2, ... , xi
  Yj: y1, y2, ... , yj

  ---------------------------------------------------------
  # 문자열 길이 구하기

  LCS(i,j) = Xi와 Yj의 LCS 길이

  LCS(i,j) = ┌ LCS(i-1,j-1)+1 | if (xi = yj)
  					 │
  					 └ max(LCS(i-1,j), LCS(i,j-1)) | if (xi != yj)

  ---------------------------------------------------------
  # 문자열 구하기

  LCS(i,j)가 0이 아닌 동안,
  	┌ LCS(i,j)가 LCS(i-1,j) 또는 LCS(i,j-1)와 같다면 해당 위치로 이동
  	│
  	└ 다르다면 LCS(i,j)일 때 문자열 저장 및 LCS(i-1,j-1)로 이동
  ```

## 문제 풀이 방법

- 시간 복잡도
  - 두 문자열을 기준으로 X가 n, Y가 m의 길이를 가진다면 시간복잡도는 O(MN)이다.

## 참고 링크

[LCS 참고 유튜브 영상](https://youtu.be/EAXDUxVYquY?si=OcURhKUIIYbb1KVu)
