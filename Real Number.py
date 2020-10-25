a=157.93
print(a)

a=-1837.2
print(a)

a=5
print(a)

a=-.7
print(a)

#10억의 지수 표현 방식

a=1e9
print(a)

#752.5
a=75.25e1
print(a)

#3.954
a=3954e-3
print(a)


#0.3+0.6=0.9가 아니고 0.899999999인 미세한 오차가 있다 (2진수 때문에)
a=0.3+0.6
print(a)

if a==0.9:
    print(True)
else:
    print(False)


#반올림round 첫번째 인자는 실수형 데이터,두번째 인자는 반올림하고자 하는 위치-1
a=0.3+0.6
print(round(a))

if round(a,4)==0.9:
    print(True)
else:
    print(False)


