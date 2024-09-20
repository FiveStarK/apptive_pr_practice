def add(a, b):
    return a + b


def subtract(a, b):
	return a -b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def pow(a, b):
    return a ** b


def abs(a):
    return a if a >= 0 else -a


def mod(a, b):
    return a % b


if __name__ == "__main__":
    # 간단한 테스트 코드
    print("Add: ", add(5, 3))
    print("Subtract: ", subtract(5, 3))
    print("Multiply: ", multiply(5, 3))
    print("Divide: ", divide(5, 3))
    print("Power: ", pow(5, 3))
    print("Absolute: ", abs(-5))
    print("Modulus: ", mod(5, 3))