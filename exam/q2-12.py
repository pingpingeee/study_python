price = int(input("책값은?"))
sale = int(input("할인율은?"))
cp = int(input("배송료는?"))

print("책 값 : %d" % price)
print("할인율 : %d" % sale)
print("배송료 : %d" % cp)

result = price - (price * (sale / 100)) + cp

print("결제 금액 : %d원" % result)
