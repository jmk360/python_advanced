# Chapter04-1
# 파이썬 심화
# 일급 함수(일급 객체) -> 함수를 객체 취급한다.
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달 가능 ex) sorted(key=len)
# 4. 함수 결과로 반환 가능

# 함수 객체 예제

def factorial(n):
    '''Factorial Function -> n:int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n - 1)

class A:
    pass

print('EX1-1 -', factorial(5))
print('EX1-2 -', factorial.__doc__)
print('EX1-3 -', type(factorial), type(A))
print('EX1-3-1 -', dir(factorial))
print('EX1-3-2 -', dir(A))
print()
print('EX1-4 -', set(sorted(dir(factorial))) - set(sorted(dir(A))))
print('EX1-5 -', factorial.__name__)
print('EX1-6 -', factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print('EX2-1 -', var_func)
print('EX2-2 -', var_func(5))
print('EX2-3 -', map(var_func, range(1, 6)))
print('EX2-4 -', list(map(var_func, range(1, 6))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order Function)

print('EX3-1 -', map(var_func, filter(lambda x: x % 2, range(1, 6))))
print('EX3-1-1 -', list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print('EX3-2 -', [var_func(i) for i in range(1, 6) if i % 2])

print()

# reduce()

from functools import reduce
from operator import add

print('EX3-3 -', reduce(add, range(1, 11))) # 누적
print('EX3-4 -', sum(range(1,11)))

# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 익명함수를 너무 많이 사용하는 것은 좋지 않지만, 적재적소에 사용하는 것은 매우 유용하다.
# 일반 함수 형태로 리팩토링 권장

print('EX3-5 -', reduce(lambda x,t: x+t, range(1,11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# dir 찍어 봤을때 __call__ 이놈이 있으면 함수명() 이런식으로 호출해서 사용 가능하다.

import random

# 로또 추첨 클래스 선언
class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]
    
    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self):
        return self.pick()

    # def __call__(self, a): # python에서는 하수 오버로딩은 지원하지 않는 것 같다.
    #     return ['dave', 'test']

    

# 객체 생성
game = LottoGame()

# 게임 실행
# 호출 가능 확인 : callable 함수를 사용해서 함수처럼 호출가능한지를 확인 할 수 있다.
print('EX4-1 -', callable(str), callable(list), callable(factorial), callable(3.14), callable(game)) 
print('EX4-2 -', game.pick())
print('EX4-3 -', game())
# print('EX4-3-1 -', game(1)) # python에서는 하수 오버로딩은 지원하지 않는 것 같다.
print('EX4-4 -', callable(game))

print()
print()

# 다양한 매개 변수 입력(*args, **kwargs)
def args_test(name, *contents, point=None, **attrs):
    return '<args_test> -> ({}) ({}) ({}) ({})'.format(name, contents, point, attrs)

print('EX5-1 -', args_test('test1'))
print('EX5-2 -', args_test('test1', 'test2'))
print('EX5-3 -', args_test('test1', 'test2', 'test3', id='admin'))
print('EX5-4 -', args_test('test1', 'test2', 'test3', id='admin', point=7))
print('EX5-5 -', args_test('test1', 'test2', 'test3', id='admin', point=7, password="1234"))

print()
print()

# 함수 Signatures -> python 2.x 때 후반 버전 부터 나옴
# signature는 깊게 보지 않아도 된다.
# sinature는 함수의 인자에 대한 정보를 표시 해줄수 있는 클래스 형태의 메소드이다.
# 이놈은 개발자를 위한 프레임워크를 만들지 않는 이상은 많이 사용되지는 않는다.
from inspect import signature

sg = signature(args_test)

print('EX6-1 -', sg) # 함수의 파라미터를 출력한다.
print('EX6-2 -', sg.parameters) # 함수의 파라미터를 자세히 출력한다.

print()

# 모든 정보 출력

for name, param in sg.parameters.items():
    print('EX6-3 -', name, param.kind, param.default)

print()
print()

# partial 사용법 : 인수 고정 -> 주로 특정 인수 고정 후 콜백 함수에 사용
# 하나 이상의 인수가 이미 할당된(채워진) 함수의 새 버전 반환
# 함수의 새 객체 타입은 이전함수의 자체를 기술하고 있다.
# partial은 많이 사용한다.
from operator import mul
from functools import partial

print('EX7-1 -', mul(10, 100))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print('EX7-2 -', five(100)) # 500
# print('EX7-2-1 -', five(100, 200)) # 에러 발생
print('EX7-3 -', six())
# print('EX7-3-1 -', six(100)) # 에러 발생
print('EX7-4 -', [five(i) for i in range(1, 11)])
print('EX7-5 -', list(map(five, range(1,11))))