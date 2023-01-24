# Chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

class Student(object):
    '''
    Student Class
    Author : Dave
    Date : 2023.01.23
    Description : Class, Static, Instance Method
    '''

    # Class Variable
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{},{}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # Instance Method
    def __str__(self):
        return 'Student Info -> name : {} grade: {} email: {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per): # 첫번째 인자가 클래스의 이름이라고 보면된다. 첫번째 인자는 cls가 아니라 다른 이름을 사용해도된다.
        if per <= 1:
            print('Please Enter 1 or More')
            return 
        cls.tuition_per = per
        print('Succeed! tuition increased!')

    # Class Method
    # class method를 사용해서 instance를 생성하는 것을 PEP에서 더 선호한다.
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    # Static Method는 cls나 self 같은거 안 받고, 내가 넘긴 인자만 받는다.
    # 요즘에는 Static Method는 잘 사용하지 않는 추세인 듯 하다.
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient.'

# 학생 인스턴스
student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student2@daum.net', '2', 500, 4.3)

# 기본정보
print(student_1)
print(student_2)

print()

# 전체 정보
print(student_1.detail_info())

# 학비 정보(인상전)
print(student_1.get_fee())
print(student_2.get_fee())

print()

# 학비 인상(클래스 메소드 미사용)
# 이렇게 직접 클래스 변수나 인스턴스 변수에 직접 접근하는 것은 좋지 않다.
Student.tuition_per = 1.2

# 학비 정보(인상후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

# 학비 인상(클래스 메소드 사용)
Student.raise_fee(1.5)

print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()

# 클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'Student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Sunghan', 'Student4@gmail.com', '4', 600, 4.1)

# 전체 정보
print(student_3.detail_info())
print(student_4.detail_info())
print()

# 학생 학비 변경 확인
print(student_3._tuition)
print(student_4._tuition)
print()

# 장학금 혜택 여부(스테이틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

print()

# 장학금 혜택 여부(스테이틱 메소드 사용)
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()

print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))