import time


epc = time.time()
print(epc)

localTime = time.localtime(epc)
print(localTime.tm_year)
print(time.ctime(epc))
