#28
#28이 나온다. why?
#이해하기 쉽도록 num이라는 변수에 숫자를 붙여서 표기해보았다.

#def 함수0(num0) :
#    return num0 * 2
#
#def 함수1(num1) :
#    return 함수0(num1 + 2)
#
#def 함수2(num2) :
#    num3 = num2 + 10
#    return 함수1(num3)
#
#c = 함수2(2)
#print(c)

#이렇게 표시해도 똑값은 값 28이 출력되긴 한다. 하지만 꼭꼭꼭 알아두자. num = num + 10에서 첫번째 num은 변수가 되고, num + 10에서의 num은 우리가 대입해야할 값 2가 된다.
#따라서 결국 num = 2 + 10이 되고 함수1(12)로 return하게 된다. 그 다음부터는 쭉 순서를 따라가면 쉽게 28이 나온다는 것을 예측할 수 있다.
