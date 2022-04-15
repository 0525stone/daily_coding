"""
pandas의 결과들을 visualize 하기 위하여 matplotlib, seaborn, pandas 자체에서 제공하는 툴 사용

여러 그래프를 하나의 figure에 그리는 방법

add_subplt으로 ax 객체를 만듦.
- seaborn에서도 ax 뭐를 설정하여, 객체들을 추가하는 방법들이 있음.
- matplotlib의 경우,

Graph 객체 선언 방법
-ax1 = fig.add_subplot(2,1,1) # 이런식으로 해당fig 객체에서 위치를 잡아줄 수도 있고
-fig.add_subplot(2,1,1) # 이렇게 할 경우, 이 이후에 그리는 plot이 해당 위치에 그려지는 걸로 앎

Graph 종류
- 빈도 확인 : distplot histogram countplot
- 

"""

# %%
from re import L
import matplotlib.pyplot as plt

# %%
# Data (예시)
x = range(0, 100, 1)
print(x)



# %%
# 그래프 객체 생성
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(1,2,1) 
ax1.plot(x, x)

fig.add_subplot(1,2,2)
plt.plot(x,[2*t for t in x])

plt.show()








# %%

print(len(2*x))
# %%
