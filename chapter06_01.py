# Chapter06-1
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# 제네레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, list, Dict, Set, Tuple, unpacking, *args
# 공부할 것 : 반복형 객체 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from

# 반복 가능한 이유? -> iter() 함수 호출

t = 'ABCDEF'

# for 사용
for c in t:
    print('EX1-1 -', c)

print()

# while 사용
w = iter(t)
while True:
    try:
        print('EX1-2 -', next(w))
    except StopIteration:
        break

from collections import abc

# 반복형 확인
print('EX1-3 -', hasattr(t, '__iter__'))
print('EX1-3-1 -', hasattr(w, '__iter__'))
print('EX1-4 -', isinstance(t, abc.Iterable))
print('EX1-4-1 -', isinstance(w, abc.Iterable))

print()
print()

# next 사용

class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stop! Stop!')
        self._idx += 1
        return word

    def __iter__(self):
        print('Called __iter__')
        return self

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitIter('Who says the nights are for sleeping')
print('EX2-1 -', wi)
print('EX2-2 -', next(wi))
print('EX2-3 -', next(wi))
print('EX2-4 -', next(wi))
print('EX2-5 -', next(wi))
print('EX2-6 -', next(wi))
print('EX2-7 -', next(wi))
print('EX2-8 -', next(wi))
# print('EX2-9 -', next(wi)) # StopIteration 에러 발생

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제네레이터 완화
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. 딕셔너리, 리스트 한 번 호출 할 때 마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함

class WordSplitGenerator:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('Who says the nights are for sleeping')

wt = iter(wg)

print('EX3-1 -', wt)
print('EX3-2 -', next(wt))
print('EX3-3 -', next(wt))
print('EX3-4 -', next(wt))
print('EX3-5 -', next(wt))
print('EX3-6 -', next(wt))
print('EX3-7 -', next(wt))
print('EX3-8 -', next(wt))
# print('EX3-9 -', next(wt)) # StopIteration 에러 발생

print()
print()