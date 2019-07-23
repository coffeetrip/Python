def calc(x, y):
    try:
        return x + y, x - y, x * y, x / y
    except ZeroDivisionError:
        print("문자열 0으로는 나눌 수 없습니다.")