class Person:
    name = "김정연"  # name => 속성

    def hello(self):  # hello 메소드 호출될 때 객체를 self 받음
        print("hello")


person1 = Person()  # 객체 생성
person1.hello()

person1.name
