import  time
def test01():
    print("Hi")
    time.sleep(5)


def test02():
    time.sleep(1.5)
    print("Method 2")

time01 = time.time()
test01()
time2 = time.time()
print "Total Exce time - ",time2 - time01


