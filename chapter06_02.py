# Chapter06-2
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# yield
# 코루틴(Coroutine)

# yield : 메인루틴 <-> 서브 루틴  ==> 메인루틴과 서브루틴과의 통신을 하게 해준다.
# 코루틴 제어, 코루틴 상태, 양방향 값 전송
# yield from

# 서브루틴 : 메인루틴에서 -> 리턴에 의해 호출 부분으로 돌아옴 ->  다시 프로세스 시작
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 수행 가능 -> 동시성 프로그래밍 가능
# 코루틴 : 코루틴 스케쥴링 오버헤드 매우 적다. -> 하나의 쓰레드에서 실행하기 때문에... -> 아주 적은 메모리로 왔다갔다 하기 때문에...
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# 코루틴 단점 : 코드가 왔다갔다 거리기때문에, 가독성이 현저하게 떨어진다. 이해하려면 디버깅을 정말 잘하여야 한다.
#              정말 병형처리가 필요한, 정말 대규모의 한번의 계산이 필요할때는 코루틴으로는 어쩔수 없다. 하나의 쓰레드만 이용하기 때문에...
#              그때는 멀티쓰레딩이나 멀티프로세싱을 사용한다.

# 코루틴 예제1

def coroutine1():
    print('>>> coroutine started.')
    i = yield # yield 왼쪽 변수는 메인루틴에서 서브루틴으로 데이터를 주는 것이고, yield 오른쪽 변수는 서브루린에서 메인루틴으로 데이터를 주는 것이다.
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언

c1 = coroutine1()

print('EX1-1 -', c1, type(c1))

# yield 실행 전까지 진행
# next(c1)

# 기본으로 None 전달
# next(c1) # StopIteration 예외 발생

# 값 전송
# c1.send(100)

# 잘못된 사용

c2 = coroutine1()

# 예외 발생
# c2.send(100) # TypeError: can't send non-None value to a just-started generator ==> 제너레이터를 실행한 다음에 값을 보내야 한다.

# next(c2)

print()
print()

# 코루틴 예제2
# 코루틴의 상태를 보여주는 좋은 메소드들이 있다.

# GEN_CREATED : 처음 대기 상태 ==> next()를 호출하기전 대기 상태를 의미한다.
# GEN_RUNNING : 실행 상태 ==> 한번이라도 next()를 호출한 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))

c3 = coroutine2(10)

from inspect import getgeneratorstate

print('EX1-2 -', getgeneratorstate(c3)) # GEN_CREATED

print(next(c3)) # 10
print('EX1-3 -', getgeneratorstate(c3)) # GEN_SUSPENDED

print(c3.send(15))

# print(c3.send(20)) # StopIteration 예외 발생

print()
print()

# 항상 코루틴의 시작은 next 함수를 호출해야만 시작한다.
# 그래서 데코레이터를 이용해서 코루틴을 만들면 next함수를 호출하지 않고 바로 사용할 수 있다.

# 데코레이터 패턴 

from functools import wraps # wraps 은 몰라도 됨

def coroutine(func):
    '''Decorator run until yield'''
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term

su = sumer()

print('EX2-1 -', su.send(100))
print('EX2-2 -', su.send(140))
print('EX2-3 -', su.send(60))

print()
print()

# 코루틴 예제3(예외처리)

class SampleException(Exception):
    '''설명에 사용할 예외 유형'''

def coroutine_except():
    print('>> coroutine started.')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing..')
            else:
                print('-> coroutine received : {}'.format(x))
    finally:
        print('-> coroutine ending')

exe_co = coroutine_except()
print('EX3-1 -', next(exe_co))
print('EX3-2 -', exe_co.send(10))
print('EX3-3 -', exe_co.send(100))
print('EX3-4 -', exe_co.throw(SampleException))
print('EX3-5 -', exe_co.send(1000))
print('EX3-6 -', exe_co.close()) # GEN_CLOSED
# print('EX3-5 -', exe_co.send(1000)) # StopIteration 발생 : close 했기 때문에...

print()
print()

# 코루틴 예제4(return)

def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return 'Average : {}'.format(avg)

avger2 = averager_re()

next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)

try:
    avger2.send(None)
except StopIteration as e:
    print('EX4-1 -', e.value)

# 실전에서 코루틴을 직접 구현하는 일은 거의 없다. -> 원리만 알고 있으면 된다.

print()
print()

# 코루틴 예제5(yeild from)
# StopIteration 자동 처리(3.7 -> await) : python3.7 버전 부터는 yield from 키워드가 await로 바꼈다.
# 중첩 코루틴 처리

def gen1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y

t1 = gen1()
print('EX5-1 -', next(t1))
print('EX5-2 -', next(t1))
print('EX5-3 -', next(t1))
print('EX5-4 -', next(t1))
print('EX5-5 -', next(t1))
# print('EX5-6 -', next(t1)) # StopIteration 예외 발생

t2 = gen1()

print('EX5-7 -', list(t2))

print()
print()

# 위의 gen1을 yield from을 사용해서 gen2로 치환할 수 있다.
def gen2():
    yield from 'AB'
    yield from range(1, 4)

t3 = gen2()

print('EX6-1 -', next(t3))
print('EX6-2 -', next(t3))
print('EX6-3 -', next(t3))
print('EX6-4 -', next(t3))
print('EX6-5 -', next(t3))
# print('EX6-6 -', next(t3)) # StopIteration 예외 발생

t4 = gen2()

print('EX6-7 -', list(t4))

print()
print()

# 메인 루틴에서 코루틴을 관리하는 함수를 만들고, 그 다음에 여러가지 코루틴을 만들어 놓고
# 메인 루틴안에서, 여러 코루틴에 next를 호출해서 서로 통신 관계를 유지 할 수 있다.

def gen3_sub():
    print('Sub coroutine.')
    x = yield 10
    print('Recv : ', str(x))
    x = yield 100
    print('Recv : ', str(x))

def gen4_main():
    yield from gen3_sub()

t5 = gen4_main()

print('EX7-1 -', next(t5))
print('EX7-2 -', t5.send(7))
print('EX7-3 -', t5.send(77))