a=[1,2,3,4,5,6,7,8,9]
print(a)

print(a[4])

#빈 리스트 생성1
a=list()
print(a)

#빈 리스트 생성2
a=[]
print(a)

#크기가 N이고,모든 값이 0
n=10
a=[0]*n
print(a)

a=[1,2,3,4,5,6,7,8,9]
print(a[-1])

print(a[-3])

a[3]=7
print(a)

a=[1,2,3,4,5,6,7,8,9]

print(a[1:4])

#리스트 컴프리헨션

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array=[i for i in range(20) if i%2 == 1]

print(array)

#위와 같은 소스코드를 풀어쓰면
array=[]
for i in range(20):
    if i%2 == 1:
        array.append(i);

print(array)

#1부터 9까지의 수의 제곱 값을 포함하는 리스트
array=[i*i for i in range(1,10)]

print(array)

#n*m크기의 2차원 리스트 초기화(2차원 리스트를 사용할 때에는 반드시 컴프리헨션을 사용해야한다)
n=3
m=4
array=[[0]*m for _ in range(n)]

print(array)

#언더바는 언더바부분을 사용하지 않을 때 쓴다
for _ in range(5):
    print("HelloWorld")


#관련 메소드

a=[1,4,3]
print("기본메서드: ",a)

#원소 삽입(뒤에) (O(1)시간복잡도)
a.append(2)
print("삽입:",a)

#오름차순 정렬
a.sort()
print("오름차순 정렬: ",a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ",a)

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ",a)

#특정 인덱스에 데이터 추가(O(N)인 시간복잡도를 가지고 있기 때문에 많이 사용X)
a.insert(2,3)
print("인덱스2에 3을 추가: ",a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 세기: ",a.count(3))

#특정 값 데이터 삭제(O(N)인 시간복잡도를 가지고 있기 때문에 많이 사용X)
a.remove(1)
print("값이 1인 데이터 삭제: ",a)

#특정 값 원소를 모두 제거
a=[1,2,3,4,5,5,5]
remove_set=[3,5]

result=[i for i in a if i not in remove_set]
print(result)