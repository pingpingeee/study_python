class Person:
    name = "김정연"  # name => 속성

    def hello(self):  # hello 메소드 호출될 때 객체를 self 받음
        print(Person.name + "님 안녕하세요")


person1 = Person()  # 객체 생성
person1.hello()

Person.name = "황서영"
person1.hello()
