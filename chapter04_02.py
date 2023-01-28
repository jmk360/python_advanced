# Chapter04-2
# 파이썬 심화
# 일급 함수(일급 객체)
# Decorator & Closure

# 파이썬 변수 범위(global)

# 예제1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5) # b가 정의가 안되어 있어서 에러 발생

# 예제2
b = 10

def func_v2(a):
    print(a)
    print(b)

func_v2(5)

# 예제3
b = 10

def func_v3(a):
    print(a)
    print(b)
    b = 5

# func_v3(5)

from dis import dis # dis는 byte코드의 실행을 흐름을 볼수 있는 패키지이다.

print('EX1-1 -')
print(dis(func_v3))

print()
print()

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언된 연결 정보를 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다.
# 이놈은 글로 이해하기는 어렵고, 코딩을 하면서 이해해야한다.

a = 10

print('EX2-1 -', a + 10)
print('EX2-2 -', a + 100)

# 결과를 누적 할 수 없을까?
print('EX2-3 -', sum(range(1, 51)))
print('EX2-4 -', sum(range(51, 101)))

print()
print()

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []
    
    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print('EX3-1 -', avg_cls(15))
print('EX3-2 -', avg_cls(35))
print('EX3-3 -', avg_cls(40))

print()
print()

# 클로저(Closure) 사용
# 클로저 패턴은 대부분 2개이상의 함수로 이루어져 있다.
# 이런것들을 활용하면, 함수형 프로그래밍이나, 누적 실행 횟수(마우스 클릭 횟수), 타이틀 누적(웹에서 클릭하는 누적), 로그 누적 같은 기능에 많이 사용되게 된다.
# 전역변수 사용 감소
# 디자인 패턴 적용 -> 많이 사용된다.
# 함수형 프로그래밍에서는 필수라고도 볼 수 있다.
# 은닉화도 가능하다.
# 단점은 함수가 끝났음에도, Free Variabel 변수는 계속 메모리에 남아 있기 때문에, 많이 사용하면, 자원(리소스)를 많이 잡아 먹는다.
# 그래서 꼭 필요한 부분에 사용해야 한다.

def closure_avg1():
    # Free Variabel(자유 변수 영역) : python에서는 외부 함수와 내부 함수의 사이를 Free Variabel(자유 변수 영역) 이라고 한다.

    series = []

    # 클로저 영역 : 내부 함수의 영역
    # -> 일반적으로 함수안에 선언된 지역변수는 함수가 끝나고 나면 소멸되지만 Free Variabel(자유 변수 영역)에 있는 변수는 소멸되지 않는다.
    def averager(v):
        # series = [] # Check
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_avg1()

print('EX4-1 -', avg_closure1)
print('EX4-1-1 -', avg_closure1(15))
print('EX4-1-2 -', avg_closure1(35))
print('EX4-1-3 -', avg_closure1(40))

print()
print()

# ---- 아래는 외울 필요없고, 그냥 한번 출력을 해본거다.
print('EX5-1 -', dir(avg_closure1))
print()
print('EX5-2 -', dir(avg_closure1.__code__))
print()
print('EX5-3 -', avg_closure1.__code__.co_freevars) # Free Variabel(자유 변수 영역) 의 변수를 출력한다.
print()
print('EX5-4 -', dir(avg_closure1.__closure__[0]))
print()
print('EX5-5 -', dir(avg_closure1.__closure__[0].cell_contents))
# ----

print()
print()

# 잘못된 클로저 사용 예
# 클로저 영역에서 '=' 이놈이 들어가면 클로저 영역 스코프에서 선언을 한거여서 Free variabel 영역의 변수가 아니다.
# 클로저 영역 변수라고 알려주기 위해서, nonlocal 키워드를 사용핟다.
# 클로저 패턴은 코딩을 하다 보면 이 패턴에서는 클로저 패턴을 사용해야 겠구나 하는 감이온다고 한다.

def closure_avg2():
    # Free Variabel
    cnt = 0
    total = 0
    # 클로저 영역
    def averager(v):
        nonlocal cnt, total # nonlocal cnt, total 해당 분분이 만약에 없으면 예외(에러)가 발생한다.
        cnt += 1
        total += v
        print('def2 >>> {} / {}'.format(total, cnt))
        return total / cnt
    return averager

avg_closure2 = closure_avg2()
print('EX5-5 -', avg_closure2(15))
print('EX5-6 -', avg_closure2(35))
print('EX5-7 -', avg_closure2(40))

# 데코레이터 실습
# 클로저 의 개념을 알아야 데코레이터를 사용할 수 있다.
# 데코레이터를 이용해서 만들면 좀더 세련되고, 파이썬을 잘활용한 기능을 구현해서, 중복된는 코드를 방지 할 수 있다.
# 데코레이터를 사용하면 장점
# 1. 중복 제거, 코드 간결
# 2. 클로저 보다 문법 간결
# 3. 조합해서 사용 용이
# -> 모듈화도 가능하기 때문에, 공통적으로 분리해서, 다수의 사람들이 협업을 할때, 이런 데코레이터를 하나 만들어 놓고,
#    함수의 앞, 뒤에서 꾸며주는 역활을 할 수가 있다.

# 단점
# 1. 너무 빈번하게 데코레이터를 쓰면 이해도에 따라서 가독성이 떨어질 수 있다., 디버깅이 어려워 질 수 있다.
# 2. 에러의 모호함
# 3. 에러 발생 지점 추적 어려움 -> 이거는 IDE 도움을 받아서 디버깅을 하면 문제는 없음

# 데코레이터는 재사용가능한 기능이 집약되어 있는 단일화 안된, 단순한 기능인데, 같은 계통의 성격과 어울리는 것을 데코레이터로 만들어 놓으면 좋다.
# 좀더 심화에 가면 데코레이터가 하나의 함수에 2개 이상 달려 있을 수도 있다.

import time

# 데코레이터 미사용

def perf_clock(func):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

def fact_func(n):
    return 1 if n < 2 else n * fact_func(n - 1)

non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

print('EX7-1 -', non_deco1, non_deco1.__code__.co_freevars)
print('EX7-2 -', non_deco2, non_deco2.__code__.co_freevars)
print('EX7-3 -', non_deco3, non_deco3.__code__.co_freevars)

print('*' * 40, 'Called Non Deco -> time_func')
print('EX7-4 -')
non_deco1(2)

print('*' * 40, 'Called Non Deco -> sum_func')
print('EX7-5 -')
non_deco2(100, 200, 300, 500)

print('*' * 40, 'Called Non Deco -> fact_func')
print('EX7-6 -')
non_deco3(5)

print()
print()
print()

# 데코레이터 사용

def perf_clock_2(func):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

@perf_clock_2
def time_func_2(seconds):
    time.sleep(seconds)

@perf_clock_2
def sum_func_2(*numbers):
    return sum(numbers)

@perf_clock_2
def fact_func_2(n):
    return 1 if n < 2 else n * fact_func(n - 1)

print('*' * 40, 'Called Deco -> time_func')
print('EX7-7 -')
time_func_2(2)

print('*' * 40, 'Called Deco -> sum_func')
print('EX7-8 -')
sum_func_2(10, 20, 30, 40, 50)

print('*' * 40, 'Called Deco -> fact_func')
print('EX7-9 -')
fact_func_2(5)