#def maximum(a, b, c):
#    i = 0
#    if a > i :
#        i = a
#    if b > i :
#        i = b
#    if c > i :
#        i = c
#    print(i)
# maximum()은 3가지 중에 가장 큰 수를 출력하는 함수여야 한다.
# but 실행 결과 이건 세 '0 또는 자연수' a b c에서만 해당한다. a b c 모두 음수로 하였더니 0이 출력됐다.
# 초기 i의 값을 음수로 바꾸면 적당히 크지 않은 음수 a b c에 대해서도 가장 큰 수를 출력하는 함수를 만들 수 있다.
# 파이썬 내장함수 max도 a b c에 음수를 넣으면 0이 나온다. 신기함.