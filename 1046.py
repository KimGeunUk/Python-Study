#정수 3개를 입력받아 합과 평균을 출력해보자.

a,b,c = map(int, input().split())

print(a+b+c)
print('%.1f' %float((a+b+c)/3))