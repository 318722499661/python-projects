import time

def test():
    while True:
        for num in range(10, 0, -1):
            time.sleep(0.3)
            print(num)

test()