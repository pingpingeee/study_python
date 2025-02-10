car = {"brand": "현대", "model": "아반떼", "start": 1990, "year": 2021}
print(car)

x = car.pop("start")  # key에 해당하는 value 추출
print(x)
print(car)

car.clear()  # 키와 값을 모두 삭제
print(car)
