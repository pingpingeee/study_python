class Cat:
    kor_name = "로키"
    eng_name = "rocky"
    age = 2

    def sound(self):
        print("야옹")


myCat = Cat()

print("한글 이름 : ", myCat.kor_name)  # 객체 속성으로 출력
print("영어 이름 : ", myCat.eng_name)
print("나이 : ", myCat.age)
myCat.sound()