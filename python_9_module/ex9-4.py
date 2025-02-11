import time

# 그리니치 천문대 기준으로 1970년 1월 1일 0시 0분 0초 부터 경과된 시간(밀리세컨)
# 1739245489.433889
seconds = time.time()
print("time() : ", seconds)

seconds = time.gmtime()
print("gmtime() : ", seconds)

seconds = time.localtime(1739245489.433889)
print("localtime() 년 : ", seconds.tm_year)
print("localtime() 월 : ", seconds.tm_mon)
print("localtime() 일 : ", seconds.tm_mday)
print("localtime() 시 : ", seconds.tm_hour)
print("localtime() 분 : ", seconds.tm_min)
print("localtime() 초초 : ", seconds.tm_sec)
